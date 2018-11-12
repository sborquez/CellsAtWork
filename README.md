# Aplicación de modelos de clasificación para la identificación de células sanguíneas

Integrantes:
* Sebastián Bórquez González [:e-mail:](mailto:sebastian.borquez@sansano.usm.cl)
* Pablo Flores Repetto [:e-mail:](mailto:pablo.floresre@sansano.usm.cl)
* John Rodriguez Mora [:e-mail:](mailto:john.rodriguez@sansano.usm.cl)

## Objetivo

Aplicar modelos de clasificación de objetos para la detección y clasificación de eritrocitos, leucocitos y trombocitos en imágenes sanguíneas para la facilitación del conteo de células y/o detección de enfermedades.

## Descripción

El ser humano adulto posee más de 5 litros de sangre en promedio y existen una variedad de problemas y enfermedades relacionados con su composición. Las células sanguíneas pueden presentar deformidades, signos de enfermedades como cáncer o células falciformes. Por otro lado, anomalías  en las proporciones de la cantidad de los subtipos de células sanguíneas, ya sea un bajo conteo de glóbulos rojos (eritrocitos), signos de anemia, o un gran número de glóbulos blancos (leucocitos) es una señal de la Leucemia.

 Un problema importante en el diagnóstico de la sangre es la clasificación y conteo de las diferentes subtipos de células sanguíneas que la componen, nuestro proyecto busca la automatización de este proceso a través de métodos de computer vision.

Para nuestra investigación tendremos a disposición la base de datos [BCCD](https://github.com/Shenggan/BCCD_Dataset), un dataset de 12,500 imágenes de células sanguíneas acompañadas de etiquetas de 4 diferentes tipos de células. El dataset se encuentra disponible al público bajo la licencia MIT.

Tomaremos el trabajo previo realizado por [Paul Mooney](https://www.kaggle.com/paultimothymooney/identify-blood-cell-subtypes-from-images/notebook) como referencia base para  nuestro proyecto de investigación.

## Caracteristicas

En este repositorio encontrarás los diferentes notebook y scripts de python utilizados a lo  largo de nuestra investigación, a continuación se presenta un índice del repositorio.

### Indice

```
CellsAtWork
│   README.md  
│
└───data
│   │   prepare_data.py
│   │
│   └───datasets
│       └───train
│       │   
│       └───test
│   
└───notebooks
        Visualize.ipynb
        Yolo.ipynb
        Retinanet.ipynb
```

* __data__: Contiene los datasets y el script _prepare_data.py_. Este script utiliza el dataset original de BCCD para generar los datasets que se utilizarán para el entrenamiento y test.

* __notebooks__: Contiene los notebooks que se utilizarán para la visualización de las imágenes y el entrenamiento de cada técnica.

## Requisitos

Para la ejecución local del repositorio se necesitan los siguientes modulos especificados en _enviroment.yml_.

Puedes instalar los requisitos con:

```
conda env create -f environment.yml
```

En resumen, se necesita _python3, tensorflow, keras, sklearn, pandas, numpy, matplotlib_

Además es necesario instalar _keras-RetinaNet_ desde este [repositorio](https://github.com/fizyr/keras-retinanet).

Finalmente, se requiere del datasets [BCCD](https://github.com/Shenggan/BCCD_Dataset). Una vez descargado utilizar el script _data/prepare_data.py_ para crear el dataset para los modelos usados en este repositorio.