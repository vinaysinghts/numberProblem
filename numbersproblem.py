def divideList(dividends,divisers):
	if len(dividends) == len(divisers):
		dividedValues = [x/y for x,y in zip(divisers,dividends)]
		return dividedValues
	return None

def checkResult(dividedValues):
	if sum(dividedValues) == 1:
		return 1
	return 0

def main():
	numbers = [1,2,3,4,5,6,7,8,9]
	numberstemp = numbers
	divisers = []
	dividends = []
	resultFound = 0
	noResult = 0
	while resultFound != 1 or noResult != 1:
		count = 1
		for i in numberstemp:
			divisers += [i]
			if count == 3:
				break
			count += 1
		restNumbers = list (set(numberstemp).difference(set(divisers)))
		temp1 = restNumbers[0::2]
		temp2 = restNumbers[1::2]
		dividends = [(i*10)+j for i,j in zip(temp1,temp2)]
		dividentsReverse = [(i*10)+j for i,j in zip(temp2,temp1)]
		
		dividedValues = divideList(dividends,divisers)#[x/y for x,y in zip(divisers,dividends)]
		print(divisers,"/",dividends,"=",dividedValues)
		resultFound = checkResult(dividedValues)
		if resultFound == 1:
			print("result found!!!!")
			print ("sum [",sum(dividedValues),"]")
			return 1	
			
		#swap dividends positions
		dtemp = dividends
		for i in range(len(dtemp) - 1):
			dtemp += [dtemp.pop(0)]
			dividedValues = divideList(dtemp,divisers)#[x/y for x,y in zip(divisers,dividends)]
			print(divisers,"/",dividends,"=",dividedValues)
			resultFound = checkResult(dividedValues)
			if resultFound == 1:
				print("result found!!!!")
				print ("sum [",sum(dividedValues),"]")
				return 1	

		#swap digits in dividends
		dividedValues = divideList(dividentsReverse,divisers)#[x/y for x,y in zip(divisers,dividends)]
		print(divisers,"/",dividends,"=",dividedValues)
		resultFound = checkResult(dividedValues)
		if resultFound == 1:
			print("result found!!!!")
			print ("sum [",sum(dividedValues),"]")
			return 1
		
		dtemp = dividentsReverse
		for i in range(len(dtemp) - 1):
			dtemp += [dtemp.pop(0)]
			dividedValues = divideList(dtemp,divisers)#[x/y for x,y in zip(divisers,dividends)]
			print(divisers,"/",dividends,"=",dividedValues)
			resultFound = checkResult(dividedValues)
			if resultFound == 1:
				print("result found!!!!")
				print ("sum [",sum(dividedValues),"]")
				return 1	
		
		#swap all numbers to begin with new combination
		numberstemp = temp2 + temp1 + divisers
		#numberstemp += [numberstemp.pop(0)]
		if numberstemp == numbers:
			print("no result found")
			noResult = 1
		print(numberstemp)
		#reset
		divisers = []
		dividends = []
		temp1 = []
		temp2 = []
		restNumbers = []

if __name__ == "__main__":
	main()