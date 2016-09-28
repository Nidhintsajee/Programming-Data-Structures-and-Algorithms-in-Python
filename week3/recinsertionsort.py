def InsertionSort(seq):
	isort(seq,len(seq))
def isort(seq,k): #
	if k > 1:
		isort(seq,k-1)
		insert(seq,k-1)
		Sort slice seq[0:k]
def insert(seq,k): # Insert seq[k] into sorted seq[0:k-1]
	pos = k
	while pos > 0 and seq[pos] < seq[pos-1]:
		(seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
		pos = pos-1
