#so lan xuat hien tu don
in_str = 'la la la la mot hai ba bon nagy hayi hai ba mot ngay'
in_lst = in_str.split(" ")
print(in_lst)
lst = list(set(in_lst))
print(lst)

dict_ = {}
print(dict_)
for item in lst:
	count = 0
	for in_item in in_lst:
		if item == in_item:
			count += 1
	dict_.update({item:count})
print(dict_)