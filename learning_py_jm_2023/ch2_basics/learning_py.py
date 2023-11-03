# Example of print
# LinkedIn Learning Python course by Joe Marini

def main():
    print("Hello world")
    name = input("What is your name? ")
    print("Nice to meet you", name)

# python does not look for a specific function when the program start
# So this helps distinguish when .py is being executed as its own program vs being called by another program
# This runs when we run the script in the terminal (think of it as an initial state of being of the script)
if __name__ == "__main__":
    main()