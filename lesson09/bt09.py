#sinh ra dict moi tu list cac dict
lst_dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output = {}
for element in lst_dict:
  item = element['item']
  amount = element['amount']
  if item not in output:
    output[item] = amount
   else:
    output[item] += amount
   
print(output)
