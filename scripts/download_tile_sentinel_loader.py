from sentinelsat import SentinelAPI
from datetime import datetime
from datetime import timedelta
from shapely.geometry import Point, Polygon, mapping
from shapely.affinity import scale
import rasterio.features
import logging
from osgeo import ogr
from shapely.wkt import loads
import geopandas as gpd
import pandas as pd
import requests
import os
import re
import os.path
from osgeo import gdal
import hashlib
from PIL import Image
import uuid
import fiona
import numpy as np
import traceback
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path

from threebee.sentinel_loader import Sentinel2Loader

logging.basicConfig(level=logging.DEBUG)

load_dotenv()  # take environment variables from .env.

Path("sentinelcache").mkdir(parents=True, exist_ok=True)

sl = Sentinel2Loader(
    "sentinelcache",
    os.environ["COPERNICUS_USER"],
    os.environ["COPERNICUS_PASSWORD"],
    apiUrl="https://apihub.copernicus.eu/apihub/",
    showProgressbars=True,
)

# Define a region centered on the given coordinates and download the history data to cache
lat_center = 45.040048
lat_min = lat_center - 0.2
lat_max = lat_center + 0.2

long_center = 10.133250
long_min = long_center - 0.2
long_max = long_center + 0.2

area = Polygon(
    [
        (lat_max, long_min),
        (lat_min, long_min),
        (lat_min, long_max),
        (lat_max, long_max),
    ]
)

# Download region history
geoTiffs = sl.getRegionHistory(area, "NDVI", "60m", "2022-07-15", "2022-07-18", daysStep=1)
