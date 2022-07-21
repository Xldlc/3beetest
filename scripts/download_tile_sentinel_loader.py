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
# lat_center = 45.040048
lat_min = 44.94
lat_max = 45.16

# long_center = 10.133250
long_min = 9.13
long_max = 10.49

area = Polygon(
    [
        (long_max, lat_min),
        (long_min, lat_min),
        (long_min, lat_max),
        (long_max, lat_max),
    ]
)

# Download region history
geoTiffs = sl.getRegionHistory(area, "NDVI", "60m", "2022-04-01", "2022-07-20", daysStep=1)
