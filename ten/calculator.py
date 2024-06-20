print("Calculator program")

def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    else:
        return False
    

def is_space(char):
    return char == ' '

def parse(expr):
    """Expects a string and returns a list"""
    expression = []
    i = 0
    while i < len(expr):
        if is_space(expr[i]) and i < len(expr):
            i += 1
        
        elif is_digit(expr[i]) and i < len(expr):
            num_start = i
            while i < len(expr) and is_digit(expr[i]):
                i += 1
            expression.append(str(expr[num_start:i]))

        elif expr[i] in ['+', '-', '/', '*']:
            expression.append(str(expr[i]))
            i += 1
    return expression


def print_result(expr):
    lhand = int(expr[0])
    op = str(expr[1])
    rhand = int(expr[2])

    if op == '+':
        print(lhand + rhand)
    elif op == '-':
        print(lhand - rhand)
    elif op == '/':
        print(lhand / rhand)
    elif op == '*':
        print(lhand * rhand)
    else :
        print("Operator not recognized")


expression = str(input("Please enter 2 numbers separated in the middle by an operator like +, -, /, or *: "))
parsed_expr = parse(expression)
print_result(parsed_expr)