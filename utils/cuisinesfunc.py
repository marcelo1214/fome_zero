import plotly.express as px
import streamlit as st

def cuisines_ratting(df, cuisine, ascending = True):
    cols = ['restaurant_name', 'country_name', 'aggregate_rating']
    df = df[df.cuisines.isin([cuisine])]
    return df

def metric_cuisine(df1, culinaria):
        cuisine_aux = cuisines_ratting(df = df1, cuisine= culinaria, ascending= False).head(1)
        st.metric(label = f"{culinaria}: {cuisine_aux['restaurant_name'].values[0]}\n",
                    value= f"{cuisine_aux['aggregate_rating'].values[0]}/5.0",
                    help = f"""
                    País: {cuisine_aux['country_name'].values[0]}\n
                    Cidade: {cuisine_aux['city'].values[0]}\n
                    Média Prato para dois: {cuisine_aux['average_cost_for_two'].values[0]}\n
                    """)
        return 

def cuisines_higher(df, select_quant_restaurant):
    cols = ['cuisines', 'aggregate_rating']
    aux = df[cols].groupby('cuisines').mean('aggregate_rating').sort_values('aggregate_rating', ascending = False).reset_index().head(select_quant_restaurant)
    fig = px.bar(aux, x = 'cuisines', y ='aggregate_rating',
                labels= {
                    'aggregate_rating': 'Avaliação',
                    'cuisines': 'Culinária'
                })
    return fig


def cuisines_lower(df, select_quant_restaurant):
    cols = ['cuisines', 'aggregate_rating']
    aux = df[cols].groupby('cuisines').mean('aggregate_rating').sort_values('aggregate_rating', ascending = True).reset_index().head(select_quant_restaurant)
    aux = aux[aux['aggregate_rating']> 0]
    fig = px.bar(aux, x = 'cuisines', y ='aggregate_rating',
                labels= {
                    'aggregate_rating': 'Avaliação',
                    'cuisines': 'Culinária'}, color_discrete_sequence= ['red'])
    return fig