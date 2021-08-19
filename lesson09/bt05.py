# tao dict theo lstkey
sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
lst_keys = ["name", "salary"]
new_dict = {i: sampleDict[i] for i in lst_keys}
print(new_dict)