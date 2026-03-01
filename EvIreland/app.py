import streamlit as st
import json
import os

def load_clean_json(filename):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.sidebar.error(f"File Not Found: {filename}")
        st.sidebar.info(f"Looking in: {full_path}")
        return None

st.set_page_config(
    page_title="Ireland EV Market Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }

    [data-testid="stMetric"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0px !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 1rem !important;
        color: #666 !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    /* Key Finding Box */
    .finding-box {
        background-color: rgba(44, 160, 44, 0.08); /* Transparent Green */
        border-left: 5px solid #2CA02C; /* Solid Green Accent */
        border-radius: 4px;
        padding: 1.2rem;
        margin-top: 15px;
        font-size: 0.95rem;
        line-height: 1.6;
        color: #1A1A1A;
    }
    
    .finding-header {
        display: block;
        font-weight: 800;
        color: #228022;
        margin-bottom: 8px;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
    }

    hr { margin-top: 2rem; margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)


st.title("Is the January 2026 'Electric Vehicle (EV) Crossover' a permanent structural shift in Irish consumer behaviour, or a temporary market spike?")
st.markdown("The big switch from gas cars to electric cars.")
st.markdown("---")

# SECTION 1: IRISH EV CAR MARKET
st.markdown('<h2 style="color: #2CA02C;">1. Ireland Car Market Share 2016-2026Jan: The Shift to Electric</h2>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.3rem; margin-top: 0px; padding-top: 0px; color: #666;">Points represent 6-month totals | Source: CSO TEM12</p>', unsafe_allow_html=True)
col_chart, col_metrics = st.columns([3, 1])

with col_chart:
    data1 = load_clean_json('Irish_EV_car_market.json')
    if data1:
        st.vega_lite_chart(data1, use_container_width=True)
    st.markdown("""
        <div class="finding-box">
            <strong>The Merging Market:</strong> Over the years, the wide gap between different vehicle types has finally narrowed down. This "merging" of lines shows the market maturing as Electric and Hybrid options catch up to and cross over traditional Petrol and Diesel dominance.
        </div>
        """, unsafe_allow_html=True)

with col_metrics:
    st.subheader("Market Metrics")

    st.metric(
        label="EV Market Share",
        value="22.0%",
        delta="+7%",
        help="EV Share increased from 15% (Jan '25) to 22% (Jan '26)."
    )
    st.metric(
        label="EV Market Units",
        value="5,439 Units",
        delta="+61% ",
        help="Volume increased from 3,386 units (Jan '25)  to 5,439 units (Jan '26)."
    )
    st.metric(
        label="Combustion Market share",
        value="31.0%",
        delta="-12% ",
        delta_color="normal",
        help="Combined Petrol & Diesel share fell from 43% (Jan '25) to 31% (Jan '26)."
    )


st.markdown("---")

# SECTION 2: GRANT VS EV REGISTRATION
st.header("2. Ireland: EV Grant vs. EV Units Sold 2016-2025")
st.markdown('<p style="font-size: 1.3rem; margin-top: 0px; padding-top: 0px; color: #666;">H1: Jan-Jun | H2: Jul-Dec | Grant dropped July 2023 | Source: CSO TEM12</p>', unsafe_allow_html=True)# Using a [1, 5, 1] ratio to force the middle column to center the chart
_, col_mid2, _ = st.columns([1, 5, 1])

with col_mid2:
    data2 = load_clean_json('GrantVsEv.json')
    if data2:
        st.vega_lite_chart(data2, use_container_width=True)
    st.markdown("""
        <div class="finding-box">
            <strong>Breaking Free from Subsidies:</strong> This trend proves the market is no longer controlled by government handouts. After a brief period of adjustment following the grant cut, sales began to rise sharply again.
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# SECTION 3: TOP 10 EV SHARE
st.header("3. Ireland: Top 10 EV Market Share (2024–2026Jan)")
st.markdown('<p style="font-size: 1.3rem; margin-top: 0px; padding-top: 0px; color: #666;">Market Share of Top 10 EV Models with Price (€) Classification | Source: CSO TEM28 </p>', unsafe_allow_html=True)# Centering the final section as well
_, col_mid3, _ = st.columns([1, 6, 1])

with col_mid3:
    data3 = load_clean_json('Top10EvShare.json')
    if data3:
        st.vega_lite_chart(data3, use_container_width=True)
    st.markdown("""
        <div class="finding-box">
            <strong>The Value Shift:</strong> There is a clear "colour migration" in these charts. 
            As car prices drop into the <strong>Value and Budget ranges</strong>, these models are 
            aggressively taking over the market share once held by premium brands.
        </div>
        """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.caption("Data provided by Central Statistics Office (CSO) Ireland. All charts interactive.")


