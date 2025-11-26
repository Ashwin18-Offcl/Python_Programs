#To get first 25 numbers
def is_prime(x):
    new = []
    if x <= 1:
        return False
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                new.append(i)
        if len(new) <= 2:
            return True
        else:
            return False

# Now the main code is outside the function
count = 0
num = 2

while count < 25:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1
