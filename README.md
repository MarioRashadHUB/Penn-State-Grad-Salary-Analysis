![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/psu_logo.png "Experience with Excel")

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
I looked at the distributions of the data and the value counts for the various categorical variables. Below are one of the highlights. 

![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/exp_excel.png "Experience with Excel")

## Results
Here are some of the interesting statisitical results that I found from this analysis.

### Average salaries for each job title.
creative director - $111,886.

marketing director - $99,547.

marketing manager - $76,266.

event manager - $68,375.

content creation - $63,641.

brand manager - $62.928.

event coordinator - $62,729.

marketing coordinator - $60,873.

social media planner - $58,658.

brand ambassador - $42,684.

### Interesting Statistics
The creative director job position makes the most money with a average salary of $111,886.

Those who have experience in Microsoft Excel make 13% more in total salary.

Experience with adobe photoshop attributes to a 12% increase in total salary.

Those who have exoerience with adobe creative cloud make 16% more in total salary.

Across all job titles, the insurance sector has the best average salary of $87,655.

### Ranking of best 5 paying states across all job title average salaries:

1. Arkansas: $89,250
2. Kansas: $75,750
3. South Dakota: $74,500
4. Montana: $73,2500
5. Iowa: $73,071

### Top 5 cities with the most job postings:

1. New York City, NY: 127 Job postings
2. San Fransico, CA: 60 Job postings
3. Chicago, IL: 58 Job postings
4. Seattle, WA: 56 Job postings
5. Atlanta, GA: 45 Job postings

### Top 5 cities for each job

### Creative Director
1. MO	$184,000
2. TX	$140,400
3. IA	$138,250
4. WA	$138,250
5. NJ	$137,250

### Marketing Manager
1. IA	186.000000
2. MI	141.500000
3. MN	130.250000
4. SC	99.500000
5. CT	96.416667

### Brand Ambassador
1. KS	81.500000
2. AL	66.000000
3. OK	56.562500
4. KY	56.166667
5. IA	56.125000

### Marketing Coordinator
1. NM	99.000000
2. MO	94.666667
3. CT	85.500000
4. DC	82.800000
5. HI	80.500000

### Content Creation
1. OH	89.500000
2. CT	85.214286
3. TX	82.875000
4. VA	79.000000
5. MD	75.875000

### Event Coordinator
1. IA	94.000000
2. MI	89.500000
3. AL	82.500000
4. NH	77.500000
5. CO	75.666667

### Brand Manager
1. NY	157.000000
2. OH	126.500000
3. NM	86.500000
4. CO	83.125000
5. MO	70.750000

### Social Media Planner
1. WI	90.250000
2. NM	66.250000
3. NY	63.650000
4. GA	63.500000
5. CA	60.625000

### Event Manager
1. IL	122.500000
2. NY	91.600000
3. GA	86.666667
4. NJ	84.000000
5. OH	80.333333

### Marketing Director
1. UT	265.5000
2. OH	182.5000
3. FL	165.5000
4. IL	127.5000
5. MN	116.2500
