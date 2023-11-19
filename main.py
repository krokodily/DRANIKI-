def prime_numb(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime: 
        print('prost')
    else:
        print('ne prost')

prime_numb(13)
prime_numb(49)


