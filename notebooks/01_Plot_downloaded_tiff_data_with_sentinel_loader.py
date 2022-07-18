# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: threebee_venv
#     language: python
#     name: threebee_venv
# ---

# %% [markdown]
# # Plot downloaded tiff images

# %% [markdown]
# Plot the tiff images downloaded with the `download_tile_sentinel_loader.py` script in the `sentinelcache` gitignored folder.

# %% [markdown]
# ## Imports

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

# import threebee

pd.set_option('display.max_columns', None)

# %%
import pandas as pd
from IPython.display import display


def left_align(df: pd.DataFrame):
    """Set the input dataframe to have its text cells all left aligned."""
    left_aligned_df = df.style.set_properties(
        **{"text-align": "left", "vertical-align": "top"}
    )
    left_aligned_df = left_aligned_df.set_table_styles(
        [dict(selector="th", props=[("text-align", "left"), ("vertical-align", "top")])]
    )
    return left_aligned_df


def display_full(df: pd.DataFrame):
    """Display an input dataframe by showing all of the cells content, and
    with left alignment of the cells."""

    with pd.option_context(
        "display.max_rows",
        None,
        "display.max_columns",
        None,
        "display.max_colwidth",
        None,
    ):
        display(left_align(df))


# %% [markdown]
# ## Plot the downloaded image of 2022/07/16

# %% [markdown]
# Open metadata csv

# %%
path_to_csv = (
    "../sentinelcache/apiquery/"
    + "Sentinel-2-S2MSI2A-224aa7cd048db6785866f6e8c60e9d2d-20220712-20220717-0-80.csv"
)

df_query = pd.read_csv(path_to_csv)

# %%
display_full(df_query)

# %% [markdown]
# Load the data and show the result

# %%
path_to_tiff = (
    "../sentinelcache/tmp/"
    + "2022-07-18-NDVI-60m-50678036e5ba43459b78898fe0ac309c.tiff"
)


# %%
img = rasterio.open(path_to_tiff)

lat_center = 45.040048
long_center = 10.133250

plt.figure(figsize=(12,12))
plt.title(f"NDVI index centered at ({lat_center}, {long_center}), on the 2022-07-18")
show(img)
plt.savefig("2022_07_18_ndvi_index.png")
plt.show()

# %%

# %% [markdown]
# ## Notes

# %% [markdown]
# The NDVI index has been calculated from the `04` and `08` bands as such:
#
# $$ ndvi = (nir - red) / (nir + red) $$

# %%
