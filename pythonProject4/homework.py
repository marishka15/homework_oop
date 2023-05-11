from pprint import pprint

#Задача №1
with open ('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        ingredients_name = line.strip()
        quantity_of_ingredients = int(file.readline())
        quantitys = []
        for i in range (quantity_of_ingredients):
            quan = file.readline()
            ingredient_name, quantity, measure = quan.strip().split('|')
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            quantitys.append(ingredient)
        file.readline()
        cook_book[ingredients_name] = quantitys
    #pprint(cook_book, sort_dicts=False)

#Задача  №2
def get_shop_list_by_dishes(dishes,person_count):
  res = {}
  for dish in dishes:
    if dish in cook_book:
      for consist in cook_book[dish]:
        if consist['ingredient_name'] in res:
          res[consist['ingredient_name']['quantity']] += consist['quantity'] * person_count
        else:
          res[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (int(consist['quantity']) * person_count)}
  pprint(res)
get_shop_list_by_dishes( ['Запеченный картофель', 'Омлет'], 2)