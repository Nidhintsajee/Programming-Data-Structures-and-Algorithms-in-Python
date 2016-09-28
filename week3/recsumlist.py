def sumlist(l):
	if l == []:
		return(0)
	else:
		return(l[0] + sumlist(l[1:])
