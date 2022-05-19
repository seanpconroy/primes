num = int(input("Enter number: "))

isPrime(num)
def isPrime(num):

	not_prime = False

	# prime numbers are greater than 1
	if num > 1:
	    # check for factors
	    for i in range(2, num):
	        if (num % i) == 0:
	            # if factor is found, set flag to True
	            not_prime = True
	            # break out of loop
	            break

	# check if flag is True
	if not_prime:
	    print(num, "is not a prime number")
	else:
	    print(num, "is a prime number")