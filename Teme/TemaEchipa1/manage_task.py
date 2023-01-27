import csv
from validation_function import *

def manage_task(task_list, categories_list):
    with open('detalii_taskuri.csv', 'a') as file_task:
        csv_writer = csv.writer(file_task, delimiter=',')
    with open('detalii_taskuri.csv', 'r') as file_task:
        lines = csv.reader(file_task, delimiter=',')
        for line in lines:
            if line:
                task_list.append(line)
    with open('detalii_taskuri.csv', 'a') as file_task:
        csv_writer = csv.writer(file_task, delimiter=',')
        while True:
            tasks = input('Insert a new task. Press ENTER key to finish: ')
            if tasks == '':
                break
            if str(tasks) in [x[0] for x in task_list]:
                print('This task is already assigned, make another one! ')
                continue
            end_date = input('Insert a due date by format: dd/mm/yyyy hh:mm: ')
            if validare_data(end_date) is False:
                print("Invalid date! ")
                continue
            if end_date == '':
                break
            responsible = input('Insert person name for this task ')
            if responsible == '':
                break
            category = input(f'Choose from: {categories_list}: ')
            if str(category).lower() not in [elem.lower() for elem in categories_list]:
                print(" Your choise is not in list, try again! ")
                continue
            csv_writer.writerow([tasks, end_date, responsible, category])
            task_list.append([tasks, end_date, responsible, category])
            next_task = input('Insert a new task? (Y/N): ')
            if next_task.lower() == 'n':
                break
            elif next_task.lower() == 'y':
                pass
            else:
                print("Your option is not valid: Y/N. Try again!")
                continue
