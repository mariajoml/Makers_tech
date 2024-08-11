import requests
import streamlit as st
from PIL import Image
import button as button


# Configuración de la página
st.set_page_config(page_title="MAKERS TECH", page_icon="🚀", layout="wide")

# Función para cargar el CSS 
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Cargar el CSS desde la carpeta 'style'
load_css('style/styless1.css')

# Encabezado principal
with st.container():
    st.header("Hola! Bienvenido a Makers Tech 🚀")
    st.subheader("Te ofrecemos los mejores productos tecnológicos con asesoramiento 24/7")

# Botón de login 
with st.container():
    col1, col2, col3 = st.columns([2, 2, 0.5])
    with col2:
        btnlog = st.button('Log In')
        if btnlog:
            st.switch_page('pages/log.py')

# ¿Quiénes somos?
with st.container():
    st.write("---")
    st.header("¿Quiénes somos?")
    text_column, image_column = st.columns([1.5, 1])
    with text_column:
        st.write(
            """
            En Makers Tech, somos apasionados por la innovación y la tecnología. Como una empresa líder en el comercio electrónico, nos especializamos en ofrecer productos tecnológicos de alta calidad que facilitan la vida de nuestros clientes y potencian sus proyectos personales y profesionales.

            Desde nuestra fundación, hemos trabajado incansablemente para construir una plataforma que no solo vende productos, sino que también educa e inspira. Nos enorgullece ser más que una tienda: somos un espacio donde los entusiastas de la tecnología pueden descubrir, aprender y crecer.
            """
        )
    with image_column:
        image = Image.open("Images/logo.png")
        st.image(image, use_column_width=True)

# Servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")

    # Venta de equipos
    image_column, text_column = st.columns([1, 2])
    with image_column:
        image = Image.open("Images/compu.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Venta de equipos")
        st.write(
            """
            En Makers Tech, nos especializamos en la venta de equipos tecnológicos 🖥 de última generación, cuidadosamente seleccionados para satisfacer las necesidades tanto de profesionales como de entusiastas de la tecnología. Ofrecemos una amplia gama de productos, desde computadoras y accesorios hasta dispositivos inteligentes para el hogar, garantizando siempre la mejor calidad y rendimiento.     
            """
        )

    # Asesoramiento 24/7
    st.write("##")
    image_column, text_column = st.columns([1, 2])
    with image_column:
        image = Image.open("Images/aseso.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Asesoramiento 24/7⏰")
        st.write(
            """
            En Makers Tech, entendemos que las preguntas y los desafíos técnicos pueden surgir en cualquier momento. Por eso, ofrecemos un servicio de asesoramiento 24/7, disponible para ayudarte a resolver tus dudas y guiarte en la elección y uso de nuestros productos, sin importar la hora del día. Nuestro equipo de expertos está siempre a tu disposición para brindarte soporte y asegurarse de que tengas la mejor experiencia posible con la tecnología, cuando lo necesites. 
            """
        )

# Sección de contacto
with st.container():
    st.write("---")
    st.header("¿Necesitas información, tienes dudas o simplemente quieres asesoría?")
    
    col1, col2, col3 = st.columns([2, 2, 0.5])
    with col2:
        btnnexy = st.button('Habla con Nexy 🤖')
        if btnnexy:
            st.switch_page('pages/nexy.py')

# Footer 
with st.container():
    st.write("---")
    st.markdown("<p style='text-align: center;'>© 2024 Makers Tech - Todos los derechos reservados.</p>", unsafe_allow_html=True)