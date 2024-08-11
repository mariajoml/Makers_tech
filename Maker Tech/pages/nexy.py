import sqlite3
import streamlit as st
import time
from groq import Groq
from typing import Generator

st.set_page_config(page_title="Nexy", page_icon="🤖", layout="wide")
st.title("Nexy 🤖")

client = Groq(
    api_key=st.secrets["ngroqAPIKey"], 
)

modelos = ['llama3-8b-8192']

# Conexión a la base de datos SQLite
def connect_db():
    conn = sqlite3.connect('inventario_computadores.db') 
    return conn

def get_inventory():
    conn = connect_db()
    query = "SELECT * FROM Computadores"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:   
    """Generated Chat Responses for Makers Tech

       This function generates chat responses by processing the chat completion information related to Makers Tech.
       The responses are displayed character by character, ensuring an interactive and smooth experience for the user.

       Instructions for the model:
       - You are representing Makers Tech, a company that provides equipment sales services.
       - Process the chat completion data, focusing on extracting and presenting information about available computers, specifications, pricing, and company services.
       - Ensure that the content is clear, relevant, and provides value to the user.
       - Prioritize information about computer inventory (e.g., processor, RAM, storage) and company-related queries (e.g., company mission, services).
       - Only yield content that directly answers the user's query, avoiding any unnecessary metadata or irrelevant information.
       - Maintain a professional and friendly tone throughout the responses.

       Args:
           chat_completion (str): The chat completion information, expected to be an iterable containing chunks of the response.

       Yields:
           str: Each part of the generated response, character by character.
    """ 
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mensaje inicial del sistema que proporciona el contexto 
if not st.session_state.messages:
    system_message = {
        "role": "system",
        "content": (
            "You are an assistant representing Makers Tech, a company that provides equipment sales services. "
            "Your role is to help users by providing detailed information about the company's inventory of computers, "
            "specifications, pricing, and services offered by Makers Tech."
        )
    }
    st.session_state.messages.append(system_message)

# Muestra solo los mensajes de chat del usuario y el asistente en la aplicación
with st.container():
    for message in st.session_state.messages:
        if message["role"] != "system":  # Evita mostrar el mensaje del sistema
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# Mostramos el campo para el prompt del usuario
prompt = st.chat_input("¿En que te puedo ayudar el dia de hoy?")

if prompt:
    # Mostrar mensaje de usuario en el contenedor de mensajes de chat
    st.chat_message("user").markdown(prompt)
    # Agregar mensaje de usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Realizar consulta de inventario si es necesario
    if "inventory" in prompt.lower() or "computers" in prompt.lower():
        inventory_df = get_inventory()
        response_content = inventory_df.to_string(index=False)
    else:
        try:
            chat_completion = client.chat.completions.create(
                model=modelos[0],  # Asegúrate de seleccionar el modelo correcto                      
                messages=[
                    {
                        "role": m["role"],
                        "content": m["content"]
                    }
                    for m in st.session_state.messages
                ], # Entregamos el historial de los mensajes para que el modelo tenga algo de memoria
                stream=True
            )  
            # Mostrar respuesta del asistente en el contenedor de mensajes de chat
            with st.chat_message("assistant"):            
                chat_responses_generator = generate_chat_responses(chat_completion)
                # Usamos st.write_stream para simular escritura
                full_response = st.write_stream(chat_responses_generator)                                    
            response_content = full_response
        except Exception as e: # Informamos si hay un error
            st.error(e)
            response_content = str(e)
    
    # Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant", "content": response_content})

