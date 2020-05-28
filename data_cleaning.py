#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:25:47 2020

@author: Mario
"""

import pandas as pd

# Imports all scrapped dataframes and combines them all into one large dataframe
df_brand_amb = pd.read_csv('glassdoor_jobs_brand_amb.csv')
df_brand_mnger = pd.read_csv('glassdoor_jobs_brand_mngr.csv')
df_exp_market = pd.read_csv('glassdoor_jobs_exp_market.csv')
df_mark_dir = pd.read_csv('glassdoor_jobs_mark_dir.csv')
df_create_dir = pd.read_csv('glassdoor_jobs_create_dir.csv')
df_social_media = pd.read_csv('glassdoor_jobs_social_media.csv')
df_content_creation = pd.read_csv('glassdoor_jobs_content_creation.csv')

df_combined = pd.concat([df_brand_amb, df_brand_mnger, df_exp_market, df_mark_dir, df_create_dir, df_social_media, df_content_creation], ignore_index=True)

df_combined.to_csv('glassdoor_jobs_combined_unclean.csv',index = False)

df_combined = pd.read_csv('glassdoor_jobs_combined_unclean.csv')