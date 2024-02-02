def main():
    current_list = []

    what_to_do = input(f"What would you like to do?\n\n1 - Create list\n2 - Most Recent Task\n3 - Delete Task\nOR \"Enter\" to EXIT\n")

    while what_to_do != "":

        if what_to_do == "1":
            todo_list = create()
            current_list = todo_list
            what_to_do = input(f"What would you like to do?\n\n1 - Create list\n2 - Most Recent Task\n3 - Delete Task\nOR \"Enter\" to EXIT\n")
            
        elif what_to_do == "2":
            last_task = read_task(current_list)
            print(last_task)
            what_to_do = input(f"What would you like to do?\n\n1 - Create list\n2 - Most Recent Task\n3 - Delete Task\nOR \"Enter\" to EXIT\n")

        elif what_to_do == "3":
            new_list = delete(current_list)
            current_list = new_list
            print(f'Here is your new list {new_list}')
            what_to_do = input(f"What would you like to do?\n\n1 - Create list\n2 - Most Recent Task\n3 - Delete Task\nOR \"Enter\" to EXIT\n")

    return(f'Here is your final ToDo list: {current_list}')
    

def create():
    order = 1
    todo_list = []

    another_task = "Y"

    while another_task == "Y":
        
        task = input("Enter a task to add to the todo list: ")
        another_task = input("Do you want to add another task? (Enter \"Y\" to continue) ").upper()
        # sub_task = input()
    
        todo_list.append([order, task])
        order += 1

    return todo_list
    

# def update():
#     pass

def delete(list):
    list.pop()
    return list

def read_task(todo_list):
    next_task = todo_list[-1]

    return(next_task)

print(main())

