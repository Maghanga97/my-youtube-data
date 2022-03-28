from googleapiclient.discovery import build
import json

class YoutubeFetch():
	api_key = None
	my_youtube_service = build('youtube', 'v3', developerKey=api_key)

	def generate_url(self):
		url = f"https://www.googleapis.com/youtube/v3/search?q=racism&part=snippet&regionCode=US&publishedAfter=2009-08-31T07:01:57Z&publishedBefore=2019-08-31T07:01:57Z&type=channel&maxResults=50&key={api_key}"
		return url

	def fetch_by_keyword(self, keyword):
		request = my_youtube_service.search().list(q=keyword,part='id', type='channel', regionCode='US', order='rating', maxResults=50)
		response = request.execute()
		with open(f'{keyword} search results.json', 'w') as f:
			json.dump(response, f, indent=4)

	def fetch_videos_by_category(self, category):
		request = my_youtube_service.videos().list(part='statistics, snippet', categoryId=category, regionCode='US', maxResults=50)
		response = request.execute()
		with open(f'video results.json', 'w') as f:
			json.dump(response, f, indent=4)

	def fetch_channel_stats(self, main_list):
		channel_stats = []
		for item in main_list:
			for channel in item:
				request = my_youtube_service.channels().list(part='statistics', id=channel)
				response = request.execute()
				channel_stats.append(response)
		return channel_stats


	def fetch_channel_data(self, channels):
		stats = []
		for channel in channels:
			request = my_youtube_service.channels().list(part='statistics, snippet', id=channel)
			response = request.execute()
			stats.append(response)
		return stats

	def fetch_single_channel(self, channel_id):
		request = my_youtube_service.channels().list(part='statistics, snippet', id=channel_id)
		response = request.execute()
		with open('Channels.json', 'w') as f:
			json.dump(response, f, indent=4)


