# rmbgPy 🐍📷

Este script contiene funciones para eliminar el fondo de imágenes utilizando Python. Las funciones están diseñadas para trabajar con archivos de imagen en el directorio actual y permiten procesar imágenes de forma individual o en lotes. Se utilizan las bibliotecas `rembg` y `Pillow` para realizar la eliminación de fondos de manera eficiente.

## Funciones

### rmbBackground()
Toma dos argumentos: el `inputPath` o el nombre del archivo y el `outputPath`. Si no se pasa el output, entonces este retornará el nombre del archivo con el mismo input pero con las siglas al comienzo de `rb`.

### rmbDir()
Toma el directorio actual de los archivos con extensiones de imagen y los lista usando el módulo `os`. Esta función remueve el fondo de cada una de las imágenes y las ingresa a una carpeta llamada `NotBackground`, que contiene las imágenes sin fondos. El `dirName` es la llamada o el nombre por defecto de la carpeta.

### rmbBackgroundList()
Toma una lista de archivos que serán pasados como listas. Estos archivos deben estar listados o en el directorio actual donde se ejecuta el script.

## Dependencias
- `rembg`
- `pillow`

## Versión de Python
Python 3.11.0



## GoodBye👋
