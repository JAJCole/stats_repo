import numpy as np
import pandas as pd

np.random.seed(123)

# How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 10_000
n_dice = ncols = 2

rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(nrows, ncols)
# convert above to dataframe
rolls = pd.DataFrame(rolls)
# now you can access index 
likelihood = rolls.apply(lambda row: row[0] == row[1], axis=1).mean()
likelihood

#


# If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?
outcome = ['H', 'T']
n_coins = 8
n_sim = 100_000

coin_flips = np.random.choice(outcome, (n_sim, n_coins))
coin_flips = pd.DataFrame(coin_flips)
likelihood = coin_flips.apply(lambda row: row == 'H', axis=1)
head_3_count = likelihood[likelihood.sum(axis=1) == 3].shape[0]

prob = head_3_count/n_sim
prob

more_head_3_count = likelihood[likelihood.sum(axis=1) >= 3].shape[0]
prob_x = more_head_3_count/n_sim

prob_x


# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards 
# I drive past both have data science students on them?
#wd_prob = 3/4
#ds_prob = 1/4
n_sim = 100_000
n_bill = 2

options = ['WD','DS','WD','WD'] # manually put options for probability of outcome

bill_prob = np.random.choice(options, (n_sim, n_bill))
bill_prob = pd.DataFrame(bill_prob)
bill_prob

likelihood_bill = bill_prob.apply(lambda row: row == 'DS', axis=1)
ds_bill_count = likelihood_bill[likelihood_bill.sum(axis=1) == 2].shape[0]

ds_prob_x = ds_bill_count/n_sim

ds_prob_x


# Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts 
# on Friday afternoon? (Remember, if you have mean and standard deviation, use the np.random.normal) 
# You'll need to make a judgement call on how to handle some of your values
pop_avg = 3
pop_std = 1.5
n_days =5
n_trials = 10_000

consumed = np.random.normal(pop_avg, pop_std, (n_trials, n_days))
consumed

prob_consumed = (consumed.sum(axis=1)< 17).mean()


# Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# Since you have means and standard deviations, you can use np.random.normal to generate observations.
# If a man and woman are chosen at random, what is the likelihood the woman is taller than the man?
men_avg = 108
men_std = 8
women_avg = 170
women_std = 6
trials = 100_000

simulated_men = np.random.normal(men_avg, men_std, n_trials)
simulated_women = np.random.normal(women_avg, women_std, n_trials)

prob = (s_women > s_men).mean()
prob


# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
# for 50 students
fail_chance = 1/250
fails = 1
success = 0
students = 50
n_sim = 100_000
outcome = [fails, success]

installs = np.random.choice(outcome, size=(n_sim, students),p=[249/250, fail_chance])
((installs < fail_chance).sum(axis=1)==0).mean()

# for 100 students
fail_chance = 1/250
fails = 1
success = 0
students = 100
n_sim = 100_000
outcome = [fails, success]

installs = np.random.choice(outcome, size=(n_sim, students),p=[249/250, fail_chance])
((installs < fail_chance).sum(axis=1)==0).mean()


# for 150 students # ask success vs failure
fail_chance = 1/250
fails = 1
success = 0
students = 150
n_sim = 100_000
outcome = ['fails', 'success']

installs = np.random.choice(outcome, size=(n_sim, students),p=[249/250, fail_chance])
((installs == 'success').sum(axis=1)< students).mean()

# for 450 students
fail_chance = 1/250
fails = 1
success = 0
students = 450
n_sim = 100_000
outcome = [fails, success]

installs = np.random.choice(outcome, size=(n_sim, students),p=[249/250, fail_chance])
((installs < fail_chance).sum(axis=1)==0).mean()


# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen 
# a food truck there in 3 days. How unlikely is this?
n_trials = 10_000
n_trucks = 3
food_truck = 1
no_truck = 0

data = np.random.random((n_trials, n_trucks))
truck_prob = 0.7

((data < truck_prob).sum(axis=1)==0).mean()

outcomes = range(0,365)
n_student


# How likely is it that a food truck will show up sometime this week?



# If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?

outcomes = range(0,365)
n_student = 23
n_sim = 10_000
bd = np.random.choice(outcomes, size = (n_sim, n_students))
bd

pd.DataFrame(bd).nunique(axis=1)
(pd.DataFrame(bd).nunique(axis=1) <23).mean()

# 20 people
outcomes = range(0,365)
n_student = 20
n_sim = 10_000
bd = np.random.choice(outcomes, size = (n_sim, n_student))
bd

pd.DataFrame(bd).nunique(axis=1)
(pd.DataFrame(bd).nunique(axis=1) <20).mean()

# 40 people
outcomes = range(0,365)
n_student = 40
n_sim = 10_000
bd = np.random.choice(outcomes, size = (n_sim, n_student))
bd

pd.DataFrame(bd).nunique(axis=1)
(pd.DataFrame(bd).nunique(axis=1) <40).mean()
