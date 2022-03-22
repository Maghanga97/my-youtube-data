from googleapiclient.discovery import build
import json

api_key = None
my_youtube_service = build('youtube', 'v3', developerKey=api_key)
request = my_youtube_service.videos().list(part='statistics, topicDetails', chart='mostPopular', videoCategoryId= '29', maxResults=30 )
response = request.execute()

with open('Nonprofits & Activism.json', 'w') as f:
	json.dump(response, f, indent=4)