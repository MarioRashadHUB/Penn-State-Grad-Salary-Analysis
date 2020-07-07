# Penn State Graduate Salary Analysis: Project Overview
* Preformed a salary analysis for common job titles that graduates from the Pennsylvania State University College of Communications recieve to aid in salary negotations and relocation depending on the job that be being seeked by the student.
* Scraped over 7000 job descriptions from glassdoor using python and selenium
* Engineered features from each glassdoor job description to quantify and observe the value companies put on excel, powerpoint, microsoft office, analytics, photoshop, adobe, and adwords.

## Code and Resources Used 
**Python Version:** 3.7

**Packages:** pandas, matplotlib, seaborn, selenium

**Ken Jee's Data Science Project from Scratch Series:**  https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium

**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

## Data
Tweaked the web scraper github repo (above) to scrape 7000 job postings from glassdoor.com. With each job, I got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
The following changes were made and created the following variables before I could preform my analysis:

*	Parsed numeric data out of salary 
*	Made columns for employer provided salary and hourly wages 
*	Removed rows without salary 
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Excel  
    * Powerpoint  
    * Microsoft Office  
    * Analytics  
    * Photoshop
    * Adobe
    * Adwords
*	Column for simplified job title
*	Column for description length 

## Exploratory Data Analysis
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/exp_adobe.png "Experience with Adobe Cloud")
![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/img1.png "Average Salary by title")
![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/exp_excel.png "Experience with Excel")
