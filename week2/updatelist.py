def update(l,i,v):
	if i >= 0 and i < len(l):
		l[i] = v
		return(True)
	else:
		v = v+1
		return(False)
