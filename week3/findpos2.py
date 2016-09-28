def findpos(l,v)
	for i in range(len(l)):
		if l[i] == v: # Exit, report position
			pos = i
			break
		else:
			pos = -1 # No break, v not in l
	return(pos)
