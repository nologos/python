# example of python dictionaries | dictionary 


sales = {
    'AKs05': {'price': 22.99, 'quantity': 1},
    'AKs02': {'price': 19.99, 'quantity': 2},
    'CLs01': {'price': 10.99, 'quantity': 3},
    'DFs01': {'price': 14.99, 'quantity': 1}
}

costs = {
    'AKs02': 8.50,
    'CLs01': 4.40,
    'DFs01': 2.45,
    'AKs01': 9.01
}

for index, sale in sales.items():
    if index in costs:
        res = (sale["price"] - costs[index]) * sale["quantity"]
        print(index, "made profit of £", res)




