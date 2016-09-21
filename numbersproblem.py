import itertools
def divideList(dividends,divisers):
	if len(dividends) == len(divisers):
		dividedValues = [x/y for x,y in zip(divisers,dividends)]
		return dividedValues
	return None

def checkResult(dividedValues):
	if sum(dividedValues) == 1:
		return 1,sum(dividedValues)
	return 0,sum(dividedValues)

def divideAndCheckResult(divisers,dividends):
	dividedValues = divideList(dividends,divisers)
	resultFound,sum = checkResult(dividedValues)
	if resultFound == 1:
		print("result found!!!!")
		print ("[",divisers,"]/[",dividends,"] = [",dividedValues,"] = sum [",sum,"]")
		#return 1	
	#swap dividends positions
	dtemp = dividends
	for i in range(len(dtemp) - 1):
		dtemp += [dtemp.pop(0)]
		dividedValues = divideList(dtemp,divisers)#[x/y for x,y in zip(divisers,dividends)]
		#print(divisers,"/",dividends,"=",dividedValues)
		resultFound,sum = checkResult(dividedValues)
		if resultFound == 1:
			print("result found!!!!")
			print ("[",divisers,"]/[",dividends,"] = [",dividedValues,"] = sum [",sum,"]")
			#return 1	

def main():
	numbers = [1,2,3,4,5,6,7,8,9]
	numbersPermutations = itertools.permutations(numbers,9)
	divisers = []
	dividends = []
	resultFound = 0
	noResult = 0
	for numberstemp in numbersPermutations:
		count = 1
		divisers = numberstemp[0:3]
		restNumbers = numberstemp[3:]
		#restNumbers = list (set(numberstemp).difference(set(divisers)))
		temp1 = restNumbers[0::2]
		temp2 = restNumbers[1::2]
		dividends = [(i*10)+j for i,j in zip(temp1,temp2)]
		dividentsReverse = [(i*10)+j for i,j in zip(temp2,temp1)]
		divideAndCheckResult(divisers,dividends)
		#swap digits in dividends
		divideAndCheckResult(divisers,dividentsReverse)

		#reset
		divisers = []
		dividends = []
		temp1 = []
		temp2 = []
		restNumbers = []
	print("~~~The END~~~")
if __name__ == "__main__":
	main()