import csv

from filter_list import *
from sort_file import *
from erase_task import *
from insert_task import *
from Edit_task import *


def manager_menu(task_list, categories_list):
    while True:
        menu_option = input(
            'Select one option: \n '
            '1. List all task by categories \n '
            '2. Sort task list \n '
            '3. Filter task list  \n '
            '4. Insert a new task \n '
            '5. Edit task \n '
            '6. Erase task \n '
            '7. Press C to close app ')
        if str(menu_option) == '':
            print("You did not type one option!Try again!")
            continue
        if menu_option.lower() == 'c':
            break
        if not str(menu_option).isdigit():
            print('Option invalid! Try again!')
            continue
        if int(menu_option) not in range(1, 7):
            print('Option invalid! Try again!')
            continue
        elif int(menu_option) == 1:
            listare_task_list_by_categories(task_list)
            continue
        elif int(menu_option) == 2:
            meniu_sortare(task_list)
            continue
        elif int(menu_option) == 3:
            meniu_filtrare(task_list)
            continue
        elif int(menu_option) == 4:
            insert_new_task(task_list, categories_list)
            continue
        elif int(menu_option) == 5:
            edit_task(task_list)
            continue
        elif int(menu_option) == 6:
            erase_task(task_list)
            continue

