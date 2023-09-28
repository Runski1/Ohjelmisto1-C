from user_called_functions import *
commands_without_parameter = ["search", "hire", "help", "exit"]


def user_input_processor(input_string):
    input_as_list = input_string.split()
    selected_function = command_dictionary[input_as_list[0]]
    if len(input_as_list) < 2 and input_as_list[0] in commands_without_parameter:
        selected_function()
    elif len(input_as_list) == 2:
        selected_function(input_as_list[1])
    else:
        print("Bad parameters.")

while True:
    user_input_processor(input("[ENTER COMMAND]"))
