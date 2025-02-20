import base64
import requests
import streamlit as st
from PIL import Image
from io import BytesIO

# Configurar la UI en Streamlit
st.title("Generador de Imágenes con Stable Diffusion")
prompt = st.text_input("Describe la imagen que deseas generar:", "un paisaje futurista con neón")
steps = st.slider("Número de pasos", min_value=10, max_value=50, value=20)
cfg_scale = st.slider("CFG Scale", min_value=1, max_value=20, value=7)

# Botón para generar la imagen
if st.button("Generar Imagen"):
    # Llamada a la API de Stable Diffusion
    url = "http://127.0.0.1:7860/sdapi/v1/txt2img"
    payload = {
        "prompt": prompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": 512,
        "height": 512
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "images" in data and len(data["images"]) > 0:
                image_data = base64.b64decode(data["images"][0])
                image = Image.open(BytesIO(image_data))
                st.image(image, caption="Imagen Generada", use_container_width=True)  # Cambio aquí
            else:
                st.error("No se recibió ninguna imagen en la respuesta.")
        else:
            st.error(f"Error en la generación de la imagen. Código de estado: {response.status_code}")
    except Exception as e:
        st.error(f"Ocurrió un error: {str(e)}")
