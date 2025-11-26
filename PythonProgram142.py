"""Get the key of a minimum value from the following dictionary
sample-dict = {'Physics':82,'math':65,'history';75}

Expected:
math"""
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

list1 = []
min_key = min(sample_dict, key=sample_dict.get)
list1.append(min_key)

print(list1)  # Output: ['Math']

