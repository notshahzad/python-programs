import string
import time
message=(input("message:"))
lets=string.ascii_lowercase
letters=[]
upper_letters=[]
for letter in lets:
	letters.append(letter)
	upper_letters.append(letter.upper())
eord=input('press (E)for encryption and (D)for decryption:')
keys=13
if eord.lower()=="e":
	print("encrypting....")
if eord.lower()=="d":
	print("decrypting....")
	eord="e"
if eord.lower()=="e":
	time.sleep(1)
	for alphabets in message:
		if alphabets.isupper():
			if upper_letters.index(alphabets)<keys:
				case=upper_letters.index(alphabets)+keys
				print(upper_letters[case],end="")
			if upper_letters.index(alphabets)>=keys:
				case=upper_letters.index(alphabets)-keys
				print(upper_letters[case],end="")
		if alphabets.islower():
			if letters.index(alphabets)<keys:
				case=letters.index(alphabets)+keys
				print(letters[case],end="")
			if letters.index(alphabets)>=keys:
				case=letters.index(alphabets)-keys
				print(letters[case],end="")
print("\n")
