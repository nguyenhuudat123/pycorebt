# 3 phan tu cua dict co key lon nhat
dict_ = {
	1 :2,
	10:4,
	5:6,
	7:8,
	9:10
}
b = sorted(dict_)
print(b)
for i in range(-1,-4,-1):
	print(b[i], ':', dict_[b[i]])
