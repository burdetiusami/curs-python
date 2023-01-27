def filter_list(initial_list, opt):
    filtered_list = []
    if opt == "1":
        # lista_taskuri= [x[0] for x in list]
        print([x[0] for x in initial_list])
        task_name = input(f"Please provide the name of the task you wish to filter ")
        filtered_list = filter(lambda x: x[0] == task_name, initial_list)
    elif opt == "2":
        print([x[1] for x in initial_list])
        date = input("Please provide the  date you wish to filter ")
        filtered_list = filter(lambda x: x[1] == date, initial_list)
    elif opt == "3":
        print([x[2] for x in initial_list])
        person_name = input("Please provide the user name you wish to filter ")
        filtered_list = filter(lambda x: x[2] == person_name, initial_list)
    elif opt == "4":
        print([x[3] for x in initial_list])
        category = input("Please provide  category you wish to filter ")
        filtered_list = filter(lambda x: x[3] == category, initial_list)
    return filtered_list


def meniu_filtrare(list_to_filter):
    while True:
        option2 = input("Please pick one of the options in order to filter the list " +
                        "\n" " 1. Filter  by task"
                        "\n" " 2. Filter  by date"
                        "\n" " 3. Filter  by name"
                        "\n" " 4. Filter  by category ")
        if int(option2) in [x for x in range(1, 5)]:
            break
        else:
            continue
    print(list(filter_list(list_to_filter, option2)))
