dict1 = {i: i**3 -30 for i in range(26)}
print(dict1)

dict2 = {i: 10*i**2 -31*i for i in range(20)}
print(dict2)
print('\nphan tu trung nhau cua 2 dict:')
for item1 in dict1:
	for jtem2 in dict2:
		if item1 == jtem2 and dict1[item1] == dict2[jtem2]:
			print(item1, ':', dict1[item1], end= ' ;')