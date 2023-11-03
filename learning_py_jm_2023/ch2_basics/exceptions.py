#
# Example file for working with Exceptions
# LinkedIn Learning Python course by Joe Marini

# Erros can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
#x = 10/0

# TODO: Exceptions provide a way of catching erros and then hadnling them
# a separate section of the code to group them together
# try:
#     x = 10/0
# except:
#     print("Well that didn't work")

# TODO: you can also catch specific exceptions
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
finally:
    print("This code always runs")