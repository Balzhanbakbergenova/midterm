#User input, code output [3.333%]
while True: #бесконечный цикл
    try: #начинается блок, в котором выполняется код, исключения из которого обрабатываются
        name = input("Please enter your name: ") #код запрашивает у пользователя ввести свое имя
        salary = float(input("Please enter your desired salary: ")) #пользователю предлагается ввести желаемую зарплату, которая затем преобразуется в число с плавающей запятой и сохраняется в переменной

        if salary < 0:
            raise ValueError("Salary cannot be negative") # Если зарплата меньше 0, то возникает исключение типа ValueError

        tax_level = salary * 0.2 #Если зарплата больше или равна 0, то рассчитывается уровень налога как 20% от зарплаты

        print(f"Hello, {name}! Your tax level is: {tax_level}") #выводится приветственное сообщение, включающее имя пользователя и рассчитанный уровень налога
        break  #цикл завершается
    except ValueError as e:
        print(f"Invalid input: {e}") #Если возникает такое исключение, программа выводит сообщение об ошибке, и цикл продолжает выполняться, пока пользователь не введет корректные данные
















#Using arithmetic, bitwise and logic ops [6.667%]
# Define lambda functions for arithmetic operations
#Сначала определены четыре лямбда-функции для выполнения арифметических операций
addition = lambda x, y: x + y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y
exponentiation = lambda x, y: x ** y
#Затем выводится меню для выбора операции с помощью
print("Please choose the task you want to perform:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

try:
    choice = int(input("Enter your choice (1/2/3/4): ")) #Пользователь вводит свой выбор с клавиатуры и сохраняет его в переменной
    if choice not in (1, 2, 3, 4):
        print("Invalid choice. Please enter a valid option.") #Если выбор пользователя не является целым числом от 1 до 4, выводится сообщение об ошибке
    else: #В зависимости от выбора пользователя (choice), определяется, какая операция будет выполняться.
        if choice == 4:
            operation = "exponentiation"
        elif choice == 3:
            operation = "division"
        elif choice == 2:
            operation = "multiplication"
        else:
            operation = "addition"

        numbers = input(f"Please enter two numbers for {operation}, comma separated: ").split(',') #Пользователь вводит два числа, разделенных запятой, соответствующих выбранной операции. Ввод проверяется на корректность.

        if len(numbers) != 2: #Пользователь вводит два числа, разделенных запятой, соответствующих выбранной операции
            print("Please enter two numbers separated by a comma.")
        else: #Если ввод корректен, числа преобразуются в числа с плавающей запятой
            x, y = map(float, numbers)

            if choice == 1:
                result = addition(x, y)
            elif choice == 2:
                result = multiplication(x, y)
#Если выбрана операция деления (choice == 3), проверяется, что второе число не равно нулю. Если второе число равно нулю, выводится сообщение об ошибке "Division by zero is not allowed."
            elif choice == 3:
                if y == 0:
                    print("Division by zero is not allowed.")
                    exit(1)
                result = division(x, y)
            else:
                result = exponentiation(x, y)

            print(f"Result: {result}") #Результат операции сохраняется и выводится на экран
except ValueError:
    print("Invalid input. Please enter a valid number for your choice.") #Если возникает исключение ValueError, выводится сообщение об ошибке











#Loops and iterations [10%]
# Prompt the user to enter the length of the Fibonacci sequence
#Пользователю предлагается ввести длину последовательности Фибоначчи с помощью input. Введенное значение сохраняется в переменной length
try:
    length = int(input("Enter the length of the Fibonacci sequence: "))
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit(1)

# Check if the length is valid (greater than 0)
if length <= 0:
    print("Length should be a positive integer.")
    exit(1)

# Initialize the first two Fibonacci numbers
fibonacci_sequence = [1, 1]
#Если введенное значение length корректно, начальные значения [1, 1] добавляются в список fibonacci_sequence
# Generate the Fibonacci sequence
for i in range(2, length): #используется цикл for для генерации остальных чисел последовательности Фибоначчи
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

# Print the Fibonacci sequence
print("Fibonacci Sequence:")
for number in fibonacci_sequence:
    print(number, end=" ") #числа разделяются пробелом










#Tuples and sets [13.333%]
# Prompt the user to enter items separated by commas
#Создается список items, в котором каждый элемент представляет собой строку, введенную пользователем и разделенную запятыми. strip() используется для удаления лишних пробелов вокруг каждого элемента
user_input = input("Enter items separated by commas: ")
items = [item.strip() for item in user_input.split(',')]

# Create a set to store unique items
unique_items = set()

# Create a dictionary to store the frequency of non-unique items
item_frequency = {} #Создается словарь для отслеживания частоты встречаемости неуникальных элементов

# Process the items
for item in items:
    if item in unique_items:
        if item in item_frequency:
            item_frequency[item] += 1
        else:
            item_frequency[item] = 2  # Second occurrence
    else:
        unique_items.add(item)

# Convert the item_frequency dictionary to a list of (item, frequency) tuples
non_unique_items = [(item, frequency) for item, frequency in item_frequency.items()] #После завершения обработки всех элементов, создается список кортежей

# Output the results
print("Unique Items (Set):", unique_items) #выводит уникальные элементы
print("Non-Unique Items (Tuple with Frequencies):", non_unique_items) #выводит неуникальные элементы и их частоту в виде списка кортежей











#Lists and dictionaries [16.667%]
# Initialize an empty list to store tasks
tasks = []
#Создается пустой список tasks, который будет содержать информацию о задачах
while True:
    print("\nTo-Do List Manager:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
#Пользователь выбирает операцию, вводя соответствующий номер
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to your to-do list.")

    elif choice == '2':
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(tasks, 1):
                status = "✓" if task["completed"] else "✗"
                print(f"{i}. [{status}] {task['task']}")

    elif choice == '3':
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            view_tasks = False
            while not view_tasks:
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['task']}")
                task_num = input("Enter the task number to mark as completed (0 to cancel): ")
                if task_num == '0':
                    break
                elif task_num.isnumeric():
                    task_num = int(task_num)
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]["completed"] = True
                        print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
                        view_tasks = True
                    else:
                        print("Invalid task number. Please try again.")
                else:
                    print("Invalid input. Please enter a valid task number.")

    elif choice == '4':
        print("Goodbye!") #Если выбрана операция "Выход" (4), программа завершает выполнение и выводит "До свидания!"
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
#Если пользователь ввел недопустимый выбор, выводится сообщение об ошибке






