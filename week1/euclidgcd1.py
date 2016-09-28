def gcd(m,n):
	# Assume m >= n
	if m < n:
		(m,n) = (n,m)
	if (m%n) == 0:
		return(n)
	else:
		diff = m-n
	# diff > n? Possible!
	return(gcd(max(n,diff),min(n,diff))
