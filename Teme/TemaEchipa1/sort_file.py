def List_Sorting(list,x):
    if x == "1":
        list.sort(key=lambda x: x[0])
        # print("your list of tasks sort in ascent  order by task")
    elif x == "2":
        list.sort(key=lambda x: x[0], reverse=True)
        # print("your list of tasks sort in descent  order by task")
    elif x == "3":
        list.sort(key=lambda x: x[1])
        # print("your list of tasks sort in ascent  order by date")
    elif x == "4":
        list.sort(key=lambda x: x[1], reverse=True)
        # print("your list of tasks sort in descent  order by date")
    elif x == "5":
        list.sort(key=lambda x: x[2])
        # print("your list of tasks sort in ascent  order by name")
    elif x == "6":
        list.sort(key=lambda x: x[2], reverse=True)
        # print("your list of tasks sort in ascent  order by name")
    elif x == "7":
        list.sort(key=lambda x: x[3])
        # print("your list of tasks sort in ascent  order by category ")
    elif x == "8":
        list.sort(key=lambda x: x[3], reverse=True)
        # print("your list of tasks sort in descent  order by category ")
    return list

def meniu_sortare(list):
    while True:
        option = input("Please pick one of the options in order to sort the list " +
                       "\n" " 1. Sort in ascending order  by task"
                       "\n" " 2. Sort in descending order  by task"
                       "\n" " 3. Sort in ascending order  by date"
                       "\n" " 4. Sort in descending order  by date"
                       "\n" " 5. Sort in ascending order  by name"
                       "\n" " 6. Sort in descending order  by name"
                       "\n" " 7. Sort in ascending order  by category"
                       "\n" " 8. Sort in descending order  by category ")
        if int(option) in [x for x in range(1, 9)]:
            break
        else:
            continue
    print(f"Lista initiala:  {list}")
    sorted_list = List_Sorting(list, option)
    print(f"Lista sortata: {sorted_list}")

def listare_task_list_by_categories(list):
    list.sort(key=lambda x: x[3])
    print(list)

