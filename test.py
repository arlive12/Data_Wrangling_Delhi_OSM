import xml.etree.cElementTree as ET
i=0
j=0
k=0
for _, element in ET.iterparse('delhi.osm'):
	if element.tag == 'node':
		i+=1
	elif element.tag == 'way':
		j+=1
	elif element.tag == 'nd':
		k+=1
print i
print j
print k