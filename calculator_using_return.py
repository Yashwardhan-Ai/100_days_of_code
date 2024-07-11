print( """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)

def add(n1,n2):
    """Adds Two Numbers"""
    return n1 + n2
def substract(n1,n2):
    """Substracts Two Numbers"""
    return n1 - n2
def multiply(n1,n2):
    """Multiplies Two Numbers"""
    return n1 * n2
def divide(n1,n2):
    """Divides Two Numbers"""
    return n1 / n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
    }
def calculator():
    num1 = float(input("ENTER THE FIRST NUMBER :"))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation :")
        num2 = float(input("ENTER THE NEXT NUMBER :"))
        operation_to_do = operations[operation_symbol]
        answer = operation_to_do(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        wanna_continue = input("PLEASE INPUT 'Y' OR 'N' TO CONTINUE OR STOP :").lower()
        if wanna_continue == "y" :
            num1 = answer
        elif wanna_continue != "y":
            should_continue = False
            calculator()

calculator()

 