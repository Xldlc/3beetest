# 3bee test
Test to analyse the data for 3bee. 

## Test requirements
Here are the requirements for the test:

1. Scaricare l'ultimo Tile disponibile senza copertura Nuvolosa, che contiene la posizione 45.040048, 10.133250, da Sentinel 2. Usare API. 
 
2. Creare una mappa con l'indice vegetativo e stamparla in PNG. 
 
3. Che tipologia di Database utilizzeresti per salvare questi Tile? 
 
4. In che modo potresti filtrare velocemente i Tile che hanno le nuvole.


## Install package threebee
To install the python package `threebee` contained in this repository, after cloning this repo run:

```bash
make virtualenv  # create the python venv from requirements-text.txt and install the threbee package
```

## Usage package threebee
To download the data from Sentinel 2, firts provide an `.env` file in the root of the repo with the
user credentials for the Copernicus HUB (https://scihub.copernicus.eu), and then run

```bash
source .venv/bin/activate
python scripts/download_tile_sentinel_loader.py
```

This will download the data to calculate the NDVI index, with a resolution of 60m, from 2022-07-15
to 2022-07-18.

## Solutions to the given questions
1. The data has been downloaded locally in the `sentinelcache` folder,
 using the `download_tile_sentinel_loader.py` script.

2. The map of the NDVI index has been saved in the `notebooks` folder.

3. In order to store these Tile files, I would store them on a cloud service that is appropriate for 
saving and retrieving big files (e.g. AWS S3), and at the same time I would save the metadata related
to the Tiles in a SQL or NoSQL database. This would require some coordination between the two resources
(the storage resourse and the database resourse) but it would be faster and more efficient then saving
the raw data directly onto a database.

4. Among the metadata related to each file there is the `cloudcoverpercentage`, as shown in the 
`notebooks/01_Plot_downloaded_tiff_data_with_sentinel_loader.ipynb` notebook which displays the downloaded
metadata for each API query. Before downloading the images, I would filter the ones where the 
cloudcoveragepercentage is lower than a certain threshold to be sure to have images with less
cloud coverage.