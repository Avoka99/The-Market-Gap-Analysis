import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from collections import Counter

# Set page configuration with a premium theme
st.set_page_config(
    page_title="Helix CPG Partners | Market Gap Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium styling (glassmorphism look, custom fonts, rounded cards)
st.markdown(
    """
    <style>
    /* Import modern typography */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Title banner styling */
    .title-container {
        background: linear-gradient(135deg, #1f4068 0%, #162447 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .title-container h1 {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .title-container p {
        font-size: 1.2rem;
        opacity: 0.85;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }
    
    /* Styled KPI Cards */
    .metric-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #1f4068;
        margin-bottom: 1.5rem;
    }
    .metric-card h3 {
        color: #555;
        font-size: 1rem;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-card p {
        color: #1f4068;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0.5rem 0 0 0;
    }
    
    /* Insight Card */
    .insight-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 12px;
        padding: 1.8rem;
        border-left: 5px solid #f39c12;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .insight-card h3 {
        color: #e67e22;
        margin-top: 0;
        font-size: 1.2rem;
        font-weight: 800;
    }
    .insight-card p {
        font-size: 1.15rem;
        line-height: 1.6;
        color: #2c3e50;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------
# DATA WRANGLING & CLEANING RULES (Self-contained)
# ----------------------------------------------------

# Tags setup for categorization
sweet_snacks_tags = {
    "sweet-snacks", "biscuits-and-cakes", "biscuits", "confectioneries", 
    "candies", "cocoa-and-its-products", "chocolates", "chocolate-bars", 
    "cookies", "cakes", "sweet-spreads", "waffles", "pastries", "donuts"
}

savory_snacks_tags = {
    "salty-snacks", "chips-and-fries", "crisps", "nuts-and-their-products", 
    "seeds", "popcorn", "pretzels", "appetizers", "crackers", "salted-snack"
}

dairy_yogurts_tags = {
    "dairies", "yogurts", "cheeses", "dairy-desserts", 
    "fermented-milk-products", "fermented-dairy-desserts", "milks", "curds"
}

breakfast_cereals_tags = {
    "breakfast-cereals", "breakfasts", "cereals-and-their-products", 
    "muesli", "granola", "cereal-bars", "oatmeal", "porridges"
}

beverages_tags = {
    "beverages", "plant-based-beverages", "sodas", "fruit-juices", 
    "sweetened-beverages", "unsweetened-beverages", "teas", "coffees", "waters"
}

def clean_tags(tags_str):
    if not isinstance(tags_str, str):
        return []
    raw_tags = [t.strip().lower() for t in tags_str.split(",")]
    cleaned = []
    for t in raw_tags:
        if ":" in t:
            cleaned.append(t.split(":", 1)[1])
        else:
            cleaned.append(t)
    return cleaned

def categorize_product(tags_str):
    tags = clean_tags(tags_str)
    if not tags:
        return "Other / Meals"
    if any(t in sweet_snacks_tags for t in tags):
        return "Sweet Snacks"
    if any(t in savory_snacks_tags for t in tags):
        return "Savory Snacks"
    if any(t in breakfast_cereals_tags for t in tags):
        return "Cereals & Breakfast"
    if any(t in dairy_yogurts_tags for t in tags):
        return "Dairy & Yogurts"
    if any(t in beverages_tags for t in tags):
        return "Beverages"
    return "Other / Meals"

@st.cache_data
def load_data():
    dataset_path = "market_gap_dataset.csv"
    if not os.path.exists(dataset_path):
        return None

    df = pd.read_csv(dataset_path)

    if "primary_category" not in df.columns:
        if "categories_tags" not in df.columns:
            raise KeyError("The dataset must include a 'categories_tags' column to derive primary_category.")
        df["primary_category"] = df["categories_tags"].apply(categorize_product)
    elif "categories_tags" in df.columns:
        missing_categories = df["primary_category"].isna() | (df["primary_category"].astype(str).str.strip() == "")
        if missing_categories.any():
            df.loc[missing_categories, "primary_category"] = df.loc[missing_categories, "categories_tags"].apply(categorize_product)

    return df

df = load_data()

# ----------------------------------------------------
# APP HEADER
# ----------------------------------------------------
st.markdown(
    """
    <div class="title-container">
        <h1>🔍 "Sugar Trap" Market Gap Analysis</h1>
        <p>Strategic food and beverage consultancy dashboard identifying the "Blue Ocean" in the snack aisle.</p>
    </div>
    """,
    unsafe_allow_html=True
)

if df is None:
    st.error("❌ Data file not found! Please make sure `market_gap_dataset.csv` is present in the project folder.")
    st.info("💡 Run the Jupyter Notebook or data ingestion script to create the single canonical dataset first.")
    st.stop()

# ----------------------------------------------------
# SIDEBAR FILTERS
# ----------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/data-configuration.png", width=60)
st.sidebar.header("Dashboard Configuration")

st.sidebar.markdown("---")
st.sidebar.subheader("1. Category Filter")

categories = sorted(df["primary_category"].unique().tolist())
# Put "Other / Meals" at the end of the list
if "Other / Meals" in categories:
    categories.remove("Other / Meals")
    categories.append("Other / Meals")

selected_categories = st.sidebar.multiselect(
    "Select Snack Categories to plot:",
    options=categories,
    default=[c for c in categories if c != "Other / Meals"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("2. Define the Target Quadrant")
st.sidebar.info("Adjust the sliders to define what R&D considers 'High Protein' and 'Low Sugar'.")

min_protein = st.sidebar.slider(
    "Minimum Protein (g / 100g):",
    min_value=0.0,
    max_value=30.0,
    value=10.0,
    step=1.0
)

max_sugar = st.sidebar.slider(
    "Maximum Sugar (g / 100g):",
    min_value=0.0,
    max_value=40.0,
    value=10.0,
    step=1.0
)

# ----------------------------------------------------
# DATA CALCULATIONS
# ----------------------------------------------------
# General filtered df based on sidebar categories
df_filtered = df[df["primary_category"].isin(selected_categories)]

# Empty quadrant filter (snack lines only)
empty_quadrant_df = df[
    (df["proteins_100g"] >= min_protein) & 
    (df["sugars_100g"] <= max_sugar) &
    (df["primary_category"] != "Other / Meals")
]

# ----------------------------------------------------
# MAIN DASHBOARD METRICS
# ----------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <h3>Total Analyzed Products</h3>
            <p>{len(df):,}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card" style="border-left: 5px solid #2ecc71;">
            <h3>Categories Filtered</h3>
            <p>{len(selected_categories)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card" style="border-left: 5px solid #f39c12;">
            <h3>Target Quadrant Products</h3>
            <p>{len(empty_quadrant_df):,}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    total_snacks_in_db = len(df[df["primary_category"] != "Other / Meals"])
    pct_gap = (len(empty_quadrant_df) / max(1, total_snacks_in_db)) * 100
    st.markdown(
        f"""
        <div class="metric-card" style="border-left: 5px solid #e74c3c;">
            <h3>Market Gap density</h3>
            <p>{pct_gap:.2f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------------------------------
# STORY 4: R&D RECOMMENDATION CARD
# ----------------------------------------------------
# Calculate dynamic values for recommendations based on empty quadrant
target_cat = "Cereals & Breakfast"
avg_prot = 15.0
avg_sug = 4.2

if not empty_quadrant_df.empty:
    counts = empty_quadrant_df["primary_category"].value_counts()
    if not counts.empty:
        target_cat = counts.index[0]
        target_cat_df = empty_quadrant_df[empty_quadrant_df["primary_category"] == target_cat]
        avg_prot = target_cat_df["proteins_100g"].mean()
        avg_sug = target_cat_df["sugars_100g"].mean()

st.markdown(
    f"""
    <div class="insight-card">
        <h3>💡 R&D Product Development Recommendation</h3>
        <p><strong>Based on the data, the biggest market opportunity is in {target_cat}, specifically targeting products with {avg_prot:.1f}g of protein and less than {avg_sug:.1f}g of sugar.</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------
# STORY 3: NUTRIENT MATRIX SCATTER PLOT
# ----------------------------------------------------
st.subheader("📊 The Nutrient Matrix (Sugar vs. Protein)")
st.markdown("Use this scatter plot to explore how product categories cluster. The shaded quadrant highlights the **Blue Ocean** segment.")

colors_map = {
    "Sweet Snacks": "#E74C3C",
    "Savory Snacks": "#E67E22",
    "Cereals & Breakfast": "#F1C40F",
    "Dairy & Yogurts": "#3498DB",
    "Beverages": "#2ECC71",
    "Other / Meals": "#95A5A6"
}

# Sample for smooth Plotly rendering (max 20k rows)
plot_df = df_filtered.sample(min(20000, len(df_filtered)), random_state=42)

fig = px.scatter(
    plot_df, 
    x="sugars_100g", 
    y="proteins_100g", 
    color="primary_category",
    hover_data=["product_name", "brands"],
    labels={"sugars_100g": "Sugar (g / 100g)", "proteins_100g": "Protein (g / 100g)", "primary_category": "Category"},
    color_discrete_map=colors_map,
    opacity=0.6,
    height=600
)

# Highlight Empty Quadrant based on user values
fig.add_shape(
    type="rect",
    x0=0, y0=min_protein, x1=max_sugar, y1=100,
    line=dict(color="navy", width=2, dash="dash"),
    fillcolor="rgba(173, 216, 230, 0.25)",
    name="Target Quadrant"
)

# Update layout
fig.update_layout(
    xaxis=dict(title="Sugar (g per 100g)", range=[-2, 102]),
    yaxis=dict(title="Protein (g per 100g)", range=[-2, 102]),
    margin=dict(l=40, r=40, t=20, b=40),
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.01)
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------
# STORY 5 & 6: LOWER DASHBOARD SECTION (TABS)
# ----------------------------------------------------
tab1, tab2 = st.tabs(["🌱 Story 5: Hidden Gems (Protein Sources)", "🛡️ Story 6: Candidate's Choice (Nutritional Processing Quality)"])

with tab1:
    st.subheader("Top Protein Sources in Healthy Snacks")
    st.markdown("We mine the ingredient text of products in the target quadrant to identify what drives protein content.")
    
    eq_ingredients = empty_quadrant_df.dropna(subset=["ingredients_text"])
    
    if eq_ingredients.empty:
        st.warning("No products found in the target quadrant with ingredients lists. Adjust the sliders to expand the quadrant.")
    else:
        protein_sources_kw = {
            "Whey (Dairy)": ["whey", "lactosérum", "milk protein", "protéine de lait", "casein", "caséine", "poudre de lait"],
            "Soy": ["soy", "soja", "soya"],
            "Peanuts": ["peanut", "cacahuète", "arachide"],
            "Pea": ["pea ", "pois", "pea protein", "protéine de pois"],
            "Almond": ["almond", "amande"],
            "Egg": ["egg", "oeuf", "albumen"],
            "Oats": ["oat", "avoine", "flocons d'avoine"],
            "Seeds": ["seed", "graine", "pumpkin", "sunflower", "tournesol", "courge", "chia", "hemp", "chanvre"],
            "Lentils / Chickpeas": ["lentil", "lentille", "chickpea", "pois chiche", "faba", "fève"]
        }

        source_counts = Counter()
        for text in eq_ingredients["ingredients_text"]:
            text_lower = text.lower()
            for source_name, kw_list in protein_sources_kw.items():
                if any(kw in text_lower for kw in kw_list):
                    source_counts[source_name] += 1
        
        # Prepare data for plotting
        source_df = pd.DataFrame(source_counts.most_common(), columns=["Protein Source", "Product Count"])
        source_df["Percentage (%)"] = (source_df["Product Count"] / len(eq_ingredients)) * 100
        
        col_chart, col_table = st.columns([2, 1])
        
        with col_chart:
            fig_bar = px.bar(
                source_df,
                x="Product Count",
                y="Protein Source",
                orientation='h',
                title="Frequency of Protein Sources in Target Segment",
                labels={"Product Count": "Number of Products", "Protein Source": "Ingredient"},
                color="Product Count",
                color_continuous_scale="Viridis",
                text="Percentage (%)"
            )
            fig_bar.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col_table:
            st.dataframe(
                source_df.style.format({"Percentage (%)": "{:.1f}%"}),
                use_container_width=True,
                hide_index=True
            )

with tab2:
    st.subheader("Food Processing Levels (NOVA) & Nutri-Score Distribution")
    st.markdown("Is the target quadrant filled with ultra-processed products (NOVA 4) using synthetic additives, or clean-label alternatives?")
    
    eq_ns = empty_quadrant_df.dropna(subset=["nutriscore_grade"])
    eq_nova = empty_quadrant_df.dropna(subset=["nova_group"])
    
    col_ns, col_nova = st.columns(2)
    
    with col_ns:
        if eq_ns.empty:
            st.warning("No products with Nutri-Score grades found in the target quadrant.")
        else:
            ns_dist = eq_ns["nutriscore_grade"].str.upper().value_counts().sort_index()
            ns_df = pd.DataFrame({"Grade": ns_dist.index, "Count": ns_dist.values})
            
            fig_ns = px.bar(
                ns_df,
                x="Grade",
                y="Count",
                title="Nutri-Score Grades in Target Quadrant",
                color="Grade",
                color_discrete_map={
                    "A": "#008245",
                    "B": "#62AC34",
                    "C": "#FECA07",
                    "D": "#EA6205",
                    "E": "#D30018"
                }
            )
            st.plotly_chart(fig_ns, use_container_width=True)
            
    with col_nova:
        if eq_nova.empty:
            st.warning("No products with NOVA processing scores found in the target quadrant.")
        else:
            # Map NOVA groups to text descriptions
            nova_desc = {
                1.0: "1: Unprocessed / Minimally Processed",
                2.0: "2: Processed Culinary Ingredients",
                3.0: "3: Processed Foods",
                4.0: "4: Ultra-Processed Foods"
            }
            nova_dist = eq_nova["nova_group"].value_counts().sort_index()
            nova_df = pd.DataFrame({
                "Group": [nova_desc.get(k, str(k)) for k in nova_dist.index],
                "Count": nova_dist.values
            })
            
            fig_nova = px.bar(
                nova_df,
                x="Group",
                y="Count",
                title="NOVA Processing Groups in Target Quadrant",
                color="Group",
                color_discrete_sequence=["#00A86B", "#FFBF00", "#FF7F50", "#DE3163"]
            )
            st.plotly_chart(fig_nova, use_container_width=True)
            
    # Business interpretation markdown
    if not eq_nova.empty:
        total_nova = len(eq_nova)
        up_count = len(eq_nova[eq_nova["nova_group"] == 4.0])
        up_ratio = (up_count / total_nova) * 100
        
        st.markdown(
            f"""
            > **💡 Strategic Takeaway for Helix CPG Partners**:
            > - **Ultra-Processed Dominance**: **{up_ratio:.1f}%** of products in this high-protein, low-sugar segment fall under **NOVA Group 4 (Ultra-Processed)**. These products achieve their nutritional profiles by using protein isolates, texturizers, and chemical sweetening agents (e.g. sucralose, acesulfame K).
            > - **The True Blue Ocean**: The remaining **{100 - up_ratio:.1f}%** of products represent **Clean-Label (NOVA 1-3)** options. A manufacturer that can formulate a clean-label, minimally processed product with high protein and low sugar can capture a highly lucrative premium market gap.
            """
        )
