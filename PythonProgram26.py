#Calculate income tax for the given income by adhering to the below rules first 10K-->0% second 10__>10% remaining-->20%
#Expected Output:
#For Example ,suppose the taxable income is 45000 the income tax payable is
#100000% + 1000010% + 25000*20% = $6000.
n=int(input("Enter the number:"))
if n<=10000:
    print(n)
else:
    a=n-10000
    b=a-10000
    c=b*0.2
    d=c+1000
    print(d)