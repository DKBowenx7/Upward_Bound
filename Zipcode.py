# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:24:15 2023

@author: dkbow
"""

import geopandas as gpd
import matplotlib.pyplot as plt

#%%

#Getting the Onondaga County zip codes

plt.rcParams["figure.dpi"] = 300


zips = gpd.read_file("cb_2020_us_zcta520_500k.zip")

county = gpd.read_file("Census_Block_Groups_in_Syracuse%2C_NY_(2010).zip")


utm18n = 26918

zips = zips.to_crs(epsg=utm18n)

county = county.to_crs(epsg=utm18n)

border = county.dissolve()

syr_zips = zips.overlay(border[["geometry"]],keep_geom_type=True)


syr_zips.to_file("Onondaga_zips.gpkg",layer = "zips")










