rev_type=input("type some shit:")
list2=[' ',rev_type]
list=" ".join(list2)
count=0
for alphabts in list:
	if alphabts==" ":
		count+=1
tem=count
while tem>=count:
	count=0
	for alphabts in list:
		if alphabts==" ":
			count+=1
		if count==tem:
			print(alphabts,end="")
	tem-=1
	count=0