# Generador de Imágenes con Stable Diffusion Web UI

<img src="" />


## Colaboradores
- **Adrián Perogil Fernández**
- **Jesús Ruiz Toledo**

## Descripción
Este proyecto es una aplicación web desarrollada en Streamlit que permite generar imágenes a partir de descripciones de texto utilizando la API de **Stable Diffusion Web UI**. El usuario puede personalizar diferentes parámetros como el modelo, el número de pasos, la escala CFG, el tamaño de la imagen y el sampler utilizado.

## Modelo Utilizado
- **Nombre del Modelo:** Anything V5
- **Fuente:** [CivitAI](https://civitai.com/) / [Hugging Face](https://huggingface.co/ckpt/anything-v5.0)
- **Tipo:** Generación de imágenes en estilo anime
- **Formato:** `.safetensors`

## Características Principales
- **Interfaz web interactiva:** Permite la configuración de la generación mediante menús desplegables y controles deslizantes.
- **Personalización de los prompts:** El usuario puede escribir una descripción detallada de la imagen que desea generar.
- **Ajustes avanzados:** Se pueden modificar parámetros como el sampler, número de pasos, escala CFG, ancho y alto de la imagen.
- **Integración con la API de Stable Diffusion Web UI:** Utiliza peticiones HTTP para comunicarse con el backend de Stable Diffusion.

## Instalación y Configuración
### Requisitos previos
- Python 3.10
- Dependencias instaladas:
  ```bash
  pip install streamlit requests pillow
  ```
- Tener **Stable Diffusion Web UI (AUTOMATIC1111)** instalado y corriendo con la API activada:
  ```bash
  webui-user.bat --api  # En Windows
  ./webui.sh --api       # En Linux/Mac
  ```

### Descarga del repositorio
```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
```

### Ejecución de la aplicación
```bash
streamlit run streamlit_app.py
```

## Uso
1. Escribe un prompt en el cuadro de texto.
2. Ajusta los parámetros según tus necesidades (número de pasos, sampler, tamaño de la imagen, etc.).
3. Haz clic en el botón "Generar Imagen".
4. La imagen generada se mostrará en la pantalla y podrás descargarla.

## Capturas de Pantalla
(Añadir capturas de la aplicación en funcionamiento)

## Estructura del Proyecto
```
/
├── streamlit_app.py        # Código principal de la aplicación en Streamlit
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias necesarias
├── assets/                 # Carpeta con ejemplos de imágenes generadas
```