from Tkinter import *
from AllTheSectorData import StockDict
from AllTheSectorData import SECTORDICT
from AllTheSectorData import allStocks
from CorrelationFunctions import *
import operator

class SectorGUI(Frame):
	
	def __init__(self, master):
	# initiates the frame
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.stockList =[]
		self.stockUniverse= allStocks
		self.stockToIndustry = StockDict
		self.findSectors = SECTORDICT
	
	def create_widgets(self):
		self.instruction = Label(self, text = "Enter The Underlying")
		
		self.instruction.grid(row = 0, column = 0, columnspan =2, sticky = W)
		
		self.stockEntry = Entry(self)
		self.stockEntry.grid(row =1, column = 1, sticky = W)
		
		self.submit_button = Button(self, text = "Submit", command = self.reveal)
		self.submit_button.grid(row = 2, column = 0, sticky = W)
		
		self.text = Text(self, width = 35, height = 25, wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
		
	def reveal(self):
		self.text.delete(0.0, END)
		
		content = self.stockEntry.get().upper()
		
		testDict ={}
		                                                                                            
		if content in self.stockUniverse: #if the stock exists
			contentCloseMarks = getCloseMarks(content)
			industry = self.stockToIndustry[content]
			for item in self.findSectors[industry]:
				itemCloseMarks = getCloseMarks(item)
				correl = CorrelationCalc(contentCloseMarks,itemCloseMarks)
				testDict[item] = correl
				
			sorted_tup = sorted(testDict.items(), key=operator.itemgetter(1))
			for item in sorted_tup:
				message = str(item)[1:-1] + '\n'
				self.text.insert(0.0, message)
			
		else:
			message = "ERROR"
			self.text.insert(0.0, message)
			
		



		
		