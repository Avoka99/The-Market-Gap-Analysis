# The Sugar Trap: Market Gap Analysis


## A. Executive Summary

This project analyzed a cleaned subset of the Open Food Facts dataset to find a real gap in the snack aisle. After filtering and wrangling the data into high-level categories, the clearest opportunity appeared in Sweet Snacks, especially products that can deliver higher protein without pushing sugar too high. The target high-protein, low-sugar quadrant is still relatively small, and a large share of those products are ultra-processed, which points to room for a cleaner-label alternative. The strongest ingredient signals in that quadrant were seeds, soy, and peanuts, making them the most practical formulation direction for a new product.

## B. Project Links

**Notebook**

https://github.com/Avoka99/The-Market-Gap-Analysis/blob/main/MarketGapAnalysis.ipynb

**Interactive Dashboard**

https://the-market-gap-analysis-dashboard.streamlit.app/

**Presentation**

https://docs.google.com/presentation/d/15ats-kO1orKKlO3OeXBGC5STOhqjAec5Epmj5dwzeXQ/edit?usp=sharing

**Video Walkthrough**

https://youtu.be/LDPHgYFM0HU


## C. Technical Explanation

Data cleaning focused on keeping a single working dataset with only the columns needed for the project, then removing rows with missing product names, categories, sugars, or proteins. I also converted the nutritional fields to numeric values and filtered out clearly invalid measurements such as negative values and impossible energy or macronutrient values. The result is a cleaner dataset that still keeps enough rows for analysis while staying aligned with the project brief.

My Choice was the NOVA and Nutri-Score analysis on the high-protein, low-sugar cluster. I added it because good macro numbers alone do not guarantee a good product, and this extra view shows whether the opportunity is dominated by ultra-processed products or whether there is room for cleaner-label alternatives.

________________________________________

---

## Business Problem

Helix CPG Partners engaged this analysis to answer the question:

> **"Where is the Blue Ocean in the snack aisle?"**

The objective was to identify product categories where consumer demand for healthier snacks is not adequately served by current market offerings.

---

## Objectives

* Clean and prepare the Open Food Facts dataset.
* Group thousands of raw product tags into meaningful high-level categories.
* Analyze the relationship between sugar and protein content.
* Identify products occupying the High Protein–Low Sugar opportunity space.
* Recommend a product opportunity supported by data.
* Build an interactive dashboard for business stakeholders.

---

## Dataset

**Source:** Open Food Facts

Dataset Used:

* English Open Food Facts Dataset
* Initial Sample: **500,000** products
* Final Clean Dataset: **38,528** products

The full dataset (~9 GB uncompressed) was not uploaded to the repository. Instead, a cleaned subset was generated for analysis.

---

## Data Cleaning

The following cleaning steps were performed:

* Selected only columns relevant to the project.
* Removed products with missing:

  * Product Name
  * Categories
  * Protein values
  * Sugar values
* Removed empty text fields.
* Converted nutritional columns into numeric values.
* Removed biologically impossible values:

  * Sugar outside 0–100 g
  * Protein outside 0–100 g
  * Fat outside 0–100 g
  * Carbohydrates outside 0–100 g
* Filtered unrealistic calorie values.

The cleaned dataset was exported as:

```text
market_gap_dataset.csv
```

---

## Category Wrangling

Raw Open Food Facts category tags were transformed into readable business categories using keyword matching.

High-level categories include:

* Sweet Snacks
* Savory Snacks
* Breakfast & Cereals
* Dairy
* Beverages
* Other / Meals

This simplified thousands of inconsistent product tags into business-friendly groups for analysis.

---

## Dashboard Features

The Streamlit dashboard provides:

* Interactive Sugar vs Protein scatter plot
* Product category filtering
* Adjustable High Protein threshold
* Adjustable Low Sugar threshold
* Market Gap KPI cards
* Dynamic business recommendation
* Hidden Gem ingredient analysis
* Nutri-Score distribution
* NOVA processing analysis

---

## Key Insight

Based on the analysis, the largest market opportunity lies within products that combine:

* Higher protein content
* Lower sugar content
* Good nutritional quality

These products represent an underserved segment where healthier snack alternatives can be developed.

---

## Candidate's Choice

Additional business value was added by analyzing:

* Nutri-Score distribution
* NOVA food processing classification

This allows stakeholders to evaluate not only nutritional composition but also product processing quality, leading to more informed product development decisions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Repository Structure

```text
.
├── MarketGapAnalysis.ipynb
├── MarketGapAnalysis.html
├── app.py
├── requirements.txt
├── README.md
```

---

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/Avoka99/The-Market-Gap-Analysis.git
cd The-Market-Gap-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

Open the local Streamlit URL displayed in your terminal.

---

## Future Improvements

* Incorporate the complete Open Food Facts dataset.
* Apply machine learning for product opportunity prediction.
* Add regional and country-specific market analysis.
* Perform ingredient-level nutritional clustering.
* Include consumer preference and pricing data.

---

## Author

**Benjamin Avoka Lahadi Assibi**

BSc Mathematics, University of Mines and Technology (UMaT)

GitHub: https://github.com/Avoka99

LinkedIn: https://www.linkedin.com/in/benjamin-avoka-l-a-99av

Email: [benjaminlahadi99@gmail.com]

---

## License

This project was developed for a technical assessment and educational purposes using the publicly available Open Food Facts dataset.

