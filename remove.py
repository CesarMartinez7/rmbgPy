from rembg import remove
from PIL import Image
import io
import os
from time import sleep
from shutil import move
from pathlib import Path




def rmbBackground(input_path: str | bytes ,output_path: str = ""):
    try:
        with open(input_path,"rb") as img:
            img_data = img.read()
            resultado = remove(img_data)
            img_resultado = Image.open(io.BytesIO(resultado))
            if(len(output_path)<1):
                output = f"rb{input_path}"
                # breakpoint()
                return img_resultado.save(output),Path(output).stem
            else:
                return img_resultado.save(output_path)
    except Exception as e:
        print(f"Error en {e}")
        




def rmbBackgroundList(lista:list) -> None:
    for i in lista:
        rmbBackground(i)



def rmbDir(nameDir: str = "NotBackground") -> None:
    dir = os.listdir()
    extensiones = [".png",".jpg"]
    for file in dir:
        os.makedirs(nameDir,exist_ok=True)
        if os.path.splitext(file)[1] in extensiones :
            try:
                _,output = rmbBackground(file)
                # breakpoint()
                move(f"{output}{os.path.splitext(file)[1]}",nameDir)
            except Exception as e:
                raise("Error en la manipulacion de imagenes")
            finally:
                print(f"Fondo removido con exito en la imagen {file}. ;) ")
    

"""

***Funciones***
rmbBackground()
rmbBackgroundList()
rmbDir()


rmbBackground(): Toma dos argumentos el inputPath o el nombre del archivo y el outputpath, si no se pasa el output entonces este retornara el nombre del archivo con el mismo input pero con las siglas al comienzo de rb

rmbDir: Toma el directorio actual de los archivos con extensiones de imagen y las lista el modulo os y esta remueve el fondo de cada una de las imagenes y las ingresa a una carpeta llamada NotBackground que contiene las imagenes sin fondos, el dirName es la llamada o el nombre por default de la carpeta.

rmbBackgroundList(): Toma una lista de archivos que seran pasados como listas, estos archivos deben estar listado o en el directorio actual donde se ejecuta el script


Dependencias: 
rembg
pillow



Python Version: 3.11.0

"""
