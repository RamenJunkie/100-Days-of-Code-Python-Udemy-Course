#Write your code below this line 👇
def prime_checker(number):
    is_prime = False

    for i in range(2,round((number/1.5))):
        if (number % i) == 0:
            #print(i)
            is_prime = True
            break


    if is_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)