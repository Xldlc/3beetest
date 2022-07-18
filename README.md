# 3bee test
Test to analyse the data for 3bee. 

Here are the requirements for the test:

1. Scaricare l'ultimo Tile disponibile senza copertura Nuvolosa, che contiene la posizione 45.040048, 10.133250, da Sentinel 2. Usare API. 
 
2. Creare una mappa con l'indice vegetativo e stamparla in PNG. 
 
3. Che tipologia di Database utilizzeresti per salvare questi Tile? 
 
4. In che modo potresti filtrare velocemente i Tile che hanno le nuvole.


## Install
To install the python package `threebee` contained in this repository, after cloning this repo run:

```bash
make virtualenv  # create the python venv from requirements-text.txt and install the threbee package
```




## Usage

```py
from threebee import BaseClass
from threebee import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m threebee
#or
$ threebee
```