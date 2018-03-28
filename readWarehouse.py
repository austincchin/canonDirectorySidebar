	
	# [0] Icon Glyph
	# [1] District/Area
	# [2] Gender
	# [3] First name
	# [4] Last name
	# [5] Owner
	# [6] Age
	# [7] Special
	# [8] FC
	# [9] FC Valid?
	# [10] HGRPG Link

class Character:
	def __init__(self):
		self.area = "" 				# [1]
		self.gender = ""			# [2]
		self.first = "" 			# [3]
		self.last = ""				# [4]
		self.owner = "" 			# [5] 
		self.age = ""					# [6]
		self.special = ""			# [7]
		self.fc = ""					# [8]
		self.fcValid = ""			# [9]
		self.link = ""				# [10]

	def addArea(self, i):
		self.area = i

	def addFirst(self, i):
		self.first = i

	def addLast(self, i):
		self.last = i

	def addLink(self, i):
		self.link = i

def findURL(s):
	# <a href="http://hungergamesrpg.com/thread/80093/gillian-imberline-district-8" 
	s = s.strip()
	s = s.replace('thehungergamesrpg.proboards.com','hungergamesrpg.com')
	s = s.replace('www.hungergamesrpg.com','hungergamesrpg.com')
	add = False
	toReturn = ""
	slashCount = 0
	breakIt = False
	for c in s:

		if add:
			toReturn = toReturn + c

			if c == "/":
				slashCount += 1

				if slashCount == 5:
					toReturn = toReturn[:len(toReturn)-1]
					breakIt = True
					break

		if breakIt:
			break

		if c == '"':
			add = not add

	toReturn = toReturn.replace('"_blank"','')
	toReturn = toReturn.replace('?page=1','')
	toReturn = toReturn.replace('?page=2','')
	toReturn = toReturn.replace('?page=3','')

	return toReturn



if __name__ == "__main__":
	title = "tableContents.html"
	f = open(title,'r')
	gatherInfo = False
	charCount = 0
	tdCount = 0
	CharList = []
	charObject = None

	for line in f:
		l = line.strip()
		#print l

		if gatherInfo:
			if '<td>' in l:
				if tdCount == 1: #district/area
					l = line.replace('<td>','').replace('</td>','').strip()
					#print l
					charObject.addArea(l)
				
				if tdCount == 3: #firstname
					l = line.replace('<td>','').replace('</td>','').strip()
					#print l
					charObject.addFirst(l)
				if tdCount == 4: #lastname
					l = line.replace('<td>','').replace('</td>','').strip()
					#print l
					charObject.addLast(l)
				if tdCount == 10: #url
					l = line.replace('<td>','').replace('</td>','').strip()
					l = findURL(l)
					#print l
					charObject.addLink(l)


				tdCount += 1



		if l == '<tr>':
			gatherInfo = True
			tdCount = 0
			charObject = Character()

		if l == "</tr>":
			gatherInfo = False
			CharList.append(charObject)
			charCount += 1
	
		#x = raw_input()

	print "Char Number: " + str(charCount)
	print len(CharList)

	w = open("warehouseCSV.csv","w")

	for i in CharList:
		w.write("%s,%s,%s,%s\n" %(i.first,i.last,i.area,i.link))

	f.close()
	w.close()



