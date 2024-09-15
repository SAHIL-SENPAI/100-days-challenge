from calculatorart import art

#additin function
def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1*number2

def devide(number1,number2):
    return number1/number2


operations = {
    '+' : add,
    '-' : subtract,
    '/' : devide,
    '*' : multiply,
}
def calculator():
    print(art)
    first_number = float(input("Enter the first number: "))
    program_over = False
    while not program_over:
        for symbon in operations:
            print(symbon)

        which_operation = input('''Pick an operation:''')
        
        second_number = float(input("Enter the second number: "))
        answer = operations[which_operation](first_number,second_number)
        print(f"{first_number} {which_operation} {second_number} = {answer}")

        continuee = input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculation").lower()
        if continuee == 'y':
            first_number = answer
        else:
            print("\n"*20)
            calculator()


calculator()