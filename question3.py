#	Problem 3: Largest prime factor
#	The prime factors of 13195 are 5, 7, 13 and 29.
#	What is the largest prime factor of the number 600851475143

primeNumblist = []

def generateNextPrimeNumber(primenumb):
	primeNumb = primenumb

	while(1==1):
		primeNumb +=1
		for element in primeNumblist:
			if primeNumb%element==0:
				break
			else:
				primeNumblist.append(primeNumb)
				return primeNumb


def LargestPrimeFactor():
	number = 600851475143
	nextPrimeNumber = 2
	primeNumblist.append(nextPrimeNumber)

	while(1==1):
		# if divisible then take the new number and continue 
		if number%nextPrimeNumber==0:
			number  = number/nextPrimeNumber
		
		if(number<nextPrimeNumber):
			break

		nextPrimeNumber = generateNextPrimeNumber(nextPrimeNumber)

	return primeNumblist

# print out list of prime factors
print LargestPrimeFactor();

