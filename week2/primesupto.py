def primesupto(n):
	primelist = []
	for i in range(1,n+1):
		if isprime(i):
			primelist = primelist + [i]
	return(primelist)
