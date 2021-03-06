def Exchange(list, index1, index2):
	temp = list[index1]
	list[index1] = list[index2]
	list[index2] = temp

def Median(list, index1, index2, index3):
	if list[index1] > list[index2]:
		if list[index3] > list[index1]:
			return index1
		elif list[index3] > list[index2]:
			return index3
		else:
			return index2
	else:		#list[index1] <= list[index2]
		if list[index3] > list[index2]:
			return index2
		elif list[index3] > list[index1]:
			return index3
		else:
		 return index1
		
def QuickSort(list, start, end):
	#Recursion end
	if start >= end:
		return

	#Choose the median from list[start], list[(start + end) / 2] and list[end] to improve QuickSort
	mid = Median(list, start, (start + end) / 2, end)
	Exchange(list, mid, end)

	#Divide list into two part
	m = start
	for i in range(start, end):
		if list[i] < list[end]:
			Exchange(list, m, i)
			m = m + 1
	Exchange(list, m, end)

	#Recursion
	QuickSort(list, start, m - 1)
	QuickSort(list, m + 1, end)

#Deal with duplicate condition
def QuickSort_Optimized(list, start, end):
	#Recursion end
	if start >= end:
		return

	#Choose the median from list[start], list[(start + end) / 2] and list[end] to improve QuickSort
	mid = Median(list, start, (start + end) / 2, end)
	Exchange(list, mid, end)

	#Divide list into two part, optimized for duplicate words
	p1 = start - 1
	p2 = start - 1
	for i in range(start, end):
		if list[i] < list[end]:
			p1 = p1 + 1
			p2 = p2 + 1
			if p1 == p2:
				Exchange(list, p2, i)
			else:
				Exchange(list, p2, i)
				Exchange(list, p1, p2)	#before list[p1] = last[last], it should be put into p2 place
		elif list[i] == list[end]:
			p2 = p2 + 1
			Exchange(list, p2, i)
	Exchange(list, p2 + 1, end)

	#Recursion
	QuickSort_Optimized(list, start, p1)
	QuickSort_Optimized(list, p2 + 2, end)
