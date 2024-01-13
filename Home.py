# Libraries
import plotly.express as px
import plotly.graph_objects as go
import base64
import folium
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import inflection

st.set_page_config(page_title='Home', page_icon='🎲', layout='wide')

# ---------------------------------
# Functions
# ---------------------------------

# Filling country names
COUNTRIES = {
    1: "India", 14: "Australia", 30: "Brazil", 37: "Canada", 94: "Indonesia",
    148: "New Zeland", 162: "Philippines", 166: "Qatar", 184: "Singapure",
    189: "South Africa", 191: "Sri Lanka", 208: "Turkey",
    214: "United Arab Emirates", 215: "England", 216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES.get(country_id, "")

# Creating food category
def create_price_type(price_range):
    categories = {1: "cheap", 2: "normal", 3: "expensive"}
    return categories.get(price_range, "gourmet")

# Creating color names
COLORS = {
    "3F7E00": "darkgreen", "5BA829": "green", "9ACD32": "lightgreen",
    "CDD614": "orange", "FFBA00": "red", "CBCBC8": "darkred", "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS.get(color_code, "")

# Renaming DataFrame columns
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x).replace(" ", "")
    snakecase = lambda x: inflection.underscore(x)
    cols_new = list(map(snakecase, map(title, df.columns)))
    df.columns = cols_new
    return df

# Applying preprocessing functions
def clean_code(df):
    df['color_name'] = df['Rating color'].apply(color_name)
    df['country_name'] = df['Country Code'].apply(country_name)
    df['food_category'] = df['Price range'].apply(create_price_type)
    df = rename_columns(df)
    df["cuisines"] = df["cuisines"].apply(lambda x: x.split(",")[0] if isinstance(x, str) else x)
    return df

# Creating a map based on the DataFrame passed
def map_maker(df):
    folium.Figure(width=1920, height=768)
    aux = df.copy()
    map = folium.Map(location=[0, 0], zoom_start=2)
    make_cluster = MarkerCluster().add_to(map)

    for index, row in aux.iterrows():
        restaurant = row['restaurant_name']
        cuisines = row['cuisines']
        rating = row['aggregate_rating']

        html = f'<p><strong>{restaurant}</strong></p><p>{cuisines}</p><p>{rating}</p>'
        pp = folium.Html(html, script=True)
        folium.Marker(location=[row['latitude'], row['longitude']],
                      icon=folium.Icon(color=row['color_name']),
                      popup=folium.Popup(pp, max_width=500)).add_to(make_cluster)

    folium_static(map, width=1024, height=600)

# Import dataset
df = pd.read_csv('fome_zero.csv')

# Cleaning dataset
df = clean_code(df)

# Dashboard
st.sidebar.image(Image.open('logo.png'), width=120)
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown(""" --- """)
with st.sidebar:
    components.html("""
                    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="light" data-type="VERTICAL" data-vanity="marcelo-lira-brandao" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/marcelo-lira-brandao?trk=profile-badge"></a></div>
                    <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>              
              """, height= 310)

st.sidebar.markdown(""" --- """)
st.sidebar.markdown("""# Filtros""")

country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as Informações:',
    ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
     'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland',
     'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey'],
    default=['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada',
             'Singapure', 'United Arab Emirates', 'India', 'Indonesia', 'New Zeland',
             'England', 'Qatar', 'South Africa', 'Sri Lanka', 'Turkey']
)

st.sidebar.markdown(""" --- """)


if st.sidebar.button('Baixar Dados'):
    csv_data = df.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="dados.csv">Baixar Dados CSV</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)


select_country = df[df['country_name'].isin(country_options)]

linhas_selecionadas = df['country_name'].isin(country_options)
df = df.loc[linhas_selecionadas, :]

st.markdown("""
    <div style="text-align: center;">
        <h1>Fome Zero</h1>
        <h2>O melhor marketplace de restaurantes!</h2>        
    </div>
    """,
    unsafe_allow_html=True)
st.markdown( """---""" )
st.markdown( """### Principais numeros da plataforma:""" )

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='large' )
    with col1:
        st.metric('Restaurantes Cadastrados', df['restaurant_id'].nunique())

    with col2:
        st.metric('Países Cadastrados', df['country_name'].nunique())

    with col3:
        st.metric('Cidades Cadastradas', df['city'].nunique())

    with col4:
        st.metric('Avaliações Feitas na Plataforma', df['votes'].sum())

    with col5:
        st.metric('Tipos de Culinárias Oferecidas', df['cuisines'].nunique())

with st.container():
    map_maker(select_country)
