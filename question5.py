#	Problem4: Largest palindrome product
#	A palindromic number reads the same both ways. 
#	The largest palindrome made from the product of two 2digit numbers is 9009 = 91 times 99
#	Find the largest palindrome made from the product of two 3-digit numbers

def LargestPalindromeProduct():
	subtractor1 = 1100	#every 1
	subtractor2 = 110	#every 10th
	subtractor3 = 11 	#every 100th
	palindromicNumb = 999999
	counter = 1

	while(palindromicNumb>100000):
		divider = 999 #reset divider
		while(divider>100):
			if(palindromicNumb%divider==0 and palindromicNumb/divider < 1000):
				return "Palindromic Number: " + str(palindromicNumb) + " with values of " + str(divider) +" and "+ str(palindromicNumb/divider) 
			divider-=1
		if(counter%10==0):
			if(counter%100==0):
				palindromicNumb -= subtractor3
			else:
				palindromicNumb -= subtractor2
		else:
			palindromicNumb -= subtractor1
		counter+=1

	return "ERROR: SUCH PALINDROMIC NUMBER NOT FOUND"

print LargestPalindromeProduct();