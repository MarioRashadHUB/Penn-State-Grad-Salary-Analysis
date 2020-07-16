![alt text](https://github.com/MarioRashadHUB/comm_salary_proj/blob/master/images/psu_logo.png "Experience with Excel")

# Penn State Graduate Salary Analysis: Project Overview
* Preformed a salary analysis for common job titles that graduates from the Pennsylvania State University College of Communications recieve to aid in salary negotations and relocation depending on the job that be being seeked by the student.
* Scraped over 2000 job descriptions from glassdoor using python and selenium
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
creative director:      $111,886.

marketing director:     $99,547.

marketing manager:      $76,266.

event manager:          $68,375.

content creation:       $63,641.

brand manager:          $62.928.

event coordinator:      $62,729.

marketing coordinator:  $60,873.

social media planner:   $58,658.

brand ambassador:       $42,684.

### Interesting Statistics
The creative director job position makes the most money with a average salary of $111,886.

Those who have experience in Microsoft Excel make 13% more in total salary.

Experience with adobe photoshop attributes to a 12% increase in total salary.

Those who have exoerience with adobe creative cloud make 16% more in total salary.

Across all job titles, the insurance sector has the best average salary of $87,655.

### My Favorite Fact from Analysis:
Hawaii is the #5 best paying state for Marketing Coordinators with a average salary of $80,500.

### Top 5 cities with the most job postings:

1. New York City, NY: 127 job postings.
2. San Fransico, CA: 60 job postings.
3. Chicago, IL: 58 job postings.
4. Seattle, WA: 56 job postings.
5. Atlanta, GA: 45 job postings.

### Ranking of best 5 paying states across all job title average salaries:

1. Arkansas: $89,250.
2. Kansas: $75,750.
3. South Dakota: $74,500.
4. Montana: $73,2500.
5. Iowa: $73,071.

### Top 5 states for each job:

### Creative Director
1. Montana:    $184,000.
2. Texas:      $140,400.
3. Iowa:       $138,250.
4. Washington:	$138,250.
5. New Jersey: $137,250.

### Marketing Manager
1. Iowa:             $186,000.
2. Michigan:         $141,500.
3. Minnesota:        $130,250.
4. South Carolina:   $99,500.
5. Connecticut:      $96,416.

### Brand Ambassador
1. Kansas:     $81,500.
2. Alabama:	   $66,000.
3. Oklahoma:   $56,562.
4. Kentucky:	$56,166.
5. Iowa:       $56,125.

### Marketing Coordinator
1. New Mexico:       $99,999.
2. Montana: 	      $94,966.
3. Connecticut:	   $85,500.
4. Washington D.C:   $82,800.
5. Hawaii:        	$80,500.

### Content Creation
1. Ohio:	         $89,500.
2. Connecticut:	$85,214.
3. Texas:      	$82,875.
4. Virginia:	   $79,000.
5. Maryland:	   $75,875.

### Event Coordinator
1. Iowa: 	      $94,000.
2. Michigan:	   $89,500.
3. Alabama:    	$82,500.
4. New Hampshire:	$77,500.
5. Colorado:   	$75,666.

### Brand Manager
1. New York:	$157,000.
2. Ohio:	      $126,500.
3. New Mexico:	$86,500.
4. Colorado:	$83,125.
5. Montana:	   $70,750.

### Social Media Planner
1. Wisconsin:	$90,250.
2. New Mexico:	$66,250.
3. New York:	$63,650.
4. Georgia:	   $63,500.
5. California:	$60,625.

### Event Manager
1. Illinois:	$122,500.
2. New York:	$91,600.
3. Georgia:	   $86,666.
4. New Jersey:	$84,000.
5. Ohio:	      $80,333.

### Marketing Director
1. Utah:       $265,500.
2. Ohio:       $182,500.
3. Florida:	   $165,500.
4. Illinois:	$127,500.
5. Minnesota:	$116,250.
