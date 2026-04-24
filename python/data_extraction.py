"""
Witness-Gaza-Genocide — Data Extraction Pipeline
=================================================
Sources:
  - Tech for Palestine (killed-in-gaza, casualties_daily, west_bank_daily)
  - OCHA HDX (humanitarian aid data)

All data is open-source and publicly available.
"""

import pandas as pd
import requests
import time
import os
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
OUTPUT_DIR = "raw_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Witness-Gaza-Genocide/1.0 (humanitarian data project)"
}

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


# ─────────────────────────────────────────────
# PHASE 1 — EXTRACTION
# ─────────────────────────────────────────────

def extract_killed_in_gaza():
    """
    Source: Tech for Palestine — I Am Not A Number
    URL: https://data.techforpalestine.org/api/v2/killed-in-gaza.csv
    Content: Named registry of martyrs (name, age, dob, sex)
    """
    log("Extracting: Killed in Gaza (named registry)...")

    url = "https://data.techforpalestine.org/api/v2/killed-in-gaza.csv"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))

    log(f"  → {len(df):,} records extracted")
    log(f"  → Columns: {df.columns.tolist()}")

    df.to_csv(f"{OUTPUT_DIR}/killed_in_gaza_raw.csv", index=False, encoding="utf-8-sig")
    log(f"  → Saved to {OUTPUT_DIR}/killed_in_gaza_raw.csv")
    return df


def extract_casualties_daily():
    """
    Source: Tech for Palestine — Daily Gaza Casualties
    URL: https://data.techforpalestine.org/api/v2/casualties_daily.csv
    Content: Daily killed/injured counts, breakdown by children/women/press/medical
    """
    log("Extracting: Daily casualties — Gaza...")

    url = "https://data.techforpalestine.org/api/v2/casualties_daily.csv"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))

    log(f"  → {len(df):,} daily records extracted")
    log(f"  → Date range: {df['report_date'].min()} → {df['report_date'].max()}")

    df.to_csv(f"{OUTPUT_DIR}/casualties_daily_raw.csv", index=False, encoding="utf-8-sig")
    log(f"  → Saved to {OUTPUT_DIR}/casualties_daily_raw.csv")
    return df


def extract_west_bank_daily():
    """
    Source: Tech for Palestine — Daily West Bank Casualties
    URL: https://data.techforpalestine.org/api/v2/west_bank_daily.csv
    Content: Daily killed/injured + settler attacks (sourced from OCHA Flash Updates)
    """
    log("Extracting: Daily casualties — West Bank...")

    url = "https://data.techforpalestine.org/api/v2/west_bank_daily.csv"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    from io import StringIO
    df = pd.read_csv(StringIO(response.text))

    log(f"  → {len(df):,} daily records extracted")
    log(f"  → Date range: {df['report_date'].min()} → {df['report_date'].max()}")

    df.to_csv(f"{OUTPUT_DIR}/west_bank_daily_raw.csv", index=False, encoding="utf-8-sig")
    log(f"  → Saved to {OUTPUT_DIR}/west_bank_daily_raw.csv")
    return df


def extract_summary():
    """
    Source: Tech for Palestine — Summary (latest cumulative figures)
    URL: https://data.techforpalestine.org/api/v2/summary.json
    Content: Latest totals for all datasets combined
    """
    log("Extracting: Summary (latest totals)...")

    url = "https://data.techforpalestine.org/api/v2/summary.json"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Flatten to DataFrame for easier use
    summary_rows = []
    for section, values in data.items():
        if isinstance(values, dict):
            for key, val in values.items():
                summary_rows.append({"section": section, "metric": key, "value": val})

    df = pd.DataFrame(summary_rows)
    df.to_csv(f"{OUTPUT_DIR}/summary_raw.csv", index=False, encoding="utf-8-sig")
    log(f"  → Saved to {OUTPUT_DIR}/summary_raw.csv")
    return df


# ─────────────────────────────────────────────
# PHASE 2 — CLEANING
# ─────────────────────────────────────────────

def clean_casualties(df):
    """
    Clean and standardize the daily casualties dataset.
    - Parse dates
    - Fill missing cumulative values forward
    - Add calculated columns
    """
    log("Cleaning: casualties_daily...")

    df = df.copy()

    # Standardize date
    df["report_date"] = pd.to_datetime(df["report_date"], errors="coerce")
    df = df.dropna(subset=["report_date"])
    df = df.sort_values("report_date").reset_index(drop=True)

    # Forward fill cumulative columns (they shouldn't have gaps)
    cum_cols = [c for c in df.columns if "cum" in c.lower()]
    df[cum_cols] = df[cum_cols].ffill()

    # Calculated columns
    if "ext_killed_children_cum" in df.columns and "killed_cum" in df.columns:
        df["child_pct"] = (
            df["ext_killed_children_cum"] / df["killed_cum"] * 100
        ).round(2)

    if "killed" in df.columns:
        df["rolling_7d_avg"] = df["killed"].rolling(7, min_periods=1).mean().round(2)

    # Add war day number
    start_date = pd.Timestamp("2023-10-07")
    df["war_day"] = (df["report_date"] - start_date).dt.days + 1

    log(f"  → {len(df):,} clean records | {df['report_date'].min().date()} → {df['report_date'].max().date()}")
    df.to_csv(f"{OUTPUT_DIR}/casualties_daily_clean.csv", index=False, encoding="utf-8-sig")
    return df


def clean_west_bank(df):
    """
    Clean West Bank daily dataset.
    """
    log("Cleaning: west_bank_daily...")

    df = df.copy()
    df["report_date"] = pd.to_datetime(df["report_date"], errors="coerce")
    df = df.dropna(subset=["report_date"])
    df = df.sort_values("report_date").reset_index(drop=True)

    cum_cols = [c for c in df.columns if "cum" in c.lower()]
    df[cum_cols] = df[cum_cols].ffill()

    start_date = pd.Timestamp("2023-10-07")
    df["war_day"] = (df["report_date"] - start_date).dt.days + 1

    log(f"  → {len(df):,} clean records")
    df.to_csv(f"{OUTPUT_DIR}/west_bank_daily_clean.csv", index=False, encoding="utf-8-sig")
    return df


def clean_killed_registry(df):
    """
    Clean the named martyrs registry.
    - Parse age groups
    - Standardize sex labels
    """
    log("Cleaning: killed_in_gaza registry...")

    df = df.copy()

    # Standardize sex
    df["sex"] = df["sex"].str.strip().str.lower()
    df["sex_label"] = df["sex"].map({"m": "Male", "f": "Female"}).fillna("Unknown")

    # Age groups
    def age_group(age):
        if pd.isna(age):
            return "Unknown"
        age = int(age)
        if age < 5:   return "0–4"
        if age < 13:  return "5–12"
        if age < 18:  return "13–17"
        if age < 30:  return "18–29"
        if age < 50:  return "30–49"
        if age < 65:  return "50–64"
        return "65+"

    df["age_group"] = df["age"].apply(age_group)

    # Parse dob
    if "dob" in df.columns:
        df["dob"] = pd.to_datetime(df["dob"], errors="coerce")

    log(f"  → {len(df):,} records | Sex dist: {df['sex'].value_counts().to_dict()}")
    df.to_csv(f"{OUTPUT_DIR}/killed_in_gaza_clean.csv", index=False, encoding="utf-8-sig")
    return df


# ─────────────────────────────────────────────
# PHASE 3 — INTEGRATION
# ─────────────────────────────────────────────

def build_master_dataset(df_casualties, df_westbank):
    """
    Merge Gaza and West Bank daily data on report_date.
    Creates a unified master file for Tableau / Excel.
    """
    log("Building master dataset...")

    master = pd.merge(
        df_casualties,
        df_westbank,
        on="report_date",
        how="left",
        suffixes=("_gaza", "_wb")
    )

    master.to_excel(f"{OUTPUT_DIR}/master_dataset.xlsx", index=False)
    log(f"  → Master dataset: {len(master):,} rows saved to {OUTPUT_DIR}/master_dataset.xlsx")
    return master


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    log("=" * 55)
    log("  Witness-Gaza-Genocide — Data Extraction Pipeline")
    log("=" * 55)

    # Extract
    df_killed    = extract_killed_in_gaza()
    time.sleep(1)
    df_cas       = extract_casualties_daily()
    time.sleep(1)
    df_wb        = extract_west_bank_daily()
    time.sleep(1)
    df_summary   = extract_summary()

    # Clean
    df_cas_clean = clean_casualties(df_cas)
    df_wb_clean  = clean_west_bank(df_wb)
    df_killed_clean = clean_killed_registry(df_killed)

    # Integrate
    master = build_master_dataset(df_cas_clean, df_wb_clean)

    log("=" * 55)
    log("  Done. Files saved in /raw_data/")
    log("=" * 55)
