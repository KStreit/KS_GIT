import csv

# Read in a pre stored CSV file with stock - sector - and industry
sectorReader = csv.DictReader(open('FullSavedComplete.csv', 'rb'))
stockSectorList = []
allStocks=[]

#putting each line of teh CSV in a list
#each line is a dictionatye
for line in sectorReader:
   stockSectorList.append(line)

#right now i'm not sure why one of the keys of the dictionary is a 
#blank space, will have to look into it, right now just removing it.	
for item in stockSectorList:
	allStocks.append(item['Stock'])
	
	
#Pulling out all of the industy titles for the list of dictionaries
#and putting them in thier own list	
industry_list =[]
StockDict ={}
for item in stockSectorList:
	#key = stockTicker
	#StockDict.setdefault(key,[])
	StockDict[item['Stock']]=item['Industry']
	industry_list.append(item['Industry'])
	

#Removing all the duplicates from the the list of industry
#storing them in a new list
finIndustryList=[]
seen = set()
for entry in industry_list:
	if entry not in seen:
		finIndustryList.append(entry)
		seen.add(entry)

#Creating a dictionary, the dictionary will store the industry names
#as keys, then insert each stock that matches the idustry as a value.
SECTORDICT ={}
for sector in finIndustryList:
	key = sector
	SECTORDICT.setdefault(key,[])
	
	for item in stockSectorList:
		if item['Industry']==sector:
			SECTORDICT[key].append(item['Stock'])
			