list=[9,2,7,4,6,7]
count=0
list.sort()
for x in list:
	for y in list:
		if x==y:
			count+=1
			if count>1:
				print(x,"found at:",list.index(x)+1)
				for q in list:
					if q==x:
						list.remove(q)
		else:
			count=0