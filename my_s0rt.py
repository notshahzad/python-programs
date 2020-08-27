import random
import time
new_list=[]
recurssion=1
counter=0
list=[]
list_size=int(input("list_range:"))
for x in range(1,list_size):
	nums=random.randint(1,100)
	list.append(nums)
print(list)
time.sleep(1)
print("processing.....")
time.sleep(2)
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