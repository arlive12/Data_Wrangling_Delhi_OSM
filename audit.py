import csv
OSMFILE = "delhi.osm"
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Bazaar","Chowk","Circle","Complex","Delhi","Enclave"
            "Bagh", "Road","Marg","Estate","Extension","Flyover","Gate","Flyover","Gate","Market","Nagar","Okhla","Paharganj","Path","Pusta","Shakarpur",
            "Wali","Bagh","Enclave","Lines","1","147","23","24","6","S1","NIT",""]

mapping = { 
            "gate": "Gate",
            "Delhi.": "Delhi",
            "Extn" : "Extension",
            "Janpath" : "Janpath Lane",
            "colony" : "Colony",
            "gate" : "Gate",
            "lane" : "Lane",
            "marg" : "Marg",
            "road" : "Road",
            "colony" : "Colony",
            "moti" : "Moti",
}

nodes_tags_updated = open('nodes_tags_updated.csv','wb')
node_tags_original = open('nodes_tags.csv','rbw')
ways_tags_original = open('ways_tags.csv','rbw')
ways_tags_updated = open('ways_tags_updated.csv','wb')

reader_nodes_tags = csv.reader(node_tags_original)
reader_ways_tags = csv.reader(ways_tags_original)

writer_nodes_tags = csv.writer(nodes_tags_updated)
writer_ways_tags = csv.writer(ways_tags_updated)

def audit_node_tags():
	for row in reader_nodes_tags:
		if True:
			if row[1] == 'state':   # removing the inconsistencies in key value state where some values were DL , NCR , Delhi
				row[2] = 'Delhi'
			if row[1] == 'source' and row[2] == 'sourvey':
				row[2] = 'survey'
			if row[1] == 'street':
				value = row[2]
				value1 = row[2].split(' ')
				street_name =  value1[len(value1)-1]
				if street_name not in expected:
					row[2] = mapping[street_name]
			if row[1] == 'postal_code':
				row[1] = 'postcode'

			if row[1] =='country' and row[2] == 'India':
				row[2] = 'IN'
			writer_nodes_tags.writerow(row)


					

def audit_ways_tags():
	for row in reader_ways_tags:
		if row[1] == 'source':
			if row[2] == 'bing' or row[2] == 'Bing' or row[2] == 'Bing 2012':
				row[2] = 'Bing'
			
		if row[1] == 'street':
			value = row[2]
			value1 = row[2].split(' ')
			street_name =  value1[len(value1)-1]
			if street_name not in expected:
				row[2] = mapping[street_name]
				row[2] = mapping[street_name]
		if row[1] == 'postal_code':
			row[1] = 'postcode'
		writer_ways_tags.writerow(row)
				


audit_node_tags()
audit_ways_tags()