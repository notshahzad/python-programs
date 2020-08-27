import time
counter=0
name=input(("first_name:"))
name2=input("second_name:")
list_name=[name," ",name2]
print("processing...")
time.sleep(2)
for word in list_name:
	for alphbt in word:
		if counter==0:
			alphbt=alphbt.swapcase()
		if counter>0:
			if alphbt=="a":
				alphbt="4"
			if alphbt=="e":
				alphbt="3"
			if alphbt=="o":
			    alphbt="0"
			if alphbt==" ": 
			    alphbt="_"
			    counter=-1
		counter+=1
		print(alphbt,end="")