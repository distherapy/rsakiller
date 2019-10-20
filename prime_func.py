from math import sqrt

#768bits 768/8 == 96/8 > 12/8

rsa232 = 1009881397871923546909564894309468582818233821955573955141120516205831021338528545374366109757154363664913380084917065169921701524733294389270280234380960909804976440540711201965410747553824948672771374075011577182305398340606162079

# ???
# x = len(digits)
# x = x / 2
# x = round x to nearest y.
# generate list of numbers equal to x
# test with different csv's, rsa's factored and unfactored
#???

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
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return n > 1
