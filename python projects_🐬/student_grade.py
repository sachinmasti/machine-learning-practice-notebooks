from colorama import Fore,Style,init
init(autoreset=True)
'''
user_input = int(input('enter your number: '))

if user_input <= 1:
    print(f'{Fore.RED} {user_input} is not a prime number')

elif user_input == 2:
    print(f'{Fore.GREEN} {user_input} is a prime number')

elif user_input % 2 == 0:
    print(f'{Fore.RED} {user_input} is not a prime number')

else:
    is_prime = True
    for i in range(3, int(user_input ** 0.5) + 1, 2):
        if user_input % i == 0:
            print(f'{Fore.RED} {user_input} is not a prime number')
            is_prime = False
            break
            
    if is_prime:
        print(f'{Fore.GREEN} {user_input} is a prime number')'''


def poly(lst_1,lst_2)->list:
    lst_3 = []
    for i, j in zip(lst_1, lst_2):
        lst_3.append(i ** j)
    return lst_3

lst = [2,3,4,5,6,7,8]
lst_2 = [1,2,3,4,5,6,7]
print(poly(lst,lst_2))

