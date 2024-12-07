def add(x,y):
    return x+y 

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return x
    else:
        return x/y


def calculator():
    i=True
    ans=0
    a = float(input('enter first number'))
    while(i):
        operator = input('+ \n - \n * \n / \n')
        
        b = float(input('enter next number'))

        if operator == '+':
            ans = add(a,b)
            
        elif operator == '-':
            ans = sub(a,b)

        elif operator == '*':
            ans = mul(a,b)

        elif operator == '/':
            ans = div(a,b)
            
        else:
            print('invalid operator')
        
        print(f'{a} {operator} {b} = {ans}')
        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation or type 'e' to exit: ")
        if choice == 'y':
            a=ans
        elif choice == 'n':
            i=False
            calculator()
        else:
            exit()
calculator()