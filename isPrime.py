def isPrime(value):
    for i in range(2,10): # prime number should not be able to divide by any number between 2-10
        if value % i == 0:
            print("Number",value, "is not a prime number!")
            return
    print("Number", value, "is a prime number!")
    return
    
isPrime(value) 

