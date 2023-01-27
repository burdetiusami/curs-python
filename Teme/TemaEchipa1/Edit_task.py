# Editarea detaliilor referitoare la task, dată, persoană
# sau categorie dintr-un anumit task ales de utilizator de la tastatură
# (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand,
# astfel încât să se știe ce informație urmează să editeze utilizatorul)

import csv
def edit_task(task_list):
    while True:
        print([x[0] for x in task_list])
        task_name = input("Please select a task from the above list ")
        if task_name not in [x[0] for x in task_list]:
            break
        option = input(
             "1. To change the date " "\n"
             "2. To change the task owner " "\n"
             "3. To change the category" "\n"
         )
        if int(option) not in range(1, 4):
            break
        if int(option) == 1:
            filtered_list = [n for n in task_list if n[0] == task_name]
            filtered_list[0][1] = input(f"Please provide a new due date for {task_name} ")
        elif int(option) == 2:
            filtered_list = [n for n in task_list if n[0] == task_name]
            filtered_list[0][2] = input(f"Please provide a new assigned person for {task_name} ")
        elif int(option) == 3:
            filtered_list = [n for n in task_list if n[0] == task_name]
            filtered_list[0][3] = input(f"Please provide a new assigned category for {task_name} ")
            break
    with open('detalii_taskuri.csv', 'w') as file_task:
        csv_writer = csv.writer(file_task, delimiter=',')
        for task in task_list:
            csv_writer.writerow(task)

