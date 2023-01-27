
from manage_categories import *
from manage_task import *
from meniu_file import *

categories_list = []
task_list = []

manage_categories(categories_list)
manage_task(task_list, categories_list)
manager_menu(task_list, categories_list)



