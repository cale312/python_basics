shopping_list = []

def show_help():
    print("What should we pick up at store today")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to view current shopping list.
Enter 'HELP' to view this menu.
""")

def show_list():
    print("Here is your list: ")
    for item in shopping_list:
            print(item)

def add_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        show_list()
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item in shopping_list:
        print("Item already added to cart")
        continue
    add_list(new_item)
