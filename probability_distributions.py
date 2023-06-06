# For the following problems, use python to simulate the problem and calculate an experimental probability, then compare that to the theoretical probability.
#standard imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1:
# A bank found that the average number of cars waiting during the noon hour at a 
# drive-up window follows a Poisson distribution with a mean of 2 cars.
# Make a chart of this distribution and answer these questions concerning 
# the probability of cars waiting at the drive-up window.
stats.poisson
lamb = 2
car_distribution = stats.poisson(lamb)
x = np.arange(0,8)
y = [car_distribution.pmf(i) for i in x]
plt.bar(x,y)
plt.show

# What is the probability that no cars drive up in the noon hour?
car_distribution.pmf(0)
# ANSWER: approx: 13%

# What is the probability that 3 or more cars come through the drive through?
car_distribution.sf(2)
# ANSWER: approx: 32%

# How likely is it that the drive through gets at least 1 car?
car_distribution.sf(0)
# ANSWER: approx: 86%


# 2:
# Grades of State University graduates are normally distributed with a mean of 3.0 
# and a standard deviation of .3. Calculate the following:
avg = 3.0
stv = .3
grad_distro = stats.norm(avg, stv)
grad_distro

# What grade point average is required to be in the top 5% of the graduating class?
grad_distro.rvs(10_000) 
pd.Series(grad_distro.rvs(100_000)).plot.hist(bins=1000)
grad_distro.isf(.05)
# ANSWER: approx: 3.49 GPA

# What GPA constitutes the bottom 15% of the class?
grad_distro.isf(.85)
# or you can do:
grad_distro.ppf(.15)
# ANSWER: approx: 2.69 GPA


# An eccentric alumnus left scholarship money for students in the third decile 
# from the bottom of their class. Determine the range of the third decile. 
# Would a student with a 2.8 grade point average qualify for this scholarship?

#3rd decile from bottom:
grad_distro.ppf([0.2,0.3])
# 3rd decile from bottom: ANSWER: approx: 2.7 - 2.8 GPA, so a 2.8 qualifies
    
# If I have a GPA of 3.5, what percentile am I in?
grad_distro.sf(3.5)
# you are in the top 4-5%, so you are in the 95th percentile.


# 3.
# A marketing website has an average click-through rate of 2%. 
# One day they observe 4326 visitors and 97 click-throughs. 
# How likely is it that this many people or more click through?
avg_rate = .02
visitors = 4326
clicks = 97

stats.poisson
lamb = avg_rate * visitors
click_distro = stats.poisson(lamb)
x = np.arange(0,visitors + 1)
y = [click_distro.pmf(i) for i in x]
plt.bar(x,y)
plt.show
# what i think the answer is: 4%
# !!!!!!! the above is wrong and needing correcting


# 4.
# You are working on some statistics homework consisting of 100 questions where all 
# of the answers are a probability rounded to the hundreths place. 
# Looking to save time, you put down random probabilities as the answer to each 
# question.
# What is the probability that at least one of your first 60 answers is correct?
n = 60
p = .01
stats.binom(n, p).sf(0)
# 45%


# 5.
# The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when 
# they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 
# students visit the break area. How likely is it that the break area gets 
# cleaned up each day? How likely is it that it goes two days without getting 
# cleaned up? All week?
n = round(0.9*3*22)
p = .03
stats.binom(n, p).sf(0)
# 83%
stats.binom(n*2, p).pmf(0)
# approx 3% for 2 days
stats.binom(n*5, p).pmf(0)
# approx. .01% for 5 days


# 6.
# You want to get lunch at La Panaderia, but notice that the line is usually very 
# long at lunchtime. After several weeks of careful observation, you notice that 
# the average number of people in line when your lunch break starts is normally 
# distributed with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to 
# getting your food, what is the likelihood that you have at least 15 minutes left 
# to eat your food before you have to go back to class? Assume you have one hour 
# for lunch, and ignore travel time to and from La Panaderia.
mean = 15 * 2 # mean of 15 and 2 min per person
std = 3 * 2 # std of 3, per person so x2

stats.norm(mean, std).cdf(33) # 33 calculated from time it takes, because 
# 60min total, -15 for eat time, -10 for waiting for food, -2 for ordering time
# so 60- 15-10-2 = 33



# 7.
# Connect to the employees database and find the average salary of current employees, 
# along with the standard deviation. For the following questions, calculate the 
# answer based on modeling the employees salaries with a normal distribution 
# defined by the calculated mean and standard deviation then compare this answer 
# to the actual values present in the salaries dataset.
url = env.get_db_url('employees')
query = '''
SELECT *
FROM salaries s
WHERE s.to_date > NOW()
'''
salaries = pd.read_sql(query, url)

salaries
# What percent of employees earn less than 60,000?
mean = salaries.salary.mean()
sal_std = salaries.salary.std()
(mean, sal_std)

stats.norm(mean, sal_std).cdf(60_000)


# What percent of employees earn more than 95,000?
stats.norm(mean, sal_std).sf(95_000)


# What percent of employees earn between 65,000 and 80,000?
np.diff(stats.norm(μ, σ).cdf([65000, 80000]))


# What do the top 5% of employees make?
stats.norm(mean, sal_std).isf(0.05)
salaries.salary.quantile(0.95)


