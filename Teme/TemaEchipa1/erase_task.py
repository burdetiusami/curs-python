import csv


def erase_task(task_list):
    print([x[0] for x in task_list])
    r_line = input("Please select a task from the above list you want to delete ")
    if r_line not in [x[0] for x in task_list]:
        print('This task is not on list!')
    else:
        print('Task was deleted!')
        with open('detalii_taskuri.csv', 'w') as file_task:
            csv_writer = csv.writer(file_task, delimiter=',')
            for task in task_list:
                if task[0] != r_line:
                    csv_writer.writerow(task)
