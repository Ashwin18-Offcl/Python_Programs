#The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
#you have to wite a program to find out the population at the end of each of the last 10 years.For eg current population is 10000 so the output should be like this:
#10th year-10000
#9th year-9000
#8th year - 8100 and so on
p=10000

for i in range(1,10):
    p=p-0.1*p
    print(round(p),end=" ")
    