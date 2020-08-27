def sort(list):
	new_list=[]
	recurssion=1
	counter=0
	q=len(list)
	while recurssion<=q:
		for xx in list:
			for yy in list:
				if xx<=yy:
					counter+=1
					if counter == len(list):
						new_list.append(xx)
						list.remove(xx)
				else:
					counter=0	
		recurssion+=1
	for x in list:
		new_list.append(x)
		list.remove(x)
	print(new_list)
lest=[11,2,5,3,6]
sort(lest)