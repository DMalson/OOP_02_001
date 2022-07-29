cook_book = {}
with open("recipes.txt", 'r', encoding='utf-8') as file_obj:
    while True:
        dish = file_obj.readline().strip()
        if len(dish) == 0:
            break
        num_of_ingredients = int(file_obj.readline().strip())
        recipe = []
        for record in range(0,num_of_ingredients):
            ingredient={}
            read_string = file_obj.readline().strip().split('|')
            ingredient['ingredient_name'] = read_string[0].strip()
            ingredient['quantity'] = int(read_string[1])
            ingredient['measure'] = read_string[2].strip()
            recipe.append(ingredient)
        cook_book[dish] = recipe
        l=file_obj.readline()
print(cook_book)

