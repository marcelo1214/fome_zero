# Libraries
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go

# bibliotecas necessárias
import folium
import pandas as pd
import streamlit as st
import datetime as dt
import inflection
from PIL import Image

from streamlit_folium import folium_static

st.set_page_config( page_title='Visão Países', page_icon='🌎', layout='wide' )

# ---------------------------------
# Funções
# ---------------------------------

#Preenchimento do nome dos países
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

#Criação do Tipo de Categoria de Comida
def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

#Criação do nome das Cores
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
    return COLORS[color_code]

#Renomear as colunas do DataFrame
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

#Apply previous functions
def clean_code(df):
    df['color_name'] = df['Rating color'].apply(color_name)
    df['country_name'] = df['Country Code'].apply(country_name)
    df['food_category'] = df['Price range'].apply(create_price_type)
    df = rename_columns(df)
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0] if isinstance(x, str) else x)
    return df

# Import dataset
df = pd.read_csv('fome_zero.csv')

# cleaning dataset
df = clean_code( df )



####### --- Visão Países --- ########

## Barra Lateral do dashboard

st.header('🌎 Visão Países')

# ## colocando a imagem: 
# image_path = 'logo.png'
# image = Image.open(image_path)
# st.sidebar.image(image, width=120)

# st.sidebar.markdown('# Cury Company')
# st.sidebar.markdown('## Fastest Delivery in Town')
# st.sidebar.markdown("""---""")



# #st.header(date_slider)
st.sidebar.markdown(""" --- """)
st.sidebar.markdown("""# Filtros""")

## multipla seleção das condições de trânsito:
country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as Informações:',
    ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
 'Singapure','United Arab Emirates','India','Indonesia','New Zeland',
 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'],
    default=['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
 'Singapure','United Arab Emirates','India','Indonesia','New Zeland',
 'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'])

st.sidebar.markdown(""" --- """)

st.sidebar.markdown('#### Created by Marcelo Brandão')

# filtro de data:
# linhas_selecionadas = df1['Order_Date'] < date_slider
# df1 = df1.loc[linhas_selecionadas, :]


# filtro de paises:
linhas_selecionadas = df['country_name'].isin(country_options)
df = df.loc[linhas_selecionadas, :]


### =================================================== ###
#                   layout streamlit                      #
### =================================================== ###

#First Line
with st.container():
    st.markdown('#### Quantidade de Restaurantes Registrados por País') # gráico de barra -
    df_aux = (df.loc[:, ['restaurant_id', 'country_name']]
                .groupby(['country_name'])
                .nunique()
                .reset_index()
                .sort_values('restaurant_id', ascending=False))
    fig = px.bar(df_aux, x = 'country_name', y= 'restaurant_id')
    #fig = fig.sort_values('restaurant_id', ascending=False)
    fig.update_layout(
        xaxis_title='Países',
        yaxis_title='Quantidade de Restaurantes'
    )
    
    for i in range(len(fig.data)):
        fig.data[i].text = fig.data[i].y
    
    st.plotly_chart(fig, use_container_width=True)
    
#Second Line
with st.container():
    st.markdown('#### Quantidade de Cidades Registrados por País') # gráico de barra -
    df_aux = (df.loc[:, ['city', 'country_name']]
                .groupby(['country_name'])
                .nunique()
                .reset_index()
                .sort_values('city', ascending=False))
    fig = px.bar(df_aux, x = 'country_name', y= 'city')
    #fig = fig.sort_values('restaurant_id', ascending=False)
    fig.update_layout(
        xaxis_title='Países',
        yaxis_title='Quantidade de Cidades'
    )
    
    for i in range(len(fig.data)):
        fig.data[i].text = fig.data[i].y
    
    st.plotly_chart(fig, use_container_width=True) 
            
#Third Line
with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('#### Média de Avaliações Feitas por País')
            df_aux = (df.loc[:, ['votes', 'country_name']]
                        .groupby(['country_name'])
                        .mean().reset_index()
                        .sort_values('votes', ascending=False))
            
            fig = px.bar(df_aux, x = 'country_name', y= 'votes')            
            fig.update_layout(
                xaxis_title='Países',
                yaxis_title='Quantidade de Avaliações'
            )
            for trace in fig.data:
                trace.texttemplate = '%{y:.2f}'
            for i in range(len(fig.data)):                
                fig.data[i].text = fig.data[i].y
        
            st.plotly_chart(fig, use_container_width=True)
            
        
        with col2:
            st.markdown('#### Média de Preço de um prato para duas pessoas por País')
            df_aux = (df.loc[:, ['average_cost_for_two', 'country_name']]
                        .groupby(['country_name'])
                        .mean().reset_index()
                        .sort_values('average_cost_for_two', ascending=False))
            
            fig = px.bar(df_aux, x = 'country_name', y= 'average_cost_for_two')            
            fig.update_layout(
                xaxis_title='Países',
                yaxis_title='Preço médio do prato para duas Pessoas'
            )
            for trace in fig.data:
                trace.texttemplate = '%{y:.2f}'
            for i in range(len(fig.data)):                
                fig.data[i].text = fig.data[i].y
        
            st.plotly_chart(fig, use_container_width=True)
        # with col2:
        #     st.markdown('#### Média de Preço de um prato para duas pessoas por País')
        #     df_aux = df1.loc[:, ['ID', 'City', 'Road_traffic_density']].groupby(['City', 'Road_traffic_density']).count().reset_index()
        #     fig = px.scatter(df_aux, x='City', y='Road_traffic_density', size='ID', color='City')
        #     st.plotly_chart(fig, use_container_width=True)
