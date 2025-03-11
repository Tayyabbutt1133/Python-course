# logic will be:
# 1. First, user will be writing todos
# 2. Then, user can read todos
# 3. Then, user can edit specific line todo


# Add todo
user_input = input("Enter todo:")
f_write_todo = open("file.txt", "a")
f_write_todo.write(user_input + '\n')
f_write_todo.close()

# Read todo
print("------Reading all todos------")
f_read_todo = open("file.txt", "r")
data = f_read_todo.read()
print(data)
f_read_todo.close()


# Edit todo
print("-----Editing todo-------")
f_edit_todo = open("file.txt", 'r')
todos_list = f_edit_todo.readlines()
# print(todos_list)
f_edit_todo.close()
todos_list[0] = "I am not learning python\n"

f_update = open("file.txt", "w")
f_update.writelines(todos_list)
f_update.close()