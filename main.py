# Task: create program for list of tasks to do
# 1. create a class, each instance of class is a single task
# task should have: create_date, update_date, title, content
# 2. add __str__ method to display the task information in nice way
# 3. create list for storing the tasks
# 4. add some tasks to the list and display the list in nice way
# 5. add code to allow to modify the tasks in the list
# 6. 

from datetime import datetime

print('welcome to todo list app')

def get_current_date():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

class TodoElement:
    def __init__(self, title, content):
        self.create_date = get_current_date()
        self.update_date = None
        self.title = title
        self.content = content
    
    def __str__(self):
        date_to_display = self.create_date if self.update_date is None else self.update_date
        return f'''{date_to_display} 
Title: {self.title} 
Content: {self.content}'''

    def update_title(self, new_title):
        self.title = new_title

    def update_content(self, new_content):
        self.content = new_content

todo_element = TodoElement("sample title", "sample content")
print()
print(todo_element)
print()
todo_list = list()
todo_list.append(todo_element)

print('list of elements contains:')
for element in todo_list:
    print(element)
print('end of list')
print()

def print_todo_list(list):
    print('list of elements contains:')
    for i, element in enumerate(todo_list):
        print(f"element number {i}")
        print(element)
    print('end of list')
    print()

print_todo_list(todo_list)

info_text = """Enter number then <Enter> to do action. 
Show list: 1. Add element: 2. Update element: 3. Remove element: 4.
Your choice: """

while(True):
    user_input = input(info_text).strip()
    user_chosen_number = int(user_input)
    if user_chosen_number == 1:
        print_todo_list(todo_list)
    elif user_chosen_number == 2:
        title = input("Title: ").strip()
        content = input("Content: ").strip()
        confirm = input("Add task? (Y/n)").lower().strip()
        if confirm == 'y':
            element_to_add = TodoElement(title, content)
            todo_list.append(element_to_add)
            print("Task added")
        else:
            print("Task not added")
    elif user_chosen_number == 3:
        user_chosen_task = int(input("Enter task number to edit: ").strip())
        if 0 <= user_chosen_number < len(todo_list):
            print(f"entered number `{user_chosen_number}` is invalid")
        else:
            print("Task to edit:")
            task_to_edit = todo_list[user_chosen_number]
            print(task_to_edit)
            print()
            title_needs_edit = input("Do you want to edit title? (Y/n)").lower().strip()
            if title_needs_edit == 'y':
                new_title = input("Enter new title: ").strip()
                task_to_edit.update_title = new_title
                print(f"title changed into: `{new_title}`")
            content_needs_edit = input("Do you want to edit content?")
            if content_needs_edit == 'y':
                new_content = input("Enter new content: ").strip()
                task_to_edit.update_content = new_content
                print(f"content changed into: `{new_content}`")
    elif user_chosen_number == 4:
        user_chosen_task = int(input("Enter task number to delete: ").strip())
        if 0 <= user_chosen_number < len(todo_list):
            print(f"entered number `{user_chosen_number}` is invalid")
        else:
            todo_list.remove(user_chosen_number)
            print(f"Task number {user_chosen_number} deleted from list")
    else:
        print(f"your choice `{user_chosen_number}` is invalid")
        