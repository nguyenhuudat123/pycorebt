# tao dict lon hon 3 phan tu
# value moi phan tu la list lon hon 5 phan tu
# truy cap, in a phan tu thu 5 ow moi value

dict_ = {i: [j*2 for j in range(i,i+6)] for i in range(5)}
print(dict_)
for i in dict_:
	print(f'phan tu thu 5 cua dict_[{i}] la {dict_[i][5]}')
# neu bat dau dem tu 0,1,2...