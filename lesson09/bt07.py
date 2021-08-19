#dem so lan xuat hien ki tu
in_str = input('nhap 1 chuoi: ')
in_lst = list(in_str)
print(in_lst)
lst = list(set(in_str))
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