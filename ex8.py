#Python Program to demonstrate working with dictionaries in python
dict1 = {'StdNo':532,'StuName': 'Naveen', 'StuAge': 21, 'StuCity': 'Hyderabad'}
print('\n Dictionary is :',dict1)
#Accessing specific values
print('\n Student Name is :',dict1['StuName'])
#Display all Keys
print('\n All Keys in Dictionary ')
for x in dict1:
    print(x)
dict1['Phno']=85457854
print('\n Updated Dictionary is :',dict1)
dict1['StuName']='Madhu'
print('\n Updated Dictionary is :',dict1)
dict1.pop('StuAge');
print('\n Updated Dictionary is :',dict1)
dict2=dict1.copy()
dict1.clear()
print('\n New Dictionary is :',dict2)
