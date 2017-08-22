import urllib2, json
addr = raw_input()
addr = addr.replace(' ','+')
api_key = '' #ADD YOUR GOOGLE API KEY HERE
address = 'https://maps.googleapis.com/maps/api/geocode/json?address='+addr+'&key='+api_key
response = urllib2.urlopen(address)
j = json.load(response)
lat,lon = j['results'][0]['geometry']['location']['lat'],j['results'][0]['geometry']['location']['lng']
print "Address Coordinates: " + str(lat),str(lon)
antilat = 0 -lat
if lon<0:
	antilon = 0 - lon
	antilon =(180-antilon)
else:
	antilon = 0-(180-lon)
print "Antipode Coordinates : "+ str(antilat),str(antilon)


