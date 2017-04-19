import csv
import math

def getCloseMarks(ticker):
	startLocation = "ClosingMarks\\"
	markReader = csv.DictReader(open(startLocation + ticker + 'close.csv', 'rb'))
	lineList = []
	
	for line in markReader:
	   lineList.append(line)
	
	closeMarkList =[]
	for item in lineList:
		closeMarkList.append(item['Close'])
	
	return closeMarkList


def CorrelationCalc (list1, list2):
	dailyReturnList = []
	dailyReturnList2 = []
	coVar =[]
	coVar2 =[]

	count = 0
	totDailyReturn = 0
	totDailyReturn2 = 0
	diffSquared = 0
	diffSquared2 = 0

	while count < (len(list1)-1):
		dailyReturnList.append((float(list1[count])/float(list1[count +1])-1))
		dailyReturnList2.append((float(list2[count])/float(list2[count +1])-1))
		totDailyReturn += (float(list1[count])/float(list1[count +1])-1)
		totDailyReturn2 += (float(list2[count])/float(list2[count +1])-1)
		count +=1

	averageReturn =	totDailyReturn/(len(list1)-1)
	averageReturn2 = totDailyReturn2/(len(list2)-1)

	#covarience formula 1/(n-1)E(Xi-Xavg)(Yi-Yavg)
	for item in dailyReturnList:
		diffSquared += (float(item) - averageReturn)**2
		coVar.append(float(item) - averageReturn)

	for item in dailyReturnList2:
		diffSquared2 += (float(item) - averageReturn2)**2
		coVar2.append(float(item) - averageReturn2)

	total = 0.0
	for i in range(0, len(coVar)):
		total += (coVar[i]*coVar2[i])

	covarience = total/len(coVar)

	varience = diffSquared/len(dailyReturnList)
	varience2 = diffSquared2/len(dailyReturnList2)
	stdDev = math.sqrt(varience)
	stdDev2 = math.sqrt(varience2)

	correlation = covarience/(stdDev*stdDev2)
	
	return correlation