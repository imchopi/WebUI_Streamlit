# Generador de Imágenes con Stable Diffusion Web UI

## Colaboradores
- **Adrián Perogil Fernández** - [GitHub](https://github.com/imchopi)
- **Jesús Ruiz Toledo** - [GitHub](https://github.com/jesusruiztoledo)

## Enlace
- **[Web de Streamlit](https://apf-jrt-webui.streamlit.app/)**

## Descripción
Este proyecto es una aplicación web desarrollada en Streamlit que permite generar imágenes a partir de descripciones de texto utilizando la API de **Stable Diffusion Web UI**. El usuario puede personalizar diferentes parámetros el número de pasos y la escala CFG.

## Modelo Utilizado
- **Nombre del Modelo:** 2D Game Icon Sill Equipment
- **Fuente:** [CivitAI](https://civitai.com/models/75116/2d-game-icon-sill-equipment)
- **Tipo:** Generación de imágenes para íconos de juegos en 2D
- **Formato:** `.ckpt`

## Características Principales
- **Interfaz web interactiva:** Permite la configuración de la generación mediante controles deslizantes.
- **Personalización de los prompts:** El usuario puede escribir una descripción detallada de la imagen que desea generar.
- **Ajustes avanzados:** Se pueden modificar parámetros como número de pasos y escala CFG.
- **Integración con la API de Stable Diffusion Web UI:** Utiliza peticiones HTTP para comunicarse con el backend de Stable Diffusion.

## Instalación y Configuración
### Requisitos previos
- Python 3. 10
- Dependencias instaladas:
  ```bash
  pip install -r requirements.txt
  ```
- Tener **Stable Diffusion Web UI (AUTOMATIC1111)** instalado y corriendo con la API activada:
  ```bash
  webui-user.bat --api  # En Windows
  ./webui.sh --api       # En Linux/Mac
  ```
- En el caso de que no funcione, asegurarse que en el archivo `webui-user.bat` esté implementada la opción --api como parámetros predeterminados.

### Descarga del repositorio
```bash
git clone https://github.com/imchopi/WebUI_Streamlit.git
cd WebUI_Streamlit
```

### Ejecución de la aplicación
```bash
streamlit run streamlit_app.py
```

## Uso
0. **[Web de Streamlit](https://apf-jrt-webui.streamlit.app/)**
1. Escribe un prompt en el cuadro de texto.
2. Ajusta los parámetros según tus necesidades (número de pasos y escala CFG).
3. Haz clic en el botón "Generar Imagen".
4. La imagen generada se mostrará en la pantalla y podrás descargarla.

## Captura de Pantalla
<img src="/img/preview_image.png">
<img src="/img/example2.jpg">
<img src="/img/example3.jpg">

## Estructura del Proyecto
```
/
├── streamlit_app.py        # Código principal de la aplicación en Streamlit
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias necesarias
├── img                     # Carpeta con imagen para el readme
```
