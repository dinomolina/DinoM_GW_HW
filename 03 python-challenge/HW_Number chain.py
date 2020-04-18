enter_number = 'y'

start = 0
end = 0


while enter_number == 'y':
    end = int(input('How many numbers? ')) + end
    
    for x in range(start , end):
        print(f'{x}')
       
    enter_number = input('Continue the chain: (y)es or (n)o? ')
    
    if enter_number == "y":
        start = end
        continue
    
    elif enter_number == "n":
        print('\nHW is complete!')
        break
    
    else:
        enter_number = input('Continue the chain: (y)es or (n)o? ')
        continue
    