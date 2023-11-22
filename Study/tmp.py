from bing_image_downloader import downloader
import os

'''query_string: String to be searched.
limit: (optional, default is 100) Number of images to download.
output_dir: (optional, default is 'dataset') Name of output dir.
adult_filter_off: (optional, default is True) Enable of disable adult filteration.
force_replace: (optional, default is False) Delete folder if present and start a fresh download.
timeout: (optional, default is 60) timeout for connection in seconds.
verbose: (optional, default is True) Enable downloaded message.'''

query_list = ['박보검', '송중기', '차은우', '현빈', '김수현', '류준열', '박서준', '공유', '이병헌', '정우성']
for query in query_list:
    downloader.download(query, limit=1000,  output_dir=os.path.join('dataset', 'boy', 'full'), 
                        adult_filter_off=True, force_replace=False, timeout=60)