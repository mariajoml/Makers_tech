import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Usuario - Makers Tech", page_icon="🛒", layout="wide")

# Función para cargar el CSS desde un archivo
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Cargar el CSS desde la carpeta 'style'
load_css('style/styless1.css')

# Inicializar el carrito de compras en session_state si no existe
if "cart" not in st.session_state:
    st.session_state.cart = []

# Crear el sidebar con opciones
st.sidebar.title("Opciones")
page = st.sidebar.radio("Selecciona una opción:", ["Comprar", "Asesoría", "Novedades"])

# Mostrar el contenido según la opción seleccionada
if page == "Comprar":
    st.title("🛒 Comprar Computadoras en Makers Tech")
    st.write("Aquí encontrarás nuestra selección de computadoras de alta calidad. Cada producto ha sido cuidadosamente seleccionado para ofrecerte el mejor rendimiento y valor.")

    # Productos
    products = [
        {
            "name": "Dell Inspiron 15",
            "image": "Images/dell.png",
            "price": 700,
            "description": "Laptop Dell Inspiron 15 con procesador Intel Core i5, 8GB de RAM y 256GB SSD. Ideal para tareas diarias y productividad."
        },
        {
            "name": "Asus VivoBook 14",
            "image": "Images/aseso.png",
            "price": 650,
            "description": "Laptop Asus VivoBook 14 con procesador AMD Ryzen 5, 8GB de RAM y 512GB SSD. Compacta y potente para el uso diario."
        },
        {
            "name": "Apple MacBook Air",
            "image": "Images/apple.png",
            "price": 999,
            "description": "Apple MacBook Air con chip M1, 8GB de RAM y 256GB SSD. Diseño ligero y potente, perfecto para usuarios avanzados."
        },
        {
            "name": "Lenovo ThinkPad X1",
            "image": "Images/lenovo.png",
            "price": 1200,
            "description": "Lenovo ThinkPad X1 con procesador Intel Core i7, 16GB de RAM y 1TB SSD. La elección preferida de profesionales."
        },
        {
            "name": "Acer Predator Helios 300",
            "image": "Images/acer.png",
            "price": 1500,
            "description": "Laptop gamer Acer Predator Helios 300 con Intel Core i7, 16GB de RAM y 1TB SSD. Perfecta para juegos exigentes."
        },
        {
            "name": "Toshiba Dynabook Tecra",
            "image": "Images/toshiba.png",
            "price": 750,
            "description": "Toshiba Dynabook Tecra con Intel Core i5, 8GB de RAM y 256GB SSD. Fiabilidad y durabilidad en un diseño clásico."
        }
    ]

    # Mostrar productos y manejar la acción de agregar al carrito
    for product in products:
        st.write("##")
        cols = st.columns([1, 2])
        with cols[0]:
            image = Image.open(product["image"])
            st.image(image, use_column_width=True)
        with cols[1]:
            st.subheader(product["name"])
            st.write(f"**Precio:** ${product['price']}")
            st.write(product["description"])
            if st.button(f"Comprar ahora - {product['name']}"):
                st.session_state.cart.append(product)
                st.success(f"Agregado al carrito: {product['name']}")

    # Mostrar el carrito de compras
    if st.session_state.cart:
        st.write("##")
        st.header("🛒 Carrito de Compras")
        total = 0
        for item in st.session_state.cart:
            st.write(f"- **{item['name']}**: ${item['price']}")
            total += item['price']
        st.write("### Total acumulado: $" + str(total))

elif page == "Asesoría":
    st.title("📞 Asesoría en Makers Tech")
    st.write("""
        ¿Tienes dudas o necesitas ayuda para elegir el producto adecuado?
        Nuestro equipo de expertos está disponible 24/7 para ofrecerte asesoramiento.
    """)
    st.write("### Opciones de Asesoría:")
    st.write("- Llamada telefónicas +57 3107545406")
    st.write("- Correo electrónico makerstech@gmail.com")
    st.write("### ¿Prefieres hablar con nuestro asistente virtual?")
    btn_nexy = st.button('Habla con Nexy 🤖')
    if btn_nexy:
        st.switch_page('pages/nexy.py')

elif page == "Novedades":
    st.title("📰 Novedades en Makers Tech")
    st.write("""
        Mantente al día con las últimas tendencias tecnológicas y productos nuevos 
        en nuestro inventario.
    """)
    st.write("### Noticias recientes:")

    st.write("- Lanzamientos")
    st.write("[Dell presenta sus nuevas laptops y workstations vitaminadas con IA >](https://es.wired.com/articulos/dell-presenta-sus-nuevas-laptops-y-workstations-vitaminadas-con-ia)")
    st.write("[HP presenta nuevas computadoras con procesadores para IA >](https://expansion.mx/tecnologia/2024/01/09/hp-presenta-nuevas-computadoras-con-procesadores-para-ia)")
    st.write("- Ofertas especiales de temporada")
    st.write("")
    st.write("Por el momento no contamos con ofertas")
    st.write("")
    st.write("- Somos distribuidores oficiales de:")
    Distribuidores = [
        {
            "image": "Images/asusl.png",
            
        },
        {
            "image": "Images/applel.png",
           
        },
        {
            "image": "Images/acerl.png",
            
        },
        {
            "image": "Images/lenovol.png",
            
        }
        
    ]
    for Distribuidores in Distribuidores:
        st.write("##")
        cols = st.columns([1, 2])
        with cols[0]:
            image = Image.open(Distribuidores["image"])
            st.image(image, use_column_width=True)
    