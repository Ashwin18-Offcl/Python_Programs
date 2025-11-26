"""Initialize dictionry with default values in Python, we can initialize  the keys with the same values.
employees = ["Kelly","Emma"]
defaults = {"designation":'Developer','salary':8000},'Emma':{'designation';'Developer'}"""
employees = ['Kelly','Emma']
defaults = {"designation":'Developer',"salary":8000}
result = dict.fromkeys(employees,defaults)
print(result)
print("="*100)
print("Details of kelly;",result["Kelly"])