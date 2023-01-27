def manage_categories(categories_list):
    with open('categorii.txt', 'a') as file_categorii:
        file_categorii.write('')
    with open('categorii.txt', 'r') as file_categorii:
        for line in file_categorii.readlines():
            categories_list.append(line.strip())
    with open('categorii.txt', 'a') as file_categorii:
        while True:
            print(f'Categories list is: {categories_list}')
            next_category = input('Insert a new category? (Y/N): ')
            if next_category.lower() == 'n':
                break
            elif next_category.lower() == 'y':
                pass
            else:
                print("Your option is not valid: Y/N. Try again!")
                continue
            category = input('Insert a category: ')
            if str(category) == '':
                break
            if str(category) not in categories_list:
                categories_list.append(category)
                file_categorii.write(category)
                file_categorii.write("\n")
            else:
                print("Category already exist, insert a new one!")