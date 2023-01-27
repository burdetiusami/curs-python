from validation_function import *
import csv


def insert_new_task(task_list, categories_list):
    with open('detalii_taskuri.csv', 'a') as file_task:
        csv_writer = csv.writer(file_task, delimiter=',')
        while True:
            task = input('Insert a new task. Press ENTER key to finish: ')
            if task == '':
                break
            if str(task) in [x[0] for x in task_list]:
                print('This task is already assigned, make another one! ')
                continue
            due_date = input('Insert a due date by format: dd/mm/yyyy hh:mm: ')
            if validare_data(due_date) is False:
                print("Invalid date! ")
                continue
            if due_date == '':
                break
            responsible_person = input('Insert person name for this task ')
            if responsible_person == '':
                break
            category_task = input(f'Choose from: {categories_list}: ')
            if str(category_task).lower() not in [elem.lower() for elem in categories_list]:
                print(" Your choise is not in list, try again! ")
                continue
            csv_writer.writerow([task, due_date, responsible_person, category_task])
            task_list.append([task, due_date, responsible_person, category_task])
