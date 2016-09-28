def nprimes(n):
	(count,i,plist) = (0,1,[])
	while(count < n):
		if isprime(i):
			(count,plist) = (count+1,plist+[i])
		i = i+1
	return(plist)
