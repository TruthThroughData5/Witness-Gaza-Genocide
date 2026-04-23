# 🇵🇸 Witness-Gaza-Genocide

> *"Every dataset is a testimony. Every number was a name, a family, a dream. All they ever asked for was the right to be human — to have a home, a country, and freedom."*

---

## What is this project?

A data witness project documenting the ongoing genocide in Gaza and the West Bank — Oct 2023 to present. We count because the world looks away. This is not a conflict. This is not a war. This is a genocide.

---

## Data Sources & What We Collected

| Source | What we extracted |
|--------|------------------|
| 🏥 Palestinian Ministry of Health | Daily martyrs, injured, children killed, medical staff killed |
| 🌍 OCHA oPt | West Bank casualties, settler attacks, aid shipments |
| 🩺 WHO EMRO | Hospital conditions, attacks on healthcare |
| 🏕️ UNRWA | Displacement numbers, shelter conditions |
| 🛰️ UNOSAT | Satellite-detected structural damage by governorate |
| 🔴 [I Am Not A Number — Tech for Palestine](https://data.techforpalestine.org) | Named martyr registry — 60,000+ names, ages, dates of birth. Because they were not numbers. |

---

## What the data covers

- Daily martyrs & injured in Gaza
- Daily casualties in the West Bank
- Named registry of 60,000+ martyrs
- Hospital conditions & attacks
- Aid shipments & humanitarian access
- Structural damage & displacement

---

## How we extracted the data

The extraction pipeline pulls live data from open-source APIs and saves it locally for analysis.

**Files extracted per source:**
- `killed_in_gaza` — 60,000+ named martyrs (name, age, sex, date of birth)
- `casualties_daily` — day-by-day killed & injured in Gaza with breakdown by children, women, press, medical staff
- `west_bank_daily` — day-by-day killed, injured & settler attacks in the West Bank
- `summary` — latest cumulative figures across all datasets

**Code:** `python/data_extraction.py`

---

## Tools Used

- **Python** — Data extraction & scraping
- **Power Query** — Data cleaning & transformation
- **Excel** — Data modeling
- **Tableau** — Interactive dashboard

---

## This project is a witness, not just an analysis.
