import requests
import json
from pprint import pprint


actorlist = ['alicia witt','nathan fillion','richard dean anderson']


for actors in actorlist:
	actors.replace(" ", "+")
	geturl = ("http://www.myapifilms.com/imdb/idIMDB?name=%s&token=<API TOKEN>&format=json&language=en-us&filmography=1&exactFilter=0&limit=1&bornDied=0&starSign=0&uniqueName=0&actorActress=0&actorTrivia=0&actorPhotos=0&actorVideos=0&salary=0&spouses=0&tradeMark=0&personalQuotes=0&starMeter=0") % actors
	response = requests.get(geturl)
	data2 = response.json()
	for filmoger in data2['data']['names'][0]['filmographies']:
		print filmoger['section']
		if 'Act' in filmoger['section']:
			for filmog in filmoger['filmography']:
				addmovie = requests.get('http://localhost:5050/api/<CP API>/movie.add/?identifier=' + filmog['imdbid'])
				print  '\t',filmog['title'],'\t\t\t',filmog['remarks'],'\t', addmovie
