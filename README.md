# basenotesCrawling

https://basenotes.com/ 크롤링

1. purfume_url.py 로 모든 개별 향수의 url을 purfume_url.txt에 저장.

2.divide.py를 활용해 purfume_url.txt.를 여러개의 파일로 분할

2. purfume_info.py는 purfume_url.txt를 읽어서 각 향수의 이름, 사진, 탑노트, 미들노트, 베이스노트를 엑셀에 저장한다.
   현재는 dataList배열에 data를 저장해서 마지막에 한 번에 엑셀에 저장하려고 하는데 이렇게 하면 잘 안 돼서 매 Loop마다 저장하도록 수정해야할 것 같음.
