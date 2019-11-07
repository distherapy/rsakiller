from math import sqrt

def prime_search(): 
	y = [2]
	x = 1000
	while len(y) < 2000:
		if all(x % i != 0 for i in range(2, int(round(sqrt(x) + 1)))):
			y.append(x)
		x = x + 1
	print(y)

def largest_prime(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
    print(largest_prime())

def primality(n):
return 2 in [n,2**n%n]
