import geoip2.webservice
import geoip2.records
import os
import webbrowser

#Grab the provided key (this is so people can't spam stuff easily on maxmind)
fileKey = open('key', 'r')
key = fileKey.readline().strip()
fileKey.close()

JSFile = open('map.js', 'r')
javascript = JSFile.readlines()
JSFile.close()

with geoip2.webservice.Client(658777, key, 'geolite.info') as client :
    try :
        response = client.city(input("Adresse IP : "))
        print(response.location.longitude)
        print(response.location.latitude)

        url = "codingglitch.github.io/school/geolite/map.html"
        url += "?longitude="+str(response.location.longitude)+"&latitude="+str(response.location.latitude)
        #url = os.getcwd().replace('\\','/') + '/map.html'
        print(url)
        webbrowser.open_new(url);
    except :
        print("Impossible de géolocaliser l'adresse IP")
    
