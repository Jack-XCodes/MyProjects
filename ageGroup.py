print(",,,,Hey wanna know your age group,,,,,.\n It's simple.\nTell me your age and  I will tell you!!!")
 
try:
    age = int(input('Your age: '))
    if age in range(0,13):
        print('Dude you are a Kid')
    elif age in range(13,20):
        print('Dude you are a Teenager')
    elif age in range(20,31):
        print('Dude you are a young Adult')
    elif age in range(31,65):
        print('Dude you are an Adult')
    else:
        print('Dude you are a Senior')
except:
    print('oops put a value')