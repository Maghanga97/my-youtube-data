import pandas as pd
import json
from tqdm import tqdm

def transform_data(json_file, category):	
	with open(json_file) as f:
		data = json.load(f)

	video_data = {'video_id': [], 'views': [], 'topic': []}
	for item in tqdm(data['items']):
		video_data['video_id'].append(item['id'])
		video_data['views'].append(int(item['statistics']['viewCount']))
		try:
			video_data['topic'].append(item['topicDetails']['topicCategories'][0])
		except:
			video_data['topic'].append('Null')
	data_frame = pd.DataFrame(video_data)
	excel_file = pd.ExcelWriter(f'excel/{category}.xlsx')
	data_frame.to_excel(excel_file)
	excel_file.save()

