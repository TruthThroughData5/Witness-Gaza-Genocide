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

---

## This project is a witness, not just an analysis.
