#sinh ra dict moi tu list cac dict
lst_dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
dict_ = {i['item']: i['amount'] for i in lst_dict}
print(dict_)