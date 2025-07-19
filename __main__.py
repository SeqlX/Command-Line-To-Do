# Remaining Objectives:
# Add a remove task by number feature
# Sort task by completed and datetime
# Possibly add Task Due Dates
# Add a return or back feature

#Libraries
from colorama import init, Fore, Style
from datetime import datetime



# Add task
def AddTask():
	with open("todo_list.txt", "a") as f:
		f.write("\n" + input(Fore.YELLOW + "Enter Task: "))

	print(Fore.GREEN + "You're task has been added.")
	print(Style.RESET_ALL)



# Marks task as completed
def CompleteTask():
	tasklist = []
	with open("todo_list.txt") as txtfile:
		for x in txtfile:
			tasklist.append(x)
	#print(tasklist)

	completedtasknum = int(input("What is the number of your completed task in the list?: ")) - 1
	newtaskstate = tasklist[completedtasknum].strip() + " [COMPLETED]\n"
	tasklist[completedtasknum] = newtaskstate
	
	with open("todo_list.txt", "w") as f:
		for x in tasklist:
			f.write(x)

	with open("todo_list.txt") as txtfile:
		for x in txtfile:
			print(Fore.CYAN + x)
		print(Fore.GREEN + "\nTask Completed!")
		print(Style.RESET_ALL)



# Primary Function
def main_menu():
	while True:
		def DisplayTasks():
			with open("todo_list.txt") as txtfile:
				for i, task in enumerate(txtfile, start=1):
					task = task.strip()
					if "[COMPLETED]" in task:
						print(Fore.GREEN + f"{i}. {task}")
					else:
						print(Fore.CYAN + f"{i}. {task}")
				print(Style.RESET_ALL)
		
		DisplayTasks()
		userinput = input(Fore.YELLOW + "What would you like to do?: Add a new task(Add), mark a completed task(Complete), or Quit?: ").lower()

		if userinput == "add":
			AddTask()
		elif userinput == "complete":
			CompleteTask()
		elif userinput == "quit":
			print(Fore.RED + "Exiting To-Do List. Goodbye!")
			print(Style.RESET_ALL)
			break
		else:
			print(Fore.RED + "Your input is not a valid option please try again.")
			print(Fore.YELLOW)






main_menu()