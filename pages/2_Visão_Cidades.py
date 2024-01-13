# Libraries
import plotly.express as px
import plotly.graph_objects as go

# Necessary libraries
import folium
import pandas as pd
import streamlit as st
import datetime as dt
import inflection
from PIL import Image
from streamlit_folium import folium_static

# Set Streamlit page configuration
st.set_page_config(page_title='Visão Cidade', page_icon='🏙️', layout='wide')

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

####### --- City View --- ########

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

st.sidebar.markdown('#### Created by Marcelo Brandão')

# Filter by countries
linhas_selecionadas = df['country_name'].isin(country_options)
df = df.loc[linhas_selecionadas, :]

### =================================================== ###
#                   Streamlit Layout                      #
### =================================================== ###

st.header('🏙️ Visão Cidade')

# First Line
with st.container():
    st.markdown('#### Top 10 Cidades com mais Restaurantes na Base de Dados')
    df_aux = (df.loc[:, ['city', 'country_name', 'restaurant_id']]
              .groupby(['country_name', 'city'])
              .nunique()
              .reset_index()
              .sort_values(['restaurant_id', 'city'], ascending=[False, True]))
    df_aux = df_aux.head(10)

    # Define colors for each country
    country_colors = {
        "India": "red",
        "Australia": "blue",
        "Brazil": "green",
        # Add more colors for other countries here
    }

    # Add a colors column based on the country
    df_aux['color'] = df_aux['country_name'].map(country_colors)

    # Create a color map for the legend
    color_map = {country: color for country, color in country_colors.items()}
    legend_colors = [color_map.get(country) for country in df_aux['country_name'].unique()]

    # Create the bar chart with colors and legend
    fig = px.bar(df_aux, x='city', y='restaurant_id', color='country_name', color_discrete_map=country_colors)
    fig.update_layout(
        xaxis_title='Cities',
        yaxis_title='Number of Restaurants',
        legend_title='Country',
        legend=dict(
            title='Country',
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1,
            traceorder="normal",
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=True
    )
    
    # Add data labels
    for i in range(len(fig.data)):                
                fig.data[i].text = fig.data[i].y

    # Display the bar chart
    st.plotly_chart(fig, use_container_width=True)
    
    
# Second Line            
with st.container():
    col1, col2 = st.columns(2)        

    with col1:
        st.markdown('#### Top 7 cidades com restaurantes com média de avaliação acima de 4')  
        filtered_df = df[df['aggregate_rating'] > 4]
        result = (filtered_df[['city', 'country_name', 'aggregate_rating']]
                  .groupby(['city', 'country_name'])
                  .count()
                  .reset_index()
                  .sort_values(['aggregate_rating', 'city'], ascending=[False, True]))
        df_aux = result.head(7)

        # Define colors for each country
        country_colors = {
            "India": "red",
            "Australia": "blue",
            "Brazil": "green",
            # Add more colors for other countries here
        }

        # Add a colors column based on the country
        df_aux['color'] = df_aux['country_name'].map(country_colors)

        # Create a color map for the legend
        color_map = {country: color for country, color in country_colors.items()}
        legend_colors = [color_map.get(country) for country in df_aux['country_name'].unique()]

        # Create the bar chart with colors and legend
        fig = px.bar(df_aux, x='city', y='aggregate_rating', color='country_name', color_discrete_map=country_colors)
        fig.update_layout(
            xaxis_title='Cities',
            yaxis_title='Number of Restaurants',
            legend_title='Country',
            legend=dict(
                title='Country',
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=1,
                traceorder="normal",
                bgcolor='rgba(0,0,0,0)'
            ),
            showlegend=True
        )
        
        # Add data labels
        for i in range(len(fig.data)):                
            fig.data[i].text = fig.data[i].y
        
        # Display the bar chart
        st.plotly_chart(fig, use_container_width=True)
            
        
    with col2:
        st.markdown('#### Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5')            
        filtered_df = df[df['aggregate_rating'] < 2.5]
        result = (filtered_df[['city', 'country_name', 'aggregate_rating']]
                  .groupby(['city', 'country_name'])
                  .count()
                  .reset_index()
                  .sort_values(['aggregate_rating', 'city'], ascending=[False, True]))
        df_aux = result.head(7)

        # Define colors for each country
        country_colors = {
            "India": "red",
            "Australia": "blue",
            "Brazil": "green",
            # Add more colors for other countries here
        }

        # Add a colors column based on the country
        df_aux['color'] = df_aux['country_name'].map(country_colors)

        # Create a color map for the legend
        color_map = {country: color for country, color in country_colors.items()}
        legend_colors = [color_map.get(country) for country in df_aux['country_name'].unique()]

        # Create the bar chart with colors and legend
        fig = px.bar(df_aux, x='city', y='aggregate_rating', color='country_name', color_discrete_map=country_colors)
        fig.update_layout(
            xaxis_title='Cities',
            yaxis_title='Number of Restaurants',
            legend_title='Country',
            legend=dict(
                title='Country',
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=1,
                traceorder="normal",
                bgcolor='rgba(0,0,0,0)'
            ),
            showlegend=True
        )
        
        # Add data labels
        for i in range(len(fig.data)):                
            fig.data[i].text = fig.data[i].y
        
        # Display the bar chart
        st.plotly_chart(fig, use_container_width=True)
        

# Third Line
with st.container():
    st.markdown('#### Top 10 cidades com mais restaurantes com tipos culinários distintos')
    df_aux = (df.loc[:, ['city', 'country_name', 'cuisines']]
              .groupby(['country_name', 'city'])
              .nunique()
              .reset_index()
              .sort_values(['cuisines', 'city'], ascending=[False, True]))
    df_aux = df_aux.head(10)

    # Define colors for each country
    country_colors = {
        "India": "red",
        "Australia": "blue",
        "Brazil": "green",
        # Add more colors for other countries here
    }

    # Add a colors column based on the country
    df_aux['color'] = df_aux['country_name'].map(country_colors)

    # Create a color map for the legend
    color_map = {country: color for country, color in country_colors.items()}
    legend_colors = [color_map.get(country) for country in df_aux['country_name'].unique()]

    # Create the bar chart with colors and legend
    fig = px.bar(df_aux, x='city', y='cuisines', color='country_name', color_discrete_map=country_colors)
    fig.update_layout(
        xaxis_title='Cities',
        yaxis_title='Number of Unique Cuisines',
        legend_title='Country',
        legend=dict(
            title='Country',
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1,
            traceorder="normal",
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=True
    )

    # Add data labels
    for i in range(len(fig.data)):                
                fig.data[i].text = fig.data[i].y
    
    # Display the bar chart
    st.plotly_chart(fig, use_container_width=True)
