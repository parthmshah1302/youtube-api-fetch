'''
YouTube pageTokens repeat in some order - which are used to change pages
This function returns the first 100 page numbers
'''
import configparser
import urllib
import requests
import json

def getNextToken(pageToken):
    cfg=configparser.ConfigParser()
    cfg.read('youtubeAPI.config')
    api_key = cfg.get('KEYS', 'youtube_api', raw='')

    topic="cricket"
    args = {"q": topic,"key": api_key,"pageToken":pageToken}
    reqUrl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=date&{}'.format(urllib.parse.urlencode(args))
    response=requests.get(reqUrl).json()

    try:
        return response['nextPageToken']
    except KeyError as e:
        print(response)

# Seed condition: first page
nextPageToken=getNextToken('CDIQAA')

for i in range(9):
    open('pageTokens.csv', 'a').write(str(i)+': '+nextPageToken+'\n')
    nextPageToken=getNextToken(nextPageToken)
