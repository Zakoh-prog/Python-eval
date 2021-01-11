#File Overlap
prime = open("primenumbers.txt", "r")
happy = open("happynumbers.txt", "r")
happy_list = happy.readlines()
result = list()

for line in prime:
	if line in happy_list:
		result.append(line.strip() )

prime.close()
happy.close()

print (result)