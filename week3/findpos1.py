def findpos(l,v):
	# Return first position of v in l
	# Return -1 if v not in l
	(found,i) = (False,0)
	while i < len(l):
		if not found and l[i] == v:
			(found,pos) = (True,i)
	if not found:
		pos = -1
	return(pos)
