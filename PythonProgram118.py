#Get all values from the dictionary and add them to a list but dont add duplicates
#speed={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sep':54}
#expected_output[47,52,44,53,54]
speed = {'Jan':47,'Feb':52, 'March':47,'April':44,'May':52,'June':53,'July':54}
speed_list=[]

for value in speed.values():
    if value not in speed_list:
        speed_list.append(value)

print(speed_list)
