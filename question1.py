#	ID	1
#	Multiples of 3 and 5
#	Find the sum of all the multiples of 3 or 5
def MultiplesOf3And5(number=1000):
	MultiplesOf3And5 = 0
	for Counter in range(0, number, 3):
		MultiplesOf3And5 += Counter
	for Counter in range(0, number, 5):
		if Counter % 3 != 0:
			MultiplesOf3And5 += Counter
	return MultiplesOf3And5

print MultiplesOf3And5();