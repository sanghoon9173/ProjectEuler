#	Problem4: Largest palindrome product
#	A palindromic number reads the same both ways. 
#	The largest palindrome made from the product of two 2digit numbers is 9009 = 91 times 99
#	Find the largest palindrome made from the product of two 3-digit numbers

def LargestPalindromeProduct():
	subtractor1 = 1100	#every 1
	subtractor2 = 110	#every 10th
	subtractor3 = 11 	#every 100th
	divider = 999

	while(divider>100):
		counter=1
		palindromicNumb = 999999
		while(1==1):
			if(palindromicNumb%divider==0 and palindromicNumb/divider < 1000):
				return "Palindromic Number: " + str(palindromicNumb) + " with values of " + str(divider) +" and "+ str(palindromicNumb/divider) 
			if(counter%10==0):
				if(counter%100==0):
					palindromicNumb -= subtractor3
				else:
					palindromicNumb -= subtractor2
			else:
				palindromicNumb -= subtractor1
			if(palindromicNumb<100000):
				break
			print palindromicNumb
			counter+=1
		divider-=1

	return "ERROR: SUCH PALINDROMIC NUMBER NOT FOUND"

print LargestPalindromeProduct();