import streamlit as st
import pandas as pd

# Cargar datos desde el archivo CSV
def load_users():
    df = pd.read_csv('pages/user.csv')  
    return df

# Función para validar el usuario
def validar_usuario(username, password):
    df = load_users()
    user_data = df[(df['usuario'] == username) & (df['contraseña'] == password)]
    if not user_data.empty:
        return user_data.iloc[0]  # Retornar la primera coincidencia encontrada
    else:
        return None

# Comprobamos si estamos en la página principal o de login
page = st.query_params.get('page', ['login'])[0]

if page == 'login':
    # Código para mostrar el formulario de login
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    login_button = st.button("Iniciar Sesión")

    if login_button:
        user_data = validar_usuario(username, password)
        if user_data is not None:
            st.success(f"Bienvenido {username}")
            if user_data['rol'] == 'admin':
                st.switch_page('pages/dash.py')
            else:
                st.switch_page('pages/Usuario.py')
            
        else:
            st.error("Usuario o contraseña incorrectos")

