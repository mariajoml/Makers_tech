import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")



def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style/styles.css')

# Función para cargar los datos desde el archivo CSV
def get_inventory():
    df = pd.read_csv('pages/inventario.csv')  
    return df
# Cargar los datos
df = get_inventory()

# Calcular ganancias aproximadas
df['Ganancias'] = df['Precio'] * df['Stock']

color_encode = True

# Layout y gráficos
container = st.container()
chart1, chart2 = container.columns(2)

# GRÁFICOS

with chart1:
    fig = px.scatter(df, x='Precio', y='Stock', color='Marca' if color_encode else None, title="Precio vs Stock")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    fig_bar = px.bar(df, x='Marca', y='Ganancias', title="Ganancias Aproximadas por Marca")
    st.plotly_chart(fig_bar, use_container_width=True)

st.header("Cantidad en Stock por Tipo de Computadora")
fig_stock = px.bar(df.groupby('Tipo')['Stock'].sum().reset_index(), x='Tipo', y='Stock', title="Cantidad en Stock por Tipo de Computadora")
st.plotly_chart(fig_stock, use_container_width=True)

st.header("Precio Promedio por Marca")
fig_price = px.bar(df.groupby('Marca')['Precio'].mean().reset_index(), x='Marca', y='Precio', title="Precio Promedio por Marca")
st.plotly_chart(fig_price, use_container_width=True)
