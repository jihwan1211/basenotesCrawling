# basenotesCrawling

https://basenotes.com/ 크롤링

1. purfume_url.py 로 모든 개별 향수의 url을 purfume_url.txt에 저장.

2.divide.py를 활용해 purfume_url.txt.를 여러개의 파일로 분할

3. purfume_info.py는 purfume_url.txt를 읽어서 각 향수의 이름, 사진, 탑노트, 미들노트, 베이스노트를 엑셀에 저장한다.
   200개마다 dataList를 비우고 새로운 엑셀 파일로 저장을 시도하는데 분할 batch를 2000개로 할때 1200개까지는 잘 됐는데 그 이후부터 안 됐음
   purfume_url.txt의 분할을 1200개씩으로 수정.
   수정 후에 시도했는데도 안 됐음.
