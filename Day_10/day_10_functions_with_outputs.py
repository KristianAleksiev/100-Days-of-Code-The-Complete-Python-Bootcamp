### Day 10 - Functions with outputs


# def my_function ():
#     result = 3*2
#     return result
# output = my_function()
# print(output)


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# print(format_name("KrIsTiaN", "ALEKsiev"))

### Multiple return functions

# return -> end of the functions


# def format_name(f_name, l_name):
#     if f_name =="" or l_name == "":
#         return "You did't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))

### 10.1 Days in month coding challenge

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

### Day 10 Project - Calculator

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with the {answer}, or type 'n' to start a new calculation.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator() #Recursive function so the code begins from the start of the function again
calculator()
