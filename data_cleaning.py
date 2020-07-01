#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:25:47 2020

@author: Mario
"""

import pandas as pd

def title_simplifier(title):
    if 'ambassador' in title.lower():
        return 'brand ambassador'
    elif 'representative' in title.lower():
        return 'brand ambassador'
    elif 'brand manager' in title.lower():
        return 'brand manager'
    elif 'creative director' in title.lower():
        return 'creative director'
    elif 'marketing manager' in title.lower():
        return 'marketing manager'
    elif 'marketing director' in title.lower():
        return 'marketing director'
    elif 'marketing coordinator' in title.lower():
        return 'marketing coordinator'
    elif 'event manager' in title.lower():
        return 'event manager'
    elif 'event coordinator' in title.lower():
        return 'event coordinator'
    elif 'content' in title.lower():
        return 'content creation'
    elif 'social media' in title.lower():
        return 'social media planner'
    elif 'creative director' in title.lower():
        return 'creative director'
    else:
        return 'na'

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

df = pd.read_csv('glassdoor_jobs_combined_unclean.csv')

# decreased dataframe size by 18% by removing all duplicated rows.
df.drop_duplicates(keep=False, inplace=True)

# removes all rows that do not have the State and City listed
df = df[df['Salary Estimate'] != '-1']
df = df[df['Location'] != 'Remote']
df = df[df['Location'] != 'United States']

df['comma'] = df['Location'].apply(lambda x: 1 if ',' in x.lower() else 0)
df = df[df['comma'] != 0]

# removes all part time positions
df['part_time'] = df['Job Description'].apply(lambda x: 1 if 'part time' in x.lower() else 0)
df.part_time.value_counts()
df = df[df['part_time'] != 1]

df['part_time_still'] = df['Job Title'].apply(lambda x: 1 if 'part time' in x.lower() or 'part-time' in x.lower()else 0)
df.part_time_still.value_counts()
df = df[df['part_time_still'] != 1]

# simplifies job titles
df['job_simp'] = df['Job Title'].apply(title_simplifier)
df = df[df['job_simp'] != 'na']

df.job_simp.value_counts()


#fix rating
df['Rating'] = df['Rating'].clip(lower = 0)

# Salary Parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

#fixes entries that do not have only state listed
df['job_state'] = df.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'orange' else 'NJ')
df['job_state'] = df.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'pinellas' else 'FL')
df['job_state'] = df.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'Cuyahoga' else 'OH')

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

# parsing of job description

df['Job Title'].value_counts(5)
#Microsoft Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

#Micrsoft Powerpoint
df['powerpoint_yn'] = df['Job Description'].apply(lambda x: 1 if 'powerpoint' in x.lower() else 0)
df.powerpoint_yn.value_counts()

#Microsoft Office
df['micro_office_yn'] = df['Job Description'].apply(lambda x: 1 if 'microsoft office' in x.lower() else 0)
df.micro_office_yn.value_counts()

#Analytics 
df['analytics_yn'] = df['Job Description'].apply(lambda x: 1 if 'analytics' in x.lower() or 'analytic' in x.lower() else 0)
df.analytics_yn.value_counts()

#Photoshop
df['photoshop_yn'] = df['Job Description'].apply(lambda x: 1 if 'photoshop' in x.lower() else 0)
df.photoshop_yn.value_counts()

#Adobe Products
df['adobe_yn'] = df['Job Description'].apply(lambda x: 1 if 'adobe' in x.lower() else 0)
df.adobe_yn.value_counts()

#Adwords
df['adwords_yn'] = df['Job Description'].apply(lambda x: 1 if 'adwords' in x.lower() or 'ad words' in x.lower() else 0)
df.adwords_yn.value_counts()




df.to_csv('comm_data_cleaned.csv',index = False)


'''
### july 1st 2020, updating data_cleaned file so it has changes made from jupyter notebook file ###


df = pd.read_csv('comm_data_cleaned.csv')

# Converts all negative values in 'Rating' column to 0.0
df['Rating'] = df['Rating'].clip(lower = 0)

# Removes unecessary columns
df = df.drop(['comma', 'part_time', 'part_time_still'], axis=1)

# hourly wage to annual 
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly ==1 else x.min_salary, axis =1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly ==1 else x.max_salary, axis =1)

# Add's 0's to all min and max salaries 
df['min_salary'] = df.apply(lambda x: x.min_salary*1000, axis =1)
df['max_salary'] = df.apply(lambda x: x.max_salary*1000, axis =1)

df.to_csv('comm_data_cleaned.csv',index = False)
'''

