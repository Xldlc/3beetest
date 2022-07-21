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
# # Plot and save images of the Po river

# %% [markdown]
# Plot and save images to make a gif

# %% [markdown]
# ## Imports

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
from pathlib import Path
import shapely.wkt

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
# Get all csv paths
path_to_apiquery = (
    "../sentinelcache/apiquery/"
)
files = Path(path_to_apiquery).glob('*.csv') # get all csvs in your dir.
all_dfs = [pd.read_csv(file,index_col = 0) for file in files]
df_csvs = pd.concat(all_dfs)

# Get all tiff paths
path_to_tiffs = (
    "../sentinelcache/products/"
)
tiffs10m = Path(path_to_tiffs).rglob('*10m.tiff')
df_tiffs = pd.DataFrame({"path" : tiffs10m})
df_tiffs["uuid"] = df_tiffs["path"].apply(lambda x: x.parent.name)

# Merge the info
df_all = pd.merge(df_csvs, df_tiffs, how="left", on="uuid")
df_all.drop_duplicates(inplace=True)

# %%
df_all

# %% [markdown]
# Select one area

# %%
# Cycle over all of the polygons ( by hand )
footprint = df_all["footprint"].unique()[3]

df_sel = df_all[df_all["footprint"] == footprint]
df_sel = df_sel.sort_values("generationdate", ascending=True)
display(df_sel)

# Check the polygon centroid
P = shapely.wkt.loads(footprint)
center = P.centroid.wkt
center = center.replace("POINT ", "")
center = center.replace("(", "")
center = center.replace(")", "")
center = center.replace(" ", "_")
print(f"images_{center}")

Path(f"images_{center}_cropped").mkdir(parents=True, exist_ok=True)

for indx, row in df_sel.iterrows():

    path_to_tiff = row["path"]
    # print(path_to_tiff)
    date = row["generationdate"]
    date_str = date.replace(" ", "_").replace(":", "_")

    if pd.notnull(path_to_tiff):

        img = rasterio.open(path_to_tiff)
        img_data = img.read()[0]

        if footprint == df_all["footprint"].unique()[3]:
            # Crop data
            img_data = img_data[200:3000, :]
            plt.figure(figsize=(20, 6))
        else:
            plt.figure(figsize=(20,20))
        # plt.title(f"Date: {date}")
        plt.imshow(img_data, cmap="twilight", vmin=800, vmax=16000)
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(f"images_{center}_cropped/{date_str}.png", dpi=200)
        print(f"images_{center}/{date_str}.png")
        # plt.colorbar()
        plt.close("all")
