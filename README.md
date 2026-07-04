## A. Executive Summary

This project analyzed a cleaned subset of the Open Food Facts dataset to find a real gap in the snack aisle. After filtering and wrangling the data into high-level categories, the clearest opportunity appeared in Sweet Snacks, especially products that can deliver higher protein without pushing sugar too high. The target high-protein, low-sugar quadrant is still relatively small, and a large share of those products are ultra-processed, which points to room for a cleaner-label alternative. The strongest ingredient signals in that quadrant were seeds, soy, and peanuts, making them the most practical formulation direction for a new product.

## B. Project Links
•	Link to Notebook: https://github.com/Avoka99/The-Market-Gap-Analysis/blob/main/MarketGapAnalysis.ipynb

•	Link to Dashboard: https://the-market-gap-analysis-dashboard.streamlit.app/.

•	Link to Presentation: https://docs.google.com/presentation/d/15ats-kO1orKKlO3OeXBGC5STOhqjAec5Epmj5dwzeXQ/edit?usp=sharing (YouTube: https://youtu.be/LDPHgYFM0HU) 

## C. Technical Explanation

Data cleaning focused on keeping a single working dataset with only the columns needed for the project, then removing rows with missing product names, categories, sugars, or proteins. I also converted the nutritional fields to numeric values and filtered out clearly invalid measurements such as negative values and impossible energy or macronutrient values. The result is a cleaner dataset that still keeps enough rows for analysis while staying aligned with the project brief.

My Choice was the NOVA and Nutri-Score analysis on the high-protein, low-sugar cluster. I added it because good macro numbers alone do not guarantee a good product, and this extra view shows whether the opportunity is dominated by ultra-processed products or whether there is room for cleaner-label alternatives.

________________________________________

Project Brief: The "Sugar Trap" Market Gap Analysis
Client: Helix CPG Partners (Strategic Food & Beverage Consultancy)
Deliverable: Interactive Dashboard, Code Notebook & Insight Presentation
________________________________________
1. Business Context
Helix CPG Partners advises major food manufacturers on new product development. Our newest client, a global snack manufacturer, wants to launch a "Healthy Snacking" line. They believe the market is oversaturated with sugary treats, but they lack the data to prove where the specific gaps are.
They have hired us to answer one question: "Where is the 'Blue Ocean' in the snack aisle?"
Specifically, they are looking for product categories that are currently under-served—areas where consumer demand for health (e.g., High Protein, High Fiber) is not being met by current product offerings (which are mostly High Sugar, High Fat).
2. The Data
You will use the Open Food Facts dataset, a free, open, and massive database of food products from around the world.
•	Source: Open Food Facts Data
•	Format: CSV (Comma Separated Values)
•	Warning: The full dataset is massive (over 3GB). You are not expected to process the entire file. You should filter the data early or work with a manageable subset (e.g., the first 500,000 rows or specific categories).
3. Tooling Requirements
You have the flexibility to choose your development environment:
•	Option A (Recommended): Use a cloud-hosted notebook like Google Colab, or Deepnote, etc.
•	Option B: Use a local Jupyter Notebook or VS Code.
o	Condition: If you choose this, you must ensure your code is reproducible. Do not reference local file paths (e.g., C:/Downloads/...). Assume the dataset is in the same folder as your notebook.
•	Dashboarding: The final output must be a publicly accessible link (e.g., Tableau Public, Google Looker Studio, Streamlit Cloud, or PowerBI Web).
________________________________________
4. User Stories & Acceptance Criteria
Story 1: Data Ingestion & "The Clean Up"
As a Strategy Director,
I want a clean dataset that removes products with erroneous nutritional information,
So that my analysis is not skewed by bad data entry.
•	Acceptance Criteria:
o	Handle missing values: Decide what to do with rows that have null or empty sugars_100g, proteins_100g, or product_name.
o	Handle outliers: Filter out biologically impossible values.
o	Deliverable: A cleaned Pandas DataFrame or SQL table export.
Story 2: The Category Wrangler
As a Product Manager,
I want to group products into readable high-level categories,
So that I don't have to look at 10,000 unique, messy tags like en:chocolate-chip-cookies-with-nuts.
•	Acceptance Criteria:
o	The categories_tags column is a comma-separated string (e.g., en:snacks, en:sweet-snacks, en:biscuits). You must parse this string.
o	Create a logic to assign a "Primary Category" to each product based on keywords.
o	Create at least 5 distinct high-level buckets.
Story 3: The "Nutrient Matrix" Visualization
As a Marketing Lead,
I want to see a Scatter Plot comparing Sugar (X-axis) vs. Protein (Y-axis) for different categories,
So that I can visually spot where the products are clustered.
•	Acceptance Criteria:
o	Create a dashboard (PowerBI, Tableau, Streamlit, or Python-based charts) displaying this relationship.
o	Allow the user to filter the chart by the "High Level Categories" you created in Story 2.
o	Key Visual: Identify the "Empty Quadrant" (e.g., High Protein + Low Sugar).
Story 4: The Recommendation
As a Client,
I want a clear text recommendation on what product we should build,
So that I can take this to the R&D team.
•	Acceptance Criteria:
o	On the dashboard, include a "Key Insight" box.
o	Complete this sentence: "Based on the data, the biggest market opportunity is in [Category Name], specifically targeting products with [X]g of protein and less than [Y]g of sugar."
________________________________________
5. Bonus User Story: The "Hidden Gem"
As a Health Conscious Consumer,
I want to know which specific ingredients are driving the high protein content in the "good" products,
So that I can replicate this in our new recipe.
•	Acceptance Criteria:
o	Analyze the ingredients_text column for products in your "High Protein" cluster.
o	Extract and list the Top 3 most common protein sources (e.g., "Whey", "Peanuts", "Soy").
________________________________________
6. The "Candidate's Choice" Challenge
As a Creative Analyst,
I want to add one additional feature or analysis to this project that I believe provides massive value,
So that I can show off my business acumen.
•	Instructions:
o	Add one more chart, filter, or metric that wasn't asked for.
o	Explain why you added it.
o	There is no wrong answer, but you must justify your choice.
________________________________________
7. Submission Guidelines
Please edit this README.md file in your forked repository to include the following three sections at the top:
A. The Executive Summary
•	A 3-5 sentence summary of your findings.
B. Project Links
•	Link to Notebook: (e.g., Google Colab, etc.). Ensure sharing permissions are set to "Anyone with the link can view".
•	Link to Dashboard: (e.g., Tableau Public / Power BI Web, etc.).
•	Link to Presentation: A link to a short slide deck (PDF, PPT) AND (Optional) a 2-minute video walkthrough (YouTube) explaining your results.
C. Technical Explanation
•	Briefly explain how you handled the "Data Cleaning".
•	Explain your "Candidate's Choice" addition.
Important Note on Code Submission:
•	Upload your .ipynb notebook file to the repo.
•	Crucial: Also upload an HTML or PDF export of your notebook so we can see your charts even if GitHub fails to render the notebook code.
•	Once you are ready, please fill out the Official Submission Form Here with your links
________________________________________
🛑 CRITICAL: Pre-Submission Checklist
Before you submit your form, you MUST complete this checklist.
⚠️ WARNING: If you miss any of these items, your submission will be flagged as "Incomplete" and you will NOT be invited to an interview.
We do not accept "permission error" excuses. Test your links in Incognito Mode.
1. Repository & Code Checks
•	  My GitHub Repo is Public. (Open the link in a Private/Incognito window to verify).
•	  I have uploaded the .ipynb notebook file.
•	  I have ALSO uploaded an HTML or PDF export of the notebook.
•	  I have NOT uploaded the massive raw dataset. (Use .gitignore or just don't commit the CSV).
•	  My code uses Relative Paths.
2. Deliverable Checks
•	  My Dashboard link is publicly accessible. (No login required).
•	  My Presentation link is publicly accessible. (Permissions set to "Anyone with the link can view").
•	  I have updated this README.md file with my Executive Summary and technical notes.
3. Completeness
•	  I have completed User Stories 1-4.
•	  I have completed the "Candidate's Choice" challenge and explained it in the README.
✅ Only when you have checked every box above, proceed to the submission form.
