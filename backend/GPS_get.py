
import googlemaps 
import requests
import json

class Locator(object):
	def __init__(self, home_mobile_country_code = None, 
		home_mobile_network_code = None, radio_type = None, 
		carrier = None, consider_ip = None, cell_towers = None, 
		wifi_access_points = None, locations = None):

		self.hbcc = home_mobile_country_code
		
		self.hbnc = home_mobile_network_code
	
		self.rtype = radio_type
	
		self.carrier = carrier
	
		self.consider_ip = consider_ip
	
		self.ctowers = cell_towers
	
		self.wifipt = wifi_access_points

		self.locations = locations

	'''def define_locate(self, home_mobile_country_code = None, 
		home_mobile_network_code = None, radio_type = None, 
		carrier = None, consider_ip = None, cell_towers = None, 
		wifi_access_points = None):

		self.hbcc = home_mobile_country_code
		
		self.hbnc = home_mobile_network_code
	
		self.rtype = radio_type
	
		self.carrier = carrier
	
		self.consider_ip = consider_ip
	
		self.ctowers = cell_towers
	
		self.wifipt = wifi_access_points'''

	'''def define_elevate(self, locations = None):
		if locations != None:
			self.locations = locations
	'''

def getPosition():
	#This is where the ip address would be
	userID = "192.168.1.1" #Obsolete at the moment
	key = "AIzaSyBO0wOgoe9pfBtB3TWwZwD0JOH_Yb_Ysd8"

	gmaps = googlemaps.Client(key=key)

	loc = Locator()

	#elevationLoc = (40.44,-79.947)

	#elevate = gmaps.elevation(elevationLoc)

	#location = gmaps.geolocate()
	location = makeRequest(loc)
	#except:
	#	print("Raised Query Limit Error")
	print("location:", location)
	position = (location['location']['lat'], location['location']['lng'])
	elevate = gmaps.elevation(position)
	print(elevate)

#getPosition()

def makeRequest(loc):
	URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="

	API_KEY = "AIzaSyBO0wOgoe9pfBtB3TWwZwD0JOH_Yb_Ysd8"

	data = {'homeMobileCountryCode':loc.hbcc,'homeMobileNetworkCode':loc.hbnc, 
	'radioType':loc.rtype, 'carrier':loc.carrier, 'considerIp':loc.consider_ip, 'cellTowers':loc.ctowers, 'wifiAccessPoints':loc.wifipt}

	r = requests.post(url= URL + API_KEY, data = json.dumps(data))

	locationData = r.json() #Converts desired return value to python type

	#print(pastebin_url)
	return locationData

#makeRequest()


getPosition()