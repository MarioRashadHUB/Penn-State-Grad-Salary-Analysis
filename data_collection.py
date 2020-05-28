#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:21:15 2020

@author: Mario
"""


import glassdoor_scraper as gs
import pandas as pd
path = "/Users/mtss/Documents/comm_salary_proj/chromedriver"

# Scrapes 1000 job listings for each title from glassdoor and saves them to dataframes
df_brand_amb = gs.get_jobs('brand ambassador', 1000, False, path, 15)
df_brand_mnger = gs.get_jobs('brand manager', 1000, False, path, 15)
df_exp_market = gs.get_jobs('experiential marketing', 1000, False, path, 15)
df_mark_dir = gs.get_jobs('Marketing director', 1000, False, path, 15)
df_create_dir = gs.get_jobs('creative director', 1000, False, path, 15)
df_social_media = gs.get_jobs('social media', 1000, False, path, 15)
df_content_creation = gs.get_jobs('content creation', 1000, False, path, 15)

# Stores all dataframes into .CSV files
df_brand_amb.to_csv('glassdoor_jobs_brand_amb.csv',index = False)
df_brand_mnger.to_csv('glassdoor_jobs_brand_mngr.csv',index = False)
df_exp_market.to_csv('glassdoor_jobs_exp_market.csv',index = False)
df_mark_dir.to_csv('glassdoor_jobs_mark_dir.csv',index = False)
df_create_dir.to_csv('glassdoor_jobs_create_dir.csv',index = False)
df_social_media.to_csv('glassdoor_jobs_social_media.csv',index = False)
df_content_creation.to_csv('glassdoor_jobs_content_creation.csv',index = False)

















