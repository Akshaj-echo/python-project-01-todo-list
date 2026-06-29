tasks = [
    "Complete Python lesson",
    "Workout",
    "Read book",
    "Practice coding"
]


completed_tasks = []

incomplete_tasks = []


print("Today's Tasks:")

for task in tasks:
    print(task)



for task in tasks:

    status = input(f"Did you complete '{task}'? (yes/no): ")

    if status == "yes":

        completed_tasks.append(task)

    else:

        incomplete_tasks.append(task)



print("\nCompleted Tasks:")

for task in completed_tasks:
    print(task)



print("\nIncomplete Tasks:")

for task in incomplete_tasks:
    print(task)      
