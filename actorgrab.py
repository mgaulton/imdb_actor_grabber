import requests
import json
from pprint import pprint


actorlist = ['alicia witt','nathan fillion','richard dean anderson']


for actors in actorlist:
	actors.replace(" ", "%20")
	geturl = ("http://www.myapifilms.com/imdb?name=%s&format=JSON&filmography=1&limit=1&lang=en-us&exactFilter=0&bornDied=0&starSign=0&uniqueName=0&actorActress=0&actorTrivia=0&actorPhotos=N&actorVideos=N&salary=0&spouses=0&tradeMark=0&personalQuotes=0") % actors
	response = requests.get(geturl)
	data = response.json()

	for filmog in data[0]['filmographies'][0]['filmography']:
		print filmog['IMDBId']
		if 'remarks' not in filmog:
			addmovie = requests.get('http://localhost:5050/api/<api key/movie.add/?identifier=' + filmog['IMDBId'])
			print addmovie
		else:
			 if ( '(TV Movie)' in filmog['remarks'] or '(TV Mini-Series)' in filmog['remarks'] ):
			 	addmovie = requests.get('http://localhost:5050/api/<api key'/movie.add/?identifier=' + filmog['IMDBId'])
			 	print addmovie
			
