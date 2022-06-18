print(".....HELLO LETS CREATE A CALCULATOR USING PYTHON......")


while True:
    print('lest do a simple calculation.with either :- ,+, *, /')
    
    num1=int(input('num1: '))
    op= input('place your operator: ')
    num2=int(input('num2: '))
    
    if op == '-' : 
        print(f'{num1}{op}{num2} = {num1-num2}')   
    elif op == '+':
        print(f'{num1}{op}{num2} = {num1+num2}')
    elif op == '/ ':
        print(f'{num1}{op}{num2} = {num1/num2}')
    elif op == '*' :
        print(f'{num1}{op}{num2} = {num1*num2}')
    
    else:
        print('OOPS! INVALID REQUEST')