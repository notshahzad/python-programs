cons_nums=[]
temp=0
count=0
nums=[0,1,5,6,4,7,3,8,2,10]
for x in nums:
	for y in nums:
		if x<=y:
			count+=1
		else:
			count=0
		if count==len(nums):
			cons_nums.append(x)
			x=temp
while True:
	if temp in nums:
		temp+=1
	if temp not in nums:
		temp=temp-1
		break
cons_nums.append(temp)
print(cons_nums)