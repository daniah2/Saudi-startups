import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium
import json
from chatbot import respond

df = pd.read_csv("cleaned_dataset.csv", encoding='utf-8') 

# Page configuration
st.set_page_config(
    page_title="MARQAB Startup Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Purple color palette
purple_palette = [
    "#9B7EBD", 
    "#D4BEE4",  
    "#674188",  
    "#A888B5",  
    "#BB9CC0",  
    "#C8ACD6", 
    "#D4BEE4", 
    "#E6CCE6",  
    "#F3E8FF",
]

# Custom CSS with purple palette
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling with purple gradient background */
    .stApp {
        background: linear-gradient(135deg, #F3E8FF 0%, #E6CCE6 50%, #D4BEE4 100%);
        font-family: 'Inter', sans-serif;
    }

    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1200px;
    }
    
    /* Header styling with purple gradient */
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #674188 0%, #9B7EBD 100%);
        color: white !important;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(103, 65, 136, 0.3);
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Logo container with purple border */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(103, 65, 136, 0.15);
        border: 2px solid #D4BEE4;
    }
    
    /* Metric cards with purple accents */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(103, 65, 136, 0.15);
        border-left: 5px solid #9B7EBD;
        transition: all 0.3s ease;
        border: 1px solid #D4BEE4;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(103, 65, 136, 0.25);
        border-left-color: #674188;
    }
    
    .metric-title {
        color: #674188 !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin: 0 !important;
    }
    
    .metric-value {
        color: #2D1B39 !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin: 0.5rem 0 0 0 !important;
    }
    
    .metric-subtitle {
        color: #9B7EBD !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin: 0.5rem 0 !important;
    }
    
    .metric-description {
        color: #6B4B73 !important;
        font-size: 1rem !important;
        margin: 0 !important;
    }
    
    /* Insight boxes with purple theme */
    .insight-box {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(103, 65, 136, 0.15);
        border: 1px solid #D4BEE4;
        transition: all 0.3s ease;
    }
    
    .insight-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 30px rgba(103, 65, 136, 0.25);
        border-color: #BB9CC0;
    }
    
    .insight-title {
        color: #674188 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    .insight-content {
        color: #4A2C58 !important;
        line-height: 1.6 !important;
        font-size: 1rem !important;
    }
    .st-cz {
        background-color: white;
     }
     
    .st-ez
    {
        border-bottom-color: rgb(255, 255, 255);
    }

    .st-ey {
        border-top-color: rgba(103, 65, 136, 0.25);
    }

    .st-ex {
        border-right-color: rgba(103, 65, 136, 0.25);
    }

    .st-ew {
        border-left-color: rgba(103, 65, 136, 0.25);
    }

    .st-bd {
        min-height: 2.5rem;
    }

    .st-bc {
        max-height: 168px;
    }

    .st-bb {
        background-color: rgb(255, 255, 255);
    }

    .st-b6 {
        color: rgb(250, 250, 250);
    }
    
    .st-b5 {
        transition-timing-function: cubic-bezier(0.2, 0.8, 0.4, 1);
    }
     
    element.style {
        font-family: "Source Sans", sans-serif;
        font-size: 12px;
        fill: rgb(0, 0, 0);
        fill-opacity: 1;
        font-weight: 400;
        font-style: normal;
        font-variant: normal;
        white-space: pre;
    }
     
    .st-emotion-cache-efbu8t {
        font-size: 2.25rem;
        color: #674188 !important;
        padding-bottom: 0.25rem;
    }

    /* Tabs styling with purple gradient */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(135deg, #F3E8FF 0%, #E6CCE6 100%);
        padding: 8px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(103, 65, 136, 0.15);
        border: 2px solid #D4BEE4;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border-radius: 12px;
        padding: 0 24px;
        color: #674188 !important;
        font-weight: 600 !important;
        border: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #9B7EBD 0%, #674188 100%) !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(103, 65, 136, 0.3);
    }
    
    /* Sidebar styling with purple theme */
    .css-1d391kg, .stSidebar > div {
        background: linear-gradient(180deg, #F3E8FF 0%, #E6CCE6 100%) !important;
        border-right: 3px solid #C8ACD6;
    }
    
    .sidebar-title {
        color: #674188 !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* Form elements with purple styling */
    .stSelectbox label, .stMultiSelect label {
        color: #674188 !important;
        font-weight: 600 !important;
    }
    
    .stSelectbox > div > div, .stMultiSelect > div > div {
        background-color: white !important;
        border: 2px solid #D4BEE4 !important;
        border-radius: 12px !important;
        color: #2D1B39 !important;
    }
    
    .stSelectbox > div > div:focus-within, .stMultiSelect > div > div:focus-within {
        border-color: #9B7EBD !important;
        box-shadow: 0 0 0 3px rgba(155, 126, 189, 0.1) !important;
    }
    
    /* Section headers with purple accent */
    .section-header {
        color: #674188 !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem !important;
        border-bottom: 3px solid #9B7EBD !important;
    }
    
    /* Data table with purple borders */
    .stDataFrame {
        border: 2px solid #D4BEE4 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        background: white !important;
    }
    
    /* Metrics with purple theme */
    .stMetric {
        background: white !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border: 1px solid #D4BEE4 !important;
        box-shadow: 0 4px 15px rgba(103, 65, 136, 0.1) !important;
    }
    
    .stMetric label {
        color: #674188 !important;
        font-weight: 600 !important;
    }
    
    .stMetric [data-testid="metric-value"] {
        color: #2D1B39 !important;
        font-weight: 700 !important;
    }
    
    /* Download button with purple gradient */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #9B7EBD 0%, #674188 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(103, 65, 136, 0.3) !important;
    }
    
    /* Chart containers with purple borders */
    .js-plotly-plot {
        background-color: white !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(103, 65, 136, 0.15) !important;
        border: 2px solid #D4BEE4 !important;
    }
    
    /* Footer with purple theme */
    .footer-container {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #F3E8FF 0%, #E6CCE6 100%);
        border-radius: 16px;
        margin-top: 3rem;
        box-shadow: 0 8px 25px rgba(103, 65, 136, 0.15);
        border: 2px solid #C8ACD6;
    }
    
    .footer-title {
        color: #674188 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    .footer-text {
        color: #6B4B73 !important;
        margin: 0.5rem 0 !important;
    }
    
    /* Additional purple styling for all text elements */
    h1, h2, h3, h4, h5, h6 {
        color: #674188 !important;
    }
    
    p {
        color: #4A2C58 !important;
    }
    
    /* Multiselect tags with purple theme */
    .stMultiSelect span[data-baseweb="tag"] {
        background-color: #BB9CC0 !important;
        color: white !important;
    }
    
    /* Radio buttons and checkboxes */
    .stRadio > div, .stCheckbox > div {
        color: #674188 !important;
    }
    
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Helper function to convert Funding_Avg to numeric
# ---------------------------
def parse_funding(value):
    """
    تحويل قيم Funding_Avg اللي فيها M أو B إلى أرقام حقيقية
    """
    if pd.isna(value):
        return 0
    if isinstance(value, (int, float)):
        return value
    value = str(value).replace(',', '').strip()
    if value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('B'):
        return float(value[:-1]) * 1_000_000_000
    else:
        try:
            return float(value)
        except:
            return 0


# ---------------------------
# Header with logo
# ---------------------------
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
try:
    logo = Image.open('MARQAB_logo.png')
    st.image(logo, width=180)
except:
    st.markdown('<div style="text-align: center; color: #674188; font-size: 2rem; font-weight: 700;"> مرقب MARQAB</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">Startup Ecosystem Distribution Dashboard</h1>', unsafe_allow_html=True)

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.markdown('<p class="sidebar-title">Dashboard Controls</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")

selected_industries = st.sidebar.multiselect(
    "Select Industries to Display",
    options=df['Industry'].unique(),
    default=df['Industry'].unique(),
    help="Choose which industries to include in your analysis"
)

chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Pie Chart", "Bar Chart", "Donut Chart", "Horizontal Bar Chart"],
    help="Choose how to visualize the data"
)

color_scheme = st.sidebar.selectbox(
    "Color Scheme",
    ["Purple Theme", "Light Purple", "Deep Purple", "Purple Gradient"],
    help="Select purple color palette for charts"
)

# ---------------------------
# Filtered DataFrame
# ---------------------------
filtered_df = df[df['Industry'].isin(selected_industries)].copy()

# Ensure Funding_min is numeric
filtered_df['Funding_min'] = pd.to_numeric(filtered_df['Funding_min'], errors='coerce')

# Funding_Avg stays as string (e.g., '2.5M', '1B') for display, 
# but we can convert to numeric for calculations:
filtered_df['Funding_Avg_Num'] = filtered_df['Funding_Avg'].apply(parse_funding)

# ---------------------------
# Purple color schemes for charts
# ---------------------------
purple_color_schemes = {
    "Purple Theme": purple_palette,
    "Light Purple": ["#F3E8FF", "#E6CCE6", "#D4BEE4", "#C8ACD6", "#BB9CC0", "#A888B5", "#9B7EBD", "#674188"],
    "Deep Purple": ["#674188", "#7A4B95", "#8D55A2", "#A063AF", "#B371BC", "#C67FC9", "#D98DD6", "#EC9BE3"],
    "Purple Gradient": ["#F3E8FF", "#D4BEE4", "#BB9CC0", "#9B7EBD", "#674188"]
}

# Main dashboard
tab1, tab2, tab3, tab4, tab5 , tab6 = st.tabs(["Overview", "Detailed Analysis", "Key Insights", "Map", "Data Table" , "Chat with Marqab"])

with tab1:
    col1, col2 = st.columns([2.5, 1.5])
    
    with col1:
        st.markdown('<p class="section-header">Distribution of Startup Industries</p>', unsafe_allow_html=True)
        
        if chart_type in ["Pie Chart", "Donut Chart"]:
            hole = 0.4 if chart_type=="Donut Chart" else 0
            fig = px.pie(
                filtered_df, 
                names='Industry',
                values='Funding_Avg_Num',  # استخدم القيمة الرقمية للرسم
                color_discrete_sequence=purple_color_schemes[color_scheme],
                hole=hole
            )
            fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=11, textfont_color='#000000')
        
        elif chart_type == "Bar Chart":
            fig = px.bar(
                filtered_df.sort_values('Funding_Avg_Num', ascending=False),
                x='Industry',
                y='Funding_Avg_Num',  # القيمة الرقمية
                color='Industry',
                color_discrete_sequence=purple_color_schemes[color_scheme],
                text='Funding_Avg'  # عرض النص بالحروف (M/B)
            )
            fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_color="#000000")
            fig.update_xaxes(tickangle=45, tickfont_color='#674188')
            fig.update_yaxes(tickfont_color='#674188')
        
        else:  # Horizontal Bar Chart
            fig = px.bar(
                filtered_df.sort_values('Funding_Avg_Num', ascending=True),
                x='Funding_Avg_Num',  # القيمة الرقمية
                y='Industry',
                color='Industry',
                color_discrete_sequence=purple_color_schemes[color_scheme],
                orientation='h',
                text='Funding_Avg'  # عرض النص بالحروف
            )
            fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_color='#674188')
            fig.update_xaxes(tickfont_color='#674188')
            fig.update_yaxes(tickfont_color='#674188')
        
        fig.update_layout(
            height=500,
            font=dict(size=12, color='#674188'),
            paper_bgcolor='white',
            plot_bgcolor='#674188',
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            title_font_color='#674188'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<p class="section-header">Key Metrics</p>', unsafe_allow_html=True)
        
        total_startups = filtered_df.shape[0]
        top_industry = filtered_df.groupby('Industry')['Funding_Avg_Num'].sum().idxmax()
        top_funding_num = filtered_df.groupby('Industry')['Funding_Avg_Num'].sum().max()
        # أفضل طريقة لعرض Funding_Avg بالحروف:
        top_funding_str = filtered_df.groupby('Industry')['Funding_Avg'].first()[top_industry]
        
        st.markdown(f"""
        <div class="metric-card">
            <p class="metric-title">Total Startups</p>
            <p class="metric-value">{total_startups}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-card">
            <p class="metric-title">Leading Industry</p>
            <p class="metric-subtitle">{top_industry}</p>
            <p class="metric-description">{top_funding_str} USD funding</p>
        </div>
        """, unsafe_allow_html=True)


with tab2:
    st.markdown('<p class="section-header">Detailed Industry Analysis</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Top 5 industries by numeric funding
    with col1:
        top5_num = filtered_df.groupby('Industry')['Funding_Avg_Num'].sum().nlargest(5).reset_index()
        # للحصول على النسخة بالحروف للعرض على الرسم
        top5_str = filtered_df.groupby('Industry')['Funding_Avg'].first().reindex(top5_num['Industry']).reset_index()
        
        fig_top = px.bar(
            top5_num, 
            x='Funding_Avg_Num', 
            y='Industry',
            orientation='h',
            title="Top 5 Industries by Total Funding",
            color='Industry',
            color_discrete_sequence=purple_palette,
            text=top5_str['Funding_Avg']  # عرض بالحروف
        )

        # تعديل نصوص الأعمدة لتكون بلون وحجم ونوع الخط المناسب
        fig_top.update_traces(
            texttemplate='%{text}', 
            textposition='outside',
            textfont=dict(
                color='#674188',  # لون النص
                size=12,          # حجم النص
                family='Inter, sans-serif'  # نوع الخط
            )
        )

        fig_top.update_layout(
            height=400,
            paper_bgcolor="#BCAACD",
            plot_bgcolor='#BCAACD',
            font=dict(color='#674188', size=11, family='Inter, sans-serif'),
            title_font_size=14,
            title_font_color='#674188',
            margin=dict(l=20, r=20, t=40, b=20)
        )

        st.plotly_chart(fig_top, use_container_width=True)

    
    # Growth potential estimation
    with col2:
        growth_data_num = top5_num.copy()
        growth_data_num['Potential'] = growth_data_num['Funding_Avg_Num'] * 1.3
        # نسخة بالحروف للعرض على الرسم
        growth_data_str = top5_str.copy()
        growth_data_str['Potential'] = growth_data_str['Funding_Avg'] + " (est.)"
        
        fig_growth = go.Figure(data=[
            go.Bar(
                name='Current Funding', 
                x=growth_data_num['Industry'], 
                y=growth_data_num['Funding_Avg_Num'], 
                marker_color='#9B7EBD',
                text=growth_data_str['Funding_Avg'],  # عرض بالحروف
                textposition='outside',
                textfont=dict(
                    color='#674188',  # لون الخط للنصوص فوق الأعمدة
                    size=15,          # حجم الخط
                    family='Inter, sans-serif'  # نوع الخط
                )
            ),
            go.Bar(
                name='Potential Funding', 
                x=growth_data_num['Industry'], 
                y=growth_data_num['Potential'], 
                marker_color='#D4BEE4',
                text=growth_data_str['Potential'],  # عرض بالحروف
                textposition='outside',
                textfont=dict(
                    color='#674188',
                    size=15,
                    family='Inter, sans-serif'
                )
            )
        ])

        
        fig_growth.update_layout(
            barmode='group',
            title="Current vs Growth Potential",
            height=400,
            xaxis_tickangle=45,
            paper_bgcolor="#DFC8F3",
            plot_bgcolor='#DFC8F3',
            font=dict(color='#674188', size=11),
            title_font_size=14,
            title_font_color='#674188',
            xaxis=dict(
                gridcolor='rgba(103,65,136,0.1)',   # لون خطوط الشبكة للـ x-axis
                tickfont_color='#674188',            # لون النصوص على المحور
                title_font_color='#674188'
            ),
            yaxis=dict(
                gridcolor='rgba(103,65,136,0.1)',   # لون خطوط الشبكة للـ y-axis
                tickfont_color='#674188',
                title_font_color='#674188'
            )
        )

        st.plotly_chart(fig_growth, use_container_width=True)


with tab3:
    st.markdown('<p class="section-header">Key Insights & Strategic Recommendations</p>', unsafe_allow_html=True)
    
    # -------------------
    # Insights النصية
    # -------------------
    with st.container():
        col1, col2 = st.columns(2)

        box_style = """
        border:1px solid #D4BEE4; 
        border-radius:12px; 
        padding:20px; 
        margin:10px 0; 
        background:#F9F5FF;
        height:180px; 
        display:flex; 
        flex-direction:column; 
        justify-content:center;
        """

        with col1:
            st.markdown(f"""
            <div style="{box_style}">
              <h4 style="margin:0 0 8px 0; color:#674188">Regional Investment Gap</h4>
              <p style="margin:0">Riyadh dominates funding (75.6%), revealing major regional imbalances</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="{box_style}">
              <h4 style="margin:0 0 8px 0; color:#674188">Funding Concentration</h4>
              <p style="margin:0">Top 6 companies capture >70% of total funding</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style="{box_style}">
              <h4 style="margin:0 0 8px 0; color:#674188">Vision Alignment Strength</h4>
              <p style="margin:0">94.8% of startups align with Vision 2030 goals</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div style="{box_style}">
              <h4 style="margin:0 0 8px 0; color:#674188">Sector Over-Concentration</h4>
              <p style="margin:0">60% of startups in just 3 sectors (SaaS, AI, Marketplace)</p>
            </div>
            """, unsafe_allow_html=True)


    # -------------------
    # Regional Insights
    # -------------------
    with st.container():
        st.markdown('<p class="section-header">Rate Percent by Region</p>', unsafe_allow_html=True)

        # حساب المتوسط + مجموع التمويل
        region_stats = df.groupby('Region').agg({
            'rate_percent': 'mean',
            'Funding_min': 'sum'  
        }).reset_index()

        colors_palette = ["#9B7EBD","#D4BEE4","#674188","#A888B5","#BB9CC0","#C8ACD6","#D4BEE4","#E6CCE6","#F3E8FF"][:len(region_stats)]
        
        plt.figure(figsize=(10,6))
        ax = sns.barplot(data=region_stats, x='Region', y='rate_percent', ci=None, palette=colors_palette)
        
        plt.title('Rate Percent by Region', fontsize=14, color='#674188')
        plt.ylabel('Rate Percent', fontsize=12, color='#674188')
        plt.xlabel('Region', fontsize=12, color='#674188')
        plt.xticks(rotation=45, fontsize=10)

        # إضافة القيم مع مبالغ التمويل فوق الأعمدة
        for p, funding in zip(ax.patches, region_stats['Funding_min']):
            height = p.get_height()
            ax.annotate(f'{height:.1f}%\n(${funding:,.0f})', 
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=10, color='black')

        st.pyplot(plt.gcf())  # <<<<<< هذا اللي يخلي الشكل يطلع في Streamlit

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        ">
        Plot shows that Riyadh leads overwhelmingly with 75.6% ($385B), capturing the majority of funding.
        \n Makkah ($71B, 13.7%) and Eastern ($26B, 5%) follow, while other regions attract minimal investment.</div>
        """, unsafe_allow_html=True)
        
        # -------------------
        # رسم جديد: Number of Unique Companies by Year
        # -------------------
        df_filtered = df[df['Year of establishment'].notna() & (df['Year of establishment'] != 0)]
        df_unique = df_filtered.drop_duplicates(subset=['Name', 'Year of establishment'])

        plt.figure(figsize=(12,6))
        ax = sns.countplot(
            data=df_unique, 
            x='Year of establishment', 
            palette=colors_palette, 
            order=sorted(df_unique['Year of establishment'].unique())
        )
        plt.title('Number of Unique Companies by Year of Establishment', fontsize=14, color='#674188')
        plt.xlabel('Year of Establishment', fontsize=12, color='#674188')
        plt.ylabel('Number of Companies', fontsize=12, color='#674188')
        plt.xticks(rotation=45, fontsize=10)

        # إضافة القيم فوق الأعمدة
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height}', 
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=10, color='black')

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        ">
        \n The analysis shows a steady rise in the number of new companies over time, with a sharp increase beginning around 2014.
        \n Company formations peaked in 2019–2020 (34–35 companies), indicating a boom period, followed by slightly lower but still strong activity through 2021–2023.
        </div>
        """, unsafe_allow_html=True)
        
        # -------------------
        # Top 30 Aligned Companies by Funding
        # -------------------
        aligned_companies = df[df['Allign with 2030'] == 'Yes']

        def convert_funding(f):
            if isinstance(f, str):
                f = f.replace(',', '').strip()
                if 'B' in f:
                    return float(f.replace('B','')) * 1000  # المليار -> مليون
                elif 'M' in f:
                    return float(f.replace('M',''))
            return f

        aligned_companies['Funding_Avg_num'] = aligned_companies['Funding_Avg'].apply(convert_funding)
        top_funding = aligned_companies.sort_values('Funding_Avg_num', ascending=False).head(30)

        plt.figure(figsize=(12,6))
        ax = sns.barplot(
            data=top_funding,
            x='Name',
            y='Funding_Avg_num',
            hue='Opportunity_Level',
            dodge=False,
            palette=colors_palette, 
            alpha=0.85
        )

        plt.title("Top 30 Aligned Companies by Funding_Avg (Grouped by Opportunity_Level)", fontsize=14, color='#674188')
        plt.xlabel("Company Name", fontsize=12, color='#674188')
        plt.ylabel("Funding_Avg (Million USD)", fontsize=12, color='#674188')
        plt.xticks(rotation=45, ha='right', fontsize=10)

        # إضافة القيم فوق الأعمدة
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:.1f}M',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=9, color='black')

        plt.legend(title='Opportunity Level', loc='upper right')
        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> The analysis shows that funding distribution is highly concentrated, with Nice One  and Rasan far ahead of other players.
        \n Most remaining companies secured moderate to low funding levels ($10M–$275M), reflecting a market dominated by a few large-scale investments.
        </div>
        """, unsafe_allow_html=True)
        

        # -------------------
        # NumOfTags Companies 
        # -------------------
        multi_tags = df[df['NumOfTags'] > 1]
        top_multi_tags = multi_tags.sort_values('NumOfTags', ascending=False).head(40)

        plt.figure(figsize=(12,6))
        ax = sns.barplot(
            data=top_multi_tags, 
            x='Name', 
            y='NumOfTags', 
            palette=colors_palette
        )

        plt.title('Sample of 40 Companies with More Than One Tag', fontsize=14, color='#674188')
        plt.xlabel('Company Name', fontsize=12, color='#674188')
        plt.ylabel('Number of Tags', fontsize=12, color='#674188')
        plt.xticks(rotation=90, fontsize=10)

        # إضافة القيم فوق الأعمدة
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{int(height)}', 
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=9, color='black')

        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> The analysis shows that some companies stand out with broader diversification, such as Yourparts and TrukKing (10 tags each), indicating wide market reach or multi-sector activity.
        \n Most other companies fall in the 4–8 tag range, reflecting moderate diversification, while only a few maintain very high tag counts.
        </div>
        """, unsafe_allow_html=True)

        # -------------------
        # Year of establishment
        # -------------------
        # فلتر للشركات اللي نبي السنوات
        companies_2023_2025 = df[(df['Year of establishment'] >= 2023) & 
                                (df['Year of establishment'] <= 2025)]

        # نحتفظ بتكرار الشركات للسنوات 2023-2024 بشكل عينة
        companies_2023_2024 = companies_2023_2025[companies_2023_2025['Year of establishment'] < 2025].head(30)

        # كل شركات 2025 تظهر
        companies_2025 = companies_2023_2025[companies_2023_2025['Year of establishment'] == 2025]

        # دمج الشركات
        companies_final = pd.concat([companies_2023_2024, companies_2025])

        plt.figure(figsize=(14,6))
        ax = sns.scatterplot(
            data=companies_final,
            x='Name',
            y='Year of establishment',
            hue='Allign with 2030',
            s=150,
            palette=colors_palette
        )

        plt.title("30 Companies Established 2023-2025 (All 2025 Companies Included)", fontsize=14, color='#674188')
        plt.xlabel("Company Name", fontsize=12, color='#674188')
        plt.ylabel("Year of Establishment", fontsize=12, color='#674188')
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.legend(title="Align with 2030")

        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())


        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> Plot shows that new company establishments between 2023–2025 are active and continuous, with a balanced spread across the years.
        \n Most of these companies are marked as aligned with Vision 2030, reflecting strong alignment of recent startups with national strategic goals.
        </div>
        """, unsafe_allow_html=True)

        # -------------------
        # Allign with 2030
        # -------------------

        # عد الشركات حسب العمود Allign with 2030
        alignment_counts = df['Allign with 2030'].value_counts()
        alignment_percent = df['Allign with 2030'].value_counts(normalize=True) * 100

        labels_box = [f"{idx}: {alignment_counts[idx]} companies ({alignment_percent[idx]:.1f}%)" 
                    for idx in alignment_counts.index]

        # رسم الـ pie
        plt.figure(figsize=(7,7))
        colors = colors_palette[:len(alignment_counts)]  # تأكد من طول الألوان مطابق للبيانات
        plt.pie(
            alignment_counts,
            labels=alignment_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            explode=(0.05, 0) if len(alignment_counts)==2 else None
        )

        plt.title("Alignment of Companies with 2030 Vision")

        # إضافة legend بجانب الرسم
        plt.gca().legend(labels_box, title="Details", loc="center left", bbox_to_anchor=(1, 0.5))

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> The analysis shows that an overwhelming majority of companies (94.8% / 436 companies) are aligned with Vision 2030, while only 5.2% (24 companies) are not.
        \n This reflects a strong national trend of startups and businesses shaping their strategies in line with Saudi Arabia’s Vision 2030 objectives.
        </div>
        """, unsafe_allow_html=True)

        # -------------------
        # Companies with/without Year of Establishment
        # -------------------

        df_with_year = df[df['Year of establishment'].notna() & (df['Year of establishment'] != 0)]
        df_with_year_unique = df_with_year.drop_duplicates(subset=['Name', 'Year of establishment'])

        df_zero_year = df[df['Year of establishment'] == 0]
        df_zero_year_unique = df_zero_year.drop_duplicates(subset=['Name'])

        counts = [len(df_with_year_unique), len(df_zero_year_unique)]
        labels = ['With Year', 'Year = 0']
        percent = [c/sum(counts)*100 for c in counts]
        labels_box = [f"{labels[i]}: {counts[i]} companies ({percent[i]:.1f}%)" for i in range(len(labels))]

        plt.figure(figsize=(7,7))
        colors = colors_palette[:len(counts)]
        plt.pie(
            counts,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            explode=(0.05,0)
        )
        plt.title("Companies with and without Year of Establishment", fontsize=14, color='#674188')
        plt.gca().legend(labels_box, title="Details", loc="center left", bbox_to_anchor=(1, 0.5))
        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> Plot shows that 59.7% of companies (273) have a recorded year of establishment, while 40.3% (184) lack this information.
        \n This gap highlights a significant portion of companies with missing historical data, which may affect trend analysis and ecosystem maturity insights.
        </div>
        """, unsafe_allow_html=True)


        # -------------------
        # Opportunity Levels
        # -------------------

        level_counts = df["Opportunity_Level"].value_counts()

        # Bar chart
        plt.figure(figsize=(6,4))
        level_counts.plot(kind="bar", color=colors_palette)
        plt.title("Distribution of Opportunity Levels", fontsize=14, color='#674188')
        plt.xlabel("Opportunity Level", fontsize=12, color='#674188')
        plt.ylabel("Number of Companies", fontsize=12, color='#674188')
        plt.xticks(rotation=45, fontsize=10)
        plt.tight_layout()
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        ">
       The bar chart shows that most companies are in the Medium opportunity level, while Low is less common and High is very rare.
        </div>
        """, unsafe_allow_html=True)

        # Pie chart
        plt.figure(figsize=(5,5))
        level_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=colors_palette)
        plt.title("Opportunity Levels Share", fontsize=14, color='#674188')
        plt.ylabel("")
        plt.tight_layout()
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        ">
        The pie chart highlights the share, confirming that Medium dominates with ~73%, Low has ~21%, and High only ~6%. \n 
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> The overall analysis indicates that most companies fall into the Medium opportunity level, suggesting that the startup ecosystem is growing steadily but still has limited cases of very high funding, which highlights the need for stronger investment pipelines to support more companies reaching the high level.</div>
        """, unsafe_allow_html=True)
        
        # -------------------
        # Funding distribution per Opportunity Level
        # -------------------

        # Simple converter (M/B/K back to numbers)
        def text_to_number(x):
            if isinstance(x, str):
                if "B" in x: return float(x.replace("B","")) * 1e9
                if "M" in x: return float(x.replace("M","")) * 1e6
                if "K" in x: return float(x.replace("K","")) * 1e3
            return float(x)

        df["Funding_Avg_Num"] = df["Funding_Avg"].apply(text_to_number)

        plt.figure(figsize=(7,5))
        df.boxplot(column="Funding_Avg_Num", by="Opportunity_Level", grid=False)
        plt.title("Funding Average by Opportunity Level", fontsize=14, color='#674188')
        plt.suptitle("")
        plt.xlabel("Opportunity Level", fontsize=12, color='#674188')
        plt.ylabel("Funding Average (USD)", fontsize=12, color='#674188')
        plt.xticks(fontsize=10)
        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        ">
The distribution shows that startups classified as High Opportunity Level receive dramatically larger funding compared to Low and Medium, with some extreme outliers above one billion USD.
        \n In contrast, the Low and Medium groups appear more stable and consistent, but their funding ranges are much smaller, highlighting a strong imbalance in how investments are allocated.
        \n This study highlights a significant funding gap, where only a few high-level startups capture extremely large investments, while the majority remain within much smaller and more stable funding ranges.        </div>
        """, unsafe_allow_html=True)
        
        # -------------------
        # Detect Funding Outliers
        # -------------------

        # 1) Ensure numeric column
        if "Funding_Avg_Num" not in df.columns:
            df["Funding_Avg_Num"] = (
                df["Funding_Avg"]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("K", "e3", regex=False)
                .str.replace("M", "e6", regex=False)
                .str.replace("B", "e9", regex=False)
                .apply(pd.to_numeric, errors="coerce")
            )

        # 2) IQR outlier detection
        Q1 = df["Funding_Avg_Num"].quantile(0.25)
        Q3 = df["Funding_Avg_Num"].quantile(0.75)
        IQR = Q3 - Q1
        threshold = Q3 + 1.5 * IQR
        outliers = df[df["Funding_Avg_Num"] > threshold].copy()

        # 3) Select columns that exist
        want = [
            "Company", "Startup", "Name",
            "Funding (USD)", "Funding_Avg", "Funding_Avg_Num",
            "Opportunity_Level", "Field", "Sector",
            "Tags", "Allign with 2030"
        ]
        cols = [c for c in want if c in outliers.columns]

        # 4) Sort
        outliers = outliers.sort_values("Funding_Avg_Num", ascending=False)

        # -------------------
        # Display in Streamlit
        # -------------------
        st.markdown('<p class="section-header">Top Funding Outliers</p>', unsafe_allow_html=True)
        st.dataframe(outliers[cols].head(20))  # عرض أعلى 20 فقط


        # -------------------
        # Top Funding Outliers (Horizontal Bar)
        # -------------------

        # Ensure numeric column
        if "Funding_Avg_Num" not in df.columns:
            df["Funding_Avg_Num"] = (
                df["Funding_Avg"].astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("K", "e3", regex=False)
                .str.replace("M", "e6", regex=False)
                .str.replace("B", "e9", regex=False)
                .apply(pd.to_numeric, errors="coerce")
            )

        # IQR outliers 
        Q1 = df["Funding_Avg_Num"].quantile(0.25)
        Q3 = df["Funding_Avg_Num"].quantile(0.75)
        IQR = Q3 - Q1
        thresh = Q3 + 1.5 * IQR
        outliers = df[df["Funding_Avg_Num"] > thresh].copy()

        # Pick a name column that exists
        name_candidates = ["Company","Startup","Name","Company Name","Company_Name","Org","Organization"]
        name_col = next((c for c in name_candidates if c in outliers.columns), None)
        outliers["_Label"] = (
            outliers[name_col].astype(str).str.strip() if name_col
            else outliers.index.astype(str)
        )

        # Clean & deduplicate
        outliers = outliers[outliers["_Label"].ne("")].drop_duplicates(subset="_Label")

        # Top N
        TOP_N = 12
        ranked = outliers.sort_values("Funding_Avg_Num", ascending=False).head(TOP_N)
       
        # Plot
        plt.figure(figsize=(9,6))
        plt.barh(ranked["_Label"], ranked["Funding_Avg_Num"], color=colors_palette)
        plt.xlabel("Funding Average (USD)")
        plt.title(f"Top {len(ranked)} Outlier Companies by Funding Average")
        plt.gca().invert_yaxis()
        plt.tight_layout()

        # Display in Streamlit
        st.pyplot(plt.gcf())
        
        
        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */
        "> The analysis shows that Nice One and Rasan dominate as clear outliers, each surpassing $1.2B in funding, far above the rest.
\n Other notable companies like Salla, Cipher, Haraj, Hungerstation, and Almosafe fall within the mid-range (~$250M–$300M), while the majority hold significantly lower funding levels, confirming a highly skewed investment landscape.</div>
        """, unsafe_allow_html=True)

        # -------------------
        # 
        # -------------------

        AL_COL = "Allign with 2030"  # column name

        # Ensure numeric Funding column
        if "Funding_Avg_Num" not in df.columns:
            df["Funding_Avg_Num"] = (
                df["Funding_Avg"].astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("K", "e3", regex=False)
                .str.replace("M", "e6", regex=False)
                .str.replace("B", "e9", regex=False)
                .apply(pd.to_numeric, errors="coerce")
            )

        # IQR outliers
        Q1 = df["Funding_Avg_Num"].quantile(0.25)
        Q3 = df["Funding_Avg_Num"].quantile(0.75)
        IQR = Q3 - Q1
        THRESH = Q3 + 1.5 * IQR
        outliers = df[df["Funding_Avg_Num"] > THRESH].copy()

        # Normalize alignment column
        outliers[AL_COL] = (
            outliers[AL_COL].astype(str).str.strip().str.lower().map({"yes":"Yes","no":"No"})
        )

        # Pick a name column
        name_candidates = ["Company","Startup","Name","Company Name","Company_Name","Org","Organization"]
        name_col = next((c for c in name_candidates if c in outliers.columns), None)
        outliers["_Label"] = (
            outliers[name_col].astype(str).str.strip() if name_col else outliers.index.astype(str)
        )
        outliers = outliers[outliers["_Label"].ne("")]

        # Keep only aligned outliers
        aligned_outliers = outliers[outliers[AL_COL] == "Yes"].copy()

        # Display top-N
        TOP_N = 12
        ranked = aligned_outliers.sort_values("Funding_Avg_Num", ascending=False).head(TOP_N)

        # Plot
        plt.figure(figsize=(9,6))
        plt.barh(ranked["_Label"], ranked["Funding_Avg_Num"], color=colors_palette[:len(ranked)])
        plt.xlabel("Funding Average (USD)")
        plt.title(f"Top {len(ranked)} Aligned Outlier Companies (>{THRESH:,.0f} USD threshold)")
        plt.gca().invert_yaxis()
        plt.tight_layout()

        # Show in Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */ ">
            The analysis indicates that companies with exceptionally high funding averages are already on a strong trajectory. Meanwhile, startups with lower average funding, even though they are aligned with Vision 2030, need to intensify their efforts and adopt more aggressive strategies to unlock higher investment potential and catch up with the leaders.
        """, unsafe_allow_html=True)
    
        # -------------------
        #Tags
        # -------------------

        # حساب التكرار والنسب المئوية لكل Tag
        tag_counts = (
            df["Tags"]
            .str.split(",")          
            .explode()                
            .str.strip()               
            .value_counts()
        )
        tag_percent = (tag_counts / tag_counts.sum()) * 100

        # تصفية الوسوم التي تمثل >= 1.5% من الإجمالي
        filtered = tag_percent[tag_percent >= 1.5]

        # رسم Pie chart
        plt.figure(figsize=(8,8))
        plt.pie(
            filtered.values,
            labels=filtered.index,
            autopct="%1.1f%%",
            startangle=160,
            colors=colors_palette[:len(filtered)]
        )
        plt.title("Distribution of Startup Tags")
        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(plt.gcf())

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */ ">
            By looking at the pie chart, we can see that most companies are concentrated in three main industries: SaaS, AI & Machine Learning, and Marketplace. Together, these sectors account for nearly 60% of the total dataset, highlighting their dominance. The remaining 40% is distributed across a wide range of other industries, each with a smaller share.""", unsafe_allow_html=True)
        
        # -------------------
        # 
        # -------------------

        # حساب عدد الشركات لكل Stage والنسب المئوية
        stage_counts = df["Stage"].value_counts()
        stage_percent = (stage_counts / stage_counts.sum()) * 100
        stage_funding = df.groupby("Stage")["Funding_min"].sum().reindex(stage_counts.index)

        # رسم Bar chart
        fig, ax = plt.subplots(figsize=(10,6))
        bars = ax.bar(stage_counts.index, stage_percent, color="#D4BEE4")

        # إضافة القيم والنصوص فوق الأعمدة
        for i, (pct, fund) in enumerate(zip(stage_percent, stage_funding)):
            ax.text(i, pct + 0.5, 
                    f"{pct:.1f}%\n${fund/1_000_000:.1f}M", 
                    ha="center", va="bottom", fontsize=10)

        ax.set_title("Most Frequent Funding Stages with % of Companies and Total Funding")
        ax.set_ylabel("Percentage of Companies (%)")
        ax.set_xlabel("Stage")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # عرض الرسم في Streamlit
        st.pyplot(fig)

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */ ">
            By looking at the bar chart, we can clearly see that over 50% of the companies are in the Seed stage.  
        This indicates that most of them are still in the initial phase of fundraising, where entrepreneurs seek capital to further develop their product and business model.  
        It also suggests that these companies are relatively early-stage ventures, still building traction and not yet operating at a large scale.
        """, unsafe_allow_html=True)
        
        # -------------------
        # Top Funding Outliers (Horizontal Bar)
        # -------------------

        # فلتر الصناعات اللي تحتوي أكثر من 10 شركات
        valid_industries = df["Industry"].value_counts()
        valid_industries = valid_industries[valid_industries > 10].index
        filtered = df[df["Industry"].isin(valid_industries)].copy()

        filtered["__size__"] = 1  # لكل شركة حجم واحد

        # رسم Treemap
        fig = px.treemap(
            filtered,
            path=[px.Constant("All Industries"), "Industry", "Name"],
            values="__size__",
            color="Industry",
            color_discrete_sequence=px.colors.sequential.Purples
        )
        fig.update_traces(root_color="lavender")
        fig.update_layout(width=900, height=800)

        # عرض الرسم في Streamlit
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"""
        <div style="
            border: 1px solid #D4BEE4;
            border-radius: 8px;
            padding: 15px;
            background-color: white;
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #674188;
            margin-bottom: 20px;  /* هذه المسافة أسفل الصندوق */ ">
            With this treemap, you can clearly see each company and the industry it belongs to, making it easy to visualize how companies are distributed across different sectors.
        """, unsafe_allow_html=True)


# --------------------------
# تاب 5 للخريطة فقط
# --------------------------
with tab4:
    st.subheader("Saudi Arabia Startups Map")

    SA_geo = "SA_regions.json"  # ملف GeoJSON
    SA_map = folium.Map(location=[23,45], zoom_start=5)

    # تحضير إحصائيات المناطق
    region_stats = df.groupby("Region").agg(
        num_companies=("Name", "count"),
        avg_rate_percent=("rate_percent", "mean"),
        avg_funding=("Funding_Avg_Num", "mean"),
        align_2030_count=("Allign with 2030", lambda x: (x=="Yes").sum())
    ).to_dict(orient="index")

    # إضافة المناطق للخرائط
    with open(SA_geo) as f:
        sa_geojson = json.load(f)

    for feature in sa_geojson["features"]:
        region_name = feature["properties"]["name"]
        stats = region_stats.get(region_name, None)
        if stats:
            funding = stats["avg_funding"]
            # تحديد اللون حسب Funding_Avg_Num
            if funding < 1e7:
                color = "#BA9ED3"
            elif funding < 5e7:
                color = "#674188"
            elif funding < 1e8:
                color = "#4F3E5F"
            else:
                color = "#411A63"
            
            popup_text = (
                f"<b>{region_name}</b><br>"
                f"Number of Companies: {stats['num_companies']}<br>"
                f"Average Funding (USD): ${stats['avg_funding']:.0f}<br>"
                f"Average rate_percent: {stats['avg_rate_percent']:.2f}<br>"
                f"Aligned with Vision 2030: {stats['align_2030_count']}"
            )

            folium.GeoJson(
                feature,
                style_function=lambda x, color=color: {"fillColor": color, "color":"black", "weight":1, "fillOpacity":0.6},
                tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["Region:"], labels=True),
                popup=folium.Popup(popup_text, max_width=300)
            ).add_to(SA_map)
    
    folium.LayerControl().add_to(SA_map)
    st_folium(SA_map, width=900, height=600)
#---------------------------------
with tab5:
    st.markdown('<p class="section-header">Complete Data Overview</p>', unsafe_allow_html=True)
    
    # نسخ الداتا المعدلة
    display_df = filtered_df.copy()
    
    # ترتيب حسب Funding_Avg من الأعلى للأدنى
    display_df = display_df.sort_values('Funding_Avg', ascending=False)
    
    # إضافة عمود Rank
    display_df['Rank'] = range(1, len(display_df) + 1)
    
    # اختيار الأعمدة اللي نعرضها
    display_df = display_df[['Rank', 'Name', 'Industry', 'Funding_Avg', 'CompanySize', 'Region', 'Year of establishment']]
    
    # عرض الجدول في Streamlit
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Rank": st.column_config.NumberColumn("Rank", format="%d"),
            "Name": st.column_config.TextColumn("Startup Name"),
            "Industry": st.column_config.TextColumn("Industry"),
            "Funding_Avg": st.column_config.NumberColumn("Average Funding (USD)", format="$,.0f"),
            "CompanySize": st.column_config.TextColumn("Company Size"),
            "Region": st.column_config.TextColumn("Region"),
            "Year of establishment": st.column_config.NumberColumn("Year of Establishment", format="%d")
        }
    )

# ===== Tab 6: Chatbot =====
with tab6:
    st.markdown('<h2 style="color:#674188"> Chat with Marqab (مرقب)</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    /* الصندوق الخارجي لحقل الإدخال + wrapper */
    div.stTextInput {
        background-color: #ffffff !important;  /* خلفية أبيض */
        border: 2px solid #674188 !important;  /* بوردر بنفسجي */
        border-radius: 8px;
        padding: 0.25rem 0.5rem;
    }

    /* المربع الداخلي (input) */
    div.stTextInput > div > input {
        color: #674188 !important;         /* نص بنفسجي غامق */
        background-color: #ffffff !important; /* نفس خلفية الصندوق */
        border: none !important;             /* إزالة البوردر الداخلي */
    }

    /* زر Ask */
    div.stButton > button {
        background-color: #ffffff !important; 
        color: #674188 !important;
        border: 2px solid #674188 !important;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.4rem 1rem;
    }

    div.stButton > button:hover {
        background-color: #f0f0f0 !important;
    }

    /* صندوق كامل للمحادثة (المخرجات) */
    div.stMarkdown > p {
        background-color: #ffffff !important;  /* خلفية أبيض */
        color: #674188 !important;             /* نص بنفسجي غامق */
        padding: 0.5rem 1rem;
        border: 2px solid #674188 !important;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        font-family: 'Inter', sans-serif !important; /* إجبار الخط */
    }
    </style>
""", unsafe_allow_html=True)

    
    user_input = st.text_input("Ask me about a company or a funding stage:", key="chat_input")
    
    if st.button("Ask", key="chat_button") and user_input.strip():
        response = respond(user_input)
        st.markdown(f"**Marqab:** {response}")


# -------------------
# Summary metrics
# -------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Startups", len(filtered_df))

with col2:
    total_funding = filtered_df['Funding_Avg_Num'].sum()
    st.metric("Total Funding (USD)", f"${total_funding:,.0f}")

with col3:
    avg_year = filtered_df['Year of establishment'].mean()
    st.metric("Average Year of Establishment", f"{avg_year:.0f}")

with col4:
    top_funded = filtered_df.loc[filtered_df['Funding_Avg_Num'].idxmax(), 'Name']
    st.metric("Top Funded Startup", top_funded)

# -------------------
# Download section
# -------------------
st.markdown('<p class="section-header">Export Data</p>', unsafe_allow_html=True)
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Complete Dataset (CSV)",
    data=csv,
    file_name='marqab_startup_data.csv',
    mime='text/csv',
    use_container_width=True
)

# -------------------
#ـــــــــــــــــ
# Footer
st.markdown("""
<div class="footer-container">
    <h3 class="footer-title"> Powered by MARQAB</h3>
    <p class="footer-text">Startup Ecosystem Analytics Dashboard</p>
    <p class="footer-text">Empowering data-driven decisions for startup success</p>
</div>
""", unsafe_allow_html=True)

