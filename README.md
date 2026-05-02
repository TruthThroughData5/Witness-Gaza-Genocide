# Witness-Gaza-Genocide

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
---

## Project Structure & File Organization

To ensure transparency and reproducibility, the project is organized into dedicated directories:

*   **`/python`**: Contains the `data_extraction.py` script used for automated data scraping and API retrieval.
*   **`/raw_data`**: Contains all original, unaltered datasets (Aid, Infrastructure, Casualties, etc.) as initially collected from their respective sources.
*   **`/cleaned_data`**: Contains the final, processed Excel file featuring the **11 optimized Power Query models** ready for Tableau analysis.

## How we extracted the data

The extraction pipeline pulls live data from open-source APIs and saves it locally for analysis.

**Files extracted per source:**
- `killed_in_gaza` — 60,000+ named martyrs (name, age, sex, date of birth)
- `casualties_daily` — day-by-day killed & injured in Gaza with breakdown by children, women, press, medical staff
- `west_bank_daily` — day-by-day killed, injured & settler attacks in the West Bank
- `summary` — latest cumulative figures across all datasets.
- `Infrastructure Situation` — Hospitals and Aids 

**Code:** `python/data_extraction.py`
---
## Data Engineering & Transformation Methodology

Moving from raw fragments to a refined analytical model required a rigorous **ETL (Extract, Transform, Load)** pipeline. We processed the raw chaos of daily reports into **11 optimized queries** designed for high-performance modeling in **Tableau**.

### 1. The Story of the Raw Data
The raw input consisted of fragmented, multi-source records that we categorized into four main pillars:
*   **Aid & Logistics:** Tracking **Aid Delivery (Table_Aid_Daily)**, **Goods**, and **Crossing Points (معابر)** to document the blockade.
*   **The Victims (Casualties):** Aggregating **Names-gaza** (60k+ records), **Gaza_daily**, and **West Bank** records to ensure every martyr is accounted for.
*   **Infrastructure & Survival:** Analyzing **Building Damage**, **Housing**, and a specialized record for **Hospitals** to document the collapse of the healthcare system.

### 2. Ethical Data Decisions (The Philosophy of Cleaning)
In this project, "cleaning" was a moral imperative to ensure the data accurately reflects the genocide:
*   **Healthcare Realism:** Facilities reported as "Partially Functional" were re-categorized as **"Completely Damaged."** We refuse to let the desperate attempt to provide minimal care mask the initial act of systematic destruction.
*   **Identity Restoration:** We engineered a custom text-parsing algorithm to accurately group **Arabic composite family names** (e.g., *Ata Allah, Faraj Allah*). This ensures that when an entire family is eliminated, our data reflects that collective loss rather than treating it as isolated cases.

### 3. Dimensional Modeling (The Fact-Dim Bridge)
To enable complex cross-filtering across 11 queries, we engineered two primary "Master Keys":
*   **`Dim_Geography`**: A unified master list for all governorates and cities in Gaza and the West Bank, ensuring geographical consistency.
*   **`Dim_Date` (The Genocide Calendar)**: A master timeline featuring a **"War Day Counter"** starting October 7, 2023. This syncs Aid, Infrastructure, and Casualty data into one unified, temporal narrative.

### 4. Technical Optimization
*   **Decoupling for Precision:** We separated **Total Infrastructure Damage** from **Temporal Progression** files to prevent "Double Counting" while maintaining the ability to track the rate of destruction over time.
*   **Connection-Only Architecture:** To handle massive datasets (+90k records) without memory bottlenecks, we utilized a "Connection-Only" approach in Power Query, ensuring the Tableau model remains lightweight and responsive.

---

## Key Performance Indicators (KPIs)

### Human Cost
- Total martyrs & injured (cumulative) & daily rate
- 7-day rolling average of daily killings & injuries
- % of martyrs & injured who are children
- % of martyrs & injured who are women
- Journalists & medical staff killed & injured (cumulative)

### Age Distribution of Martyrs
- Infants (0–4 years)
- Children (5–12 years)
- Teenagers (13–17 years)
- Adults (18–59 years)
- Elderly (60+ years)

### Family Annihilation
- Families with highest number of martyrs
- Families completely wiped out (no survivors)
- Average martyrs per family name

### Injuries — Correlation Analysis
- Injured rate vs. % of buildings destroyed per governorate
- Injured rate vs. hospital shutdown dates
- Injured rate vs. aid trucks per day
- Injured rate over time — identifying escalation phases
- % of injured with no access to medical care

### Healthcare Collapse
- Hospitals out of service over time per governorate
- Correlation: hospital shutdown vs. spike in deaths & injuries in that area
- % of population left without any medical access
- Medical staff killed & injured (cumulative)

### Geographic Pattern — Strikes vs. Destruction
- Areas with highest casualties mapped against % of buildings destroyed
- Correlation between injury rate and structural damage per governorate

### Aid Starvation & Death
- Aid trucks per day vs. daily death & injury rate (correlation)
- Famine-related deaths vs. aid blockage periods
- Periods of zero aid entry vs. spikes in civilian casualties
- Starvation deaths as % of total martyrs over time

### Humanitarian Aid
- Average aid trucks per day vs. required (500/day pre-war)
- Aid coverage rate (% of need met)

### West Bank
- Daily casualties & injuries cumulative total
- Settler attacks (cumulative)
- Children killed & injured (cumulative)

### Structural Damage
- % of structures destroyed per governorate
- Total destroyed vs. damaged vs. possibly damaged

---



---

## Tools Used

- **Python + ClaudeAI + web scraping** — Data extraction & scraping
- **Power Query** — Data cleaning & transformation
- **Tableau** — Data Modelling & Interactive dashboard



---

## This project is a witness, not just an analysis.
