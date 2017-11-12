# Pygoim
Pequeño modulo desarrollado en python para descarga de imagenes utilizando el motor de Google

El modulo solo ha sido probado en Linux.

## Requerimientos
Para que Pygoim funcione correctamente necesita los siguientes modulos.

pycurl <br />
beautifulsoup4

## Uso
```
from pygoim import Pygoim

pygoim_ = Pygoim()

# Descargar el documento html de google
html_doc = pygoim_.download_page(search)

# Obtener arreglo de diccionarios
img_list = pygoim_.image_tracker(html_doc)

for img_dict in img_list:
  pygoim_.download_image(img_dict, '/path/to/save/image')

```

## Función .download_page(search, size=None, color=None, type_=None, cpr=Non)
1. search: texto de busqueda
2. size: texto indicando el tamaño de las imagenes.
  - lg
  - md
  - sm
  - tamaño personalizado, ejemplo: pygoim_.download_page(search, '400x900')
3. color: Filtrar busqueda por color de imagenes.
  - all (a todo color)
  - gs (blanco y negro)
  - png (transparentes)
  - Otro tipos: red, orange, yellow, green, teal, blue, purple, pink, white, gray, black or brown
4. type_: Tipos de imagenes.
  - face
  - photo
  - clipart
  - lineart
  - animated
5. cpr: Filtrar imagenes por licencias.
  - fmc (etiquetadas para reutilización con modificaciones)
  - fc (etiquetadas para reutilización)
  - fm (etiquetadas para reutilización no comercial con modificaciones)
  - f (etiquetadas para reutilización no comercial)

## Función .image_tracker(html_doc)
La función recibe un texto con la estructura de un documento HTML5 buscara hasta un maximo de 100 url's. Pueden darse los casos en que la función encuentre menos de 100 imágenes.<br /><br />

## Funcion .download_image(img_dict, dest)
Esta función recibe un diccionario como el siguiente:
```
{
  'img_url': 'https://url/to/image',
  'img_type': 'jpg'
}
```
Y la dirección local donde se guardara la imágen.

## Bugs
Hasta el momento el unico bug del que puedo informar es que, algunas de las imágenes que se descargan no pueden ser leídas.
