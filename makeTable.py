if __name__ == "__main__":
	w = open('table.html','w')
	f = open('warehouseCSV.csv',"r")

	currentA = "0"


	for line in f:
		l = line.strip().split(',')
		first = l[0]
		last = l[1]
		area = l[2]
		url = l[3]

		if area != currentA:
			w.write('</ul>\n\n')
			w.write('<div id="dirHeader"><strong>%s</strong></div>\n' %(area))
			w.write('<ul>\n')
			currentA = area

		w.write('\t<li><a href="%s">%s %s</a></li>\n' %(url,first,last))


		print l

