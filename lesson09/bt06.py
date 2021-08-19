#lay top 3 phan tu value lon nhat
dict_ = {
	1:2, 1:6, 4:10,
	3:4, 5:6,
	7:8, 9:10,
	5:3,3:1
}
if len(dict_) <3:
	print('khong du phan tu')
else:
	count = 1
	a = sorted(list(set(dict_.values())), reverse=True)
	#set: loai pt lap
	#list: dua ve dang chi so
	#sorted: ra list co thu tu be --> to
	print(a)
	for i in a:
		for item in dict_:
			if dict_[item] == i:
				print(item, ':', i)
				count += 1
			if count >= 3:
				break
