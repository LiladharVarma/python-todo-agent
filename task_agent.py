
tasks= []
def add_task(description=""):
    if description == "":
       print("Please add valid task , ex: buy milk ")
    else:
        tasks.append({"description": description, "done": False})
        print(f"Tasks Added ! ")



def list_task(ignored=None):
    for i , task in enumerate(tasks):
        if task["done"] == False:
            print(f"[ ] {i}:{task['description']}")
        else:
            print(f"[X] {i}:{task['description']}")

def complete_task(index=""):

    try:
        index = int(index)
        tasks[index]["done"] = True
        print(tasks[index])

    except ValueError:
        print("That is not a valid number")
    except IndexError:
        print("No valid value present at tis position")



functions = {
    "list":list_task ,
    "add":add_task,
    "done":complete_task
}

add_task("Drink Water")
add_task("buy milk")
add_task("Bring clothes frmo loundry")
#
# list_task()
# complete_task(0)
# print(tasks)

while True:
    command = input("> ").strip()
    command_parts = command.split(" " , 1)
    command = command_parts[0]
    argument = ""
    if len(command_parts) > 1:
        argument = command_parts[1]
    else:
        argument = None

    if command == "quit":
        # print(f"{command}")
        print("Bye")
        break
    elif command in functions:
        # print(f"{command}")
        if argument is None:
            functions[command]()
        else:
            functions[command](argument)
    else:
        print(f"Unknown command : {command}")