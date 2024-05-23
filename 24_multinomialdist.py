#multinomial dist- it is the generalization of binomial dist.

#parameters- n= number of possibilities/outcomes
#pvals= list of possibility or outcome
#size

#draw out a sample of dice roll
from numpy import random 
dice= random.multinomial(n=6,pvals= [1/6,1/6,1/6,1/6,1/6,1/6]) 
print(dice)