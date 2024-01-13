# Libraries
import plotly.express as px
import plotly.graph_objects as go
from utils.cuisinesfunc import metric_cuisine, cuisines_higher, cuisines_lower
import utils.cuisinesfunc as cuisinesfunc
import folium
import pandas as pd
import streamlit as st
import datetime as dt
import inflection
from PIL import Image
from utils import markdown as mk
from streamlit_folium import folium_static

st.set_page_config(page_title='Visão Cidade', page_icon='🍽️', layout='wide')

# ---------------------------------
# Functions
# ---------------------------------

# Country name mapping
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]

# Create food category based on price range
def create_price_type(price_range):
    return {
        1: "cheap",
        2: "normal",
        3: "expensive",
    }.get(price_range, "gourmet")

# Color name mapping
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS.get(color_code, "unknown")

# Rename columns of the DataFrame
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# Apply previous functions
def clean_code(df):
    df['color_name'] = df['Rating color'].apply(color_name)
    df['country_name'] = df['Country Code'].apply(country_name)
    df['food_category'] = df['Price range'].apply(create_price_type)
    df = rename_columns(df)
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0] if isinstance(x, str) else x)
    return df

# Import dataset
df = pd.read_csv('fome_zero.csv')

# Cleaning dataset
df = clean_code(df)

####### --- Cuisine View --- ########

## Dashboard Sidebar

st.sidebar.markdown(""" --- """)
st.sidebar.markdown("""# Filters""")

# Multiple selection of countries
country_options = st.sidebar.multiselect(
    'Choose the countries you want to visualize:',
    ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
     'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland',
     'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'],
    default=['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
             'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland',
             'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'])

st.sidebar.markdown(""" --- """)

# Slider for selecting the number of restaurants
select_quant_restaurant = st.sidebar.slider(label='Select the number of restaurants',
                                            value=(10),
                                            max_value=20)
st.sidebar.markdown('---')

# Multi-selection for choosing types of cuisines
select_cuisines_mult = st.sidebar.multiselect(label='Choose the types of cuisine',
                                              options=df.cuisines.unique(),
                                              default=['Italian', 'American', 'Arabian', 'Japanese', 'Brazilian'])

st.sidebar.markdown('#### Created by Marcelo Brandão')

# Filter by countries
linhas_selecionadas = df['country_name']

df = df[df['country_name'].isin(country_options)]

### =================================================== ###
#                   layout streamlit                      #
### =================================================== ###

st.header('🍽️ Visão Cozinhas')

with st.container():
    st.title('Melhores Restaurantes dos Principais tipos Culinários')    

    Italian, American, Arabian, Japanese, Brazilian = st.columns(5)
        
    with Italian:
        metric_cuisine(df, 'Italian')
    with American:
        metric_cuisine(df, 'American')
    with Arabian:
        metric_cuisine(df, 'Arabian')
        
    with Japanese:
        metric_cuisine(df, 'Japanese')
    with Brazilian:
        metric_cuisine(df, 'Brazilian')
    st.markdown('---')

with st.container():
    
    st.title(f"Top {select_quant_restaurant} Restaurantes com Melhores Avaliações")
    st.dataframe(df[['restaurant_name',
                        'country_name',
                        'city',
                        'cuisines',
                        'aggregate_rating']].sort_values(by= 'aggregate_rating', ascending = False).head(select_quant_restaurant), use_container_width= True)

    st.markdown('---')
    
with st.container():
    
    col1, col2 = st.columns(2)
    
    with col1:
        #title
        corpo = mk.aling(h = 'h4', text=f"Top {select_quant_restaurant}Tipos de Culinárias com as Melhores Avaliações" )
        st.markdown(corpo, unsafe_allow_html= True)
        
        #plot
        
        fig = cuisinesfunc.cuisines_higher(df, select_quant_restaurant)
        st.plotly_chart(fig, use_container_width= True)
        
    with col2:
        corpo = mk.aling(h = 'h4', text=f"Top {select_quant_restaurant} Tipos de Culinárias com as Piores Avaliações" )
        st.markdown(corpo, unsafe_allow_html= True)
        
        fig = cuisinesfunc.cuisines_lower(df, select_quant_restaurant)   
        st.plotly_chart(fig, use_container_width= True)
    
