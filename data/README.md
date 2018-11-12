# Preparar el DataSet

Antes de ejecutar cualquier modelo es necesario tener los datos que vamos utilizar, para esto necesitas realizar los siguientes pasos.

1. Descargar el dataset BCCD desde este [repositorio](https://github.com/Shenggan/BCCD_Dataset).

2. Ejecutar _prepare_data.py_ dandole como argumento la ruta del dataset descargado.

```
python prepare_data.py ruta/a/la/carpeta/BCCD
```

Como resultado se tendrá una carpeta con las imágenes y csv necesarios.

__Advertencia__, se debe ejecutar el script desde este directorio, además el argumento debe ser una dirección absoluta.