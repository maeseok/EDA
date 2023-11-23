from bing_image_downloader import downloader
import os

'''query_string: String to be searched.
limit: (optional, default is 100) Number of images to download. - 사진 개수
output_dir: (optional, default is 'dataset') Name of output dir. - 폴더 이름
adult_filter_off: (optional, default is True) Enable of disable adult filteration. - 성인 필터
force_replace: (optional, default is False) Delete folder if present and start a fresh download. - 기존 사진 삭제 여부
timeout: (optional, default is 60) timeout for connection in seconds.
verbose: (optional, default is True) Enable downloaded message. - 다운로드 메시지''' 

query_list = [ '송중기', '류준열', '박서준', '공유', '정우성']
for query in query_list:
    downloader.download(query, limit=30,  output_dir=os.path.join('인물사진'), 
                        adult_filter_off=True, force_replace=False, timeout=60)