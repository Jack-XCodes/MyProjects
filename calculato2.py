print('LETS DO SOME BASIC MATHEMATICS')

while True:
    num1=int(input('First no: '))
    op= input('choose operator: \n- to subtract , + to add, * to multiply, / to divide\n ')
    num2=int(input('Second no: '))
    try:
        if op == '-':
                answer=num1-num2  
        elif op == '+':
                answer=num1+num2
        elif op == '/':
                answer=num1/num2
        elif op == '*':
                answer=num1*num2
    except(ValueError):
        print('INVALID!request Try again')      
    break

print(f'{num1}{op}{num2} = {answer}')
        
        
        
        
        
