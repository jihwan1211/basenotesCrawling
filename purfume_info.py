import requests
from bs4 import BeautifulSoup

# .txt 파일 경로 지정
file_path = 'perfume_url.txt'

# URL을 저장할 리스트 생성
urls = []

# .txt 파일에서 URL 읽어오기
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 각 줄에서 줄바꿈 문자 및 공백 제거하여 URL 추출
        url = line.strip()
        if url:
            urls.append(url)

# URLs 리스트 확인
# print(urls)

# user-agent는 각자 컴퓨터에 맞는 걸로
purfume_id = 0
for url in urls:
    try:
        response = requests.get(url, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
        if response.status_code == 200:
   
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
    # spans = soup.select('span[class=h1_fragname]')
            # 향수 이름
            name_span = soup.find('span', class_='h1_fragname')
            name = name_span.text

    # 향수 이미지
            img_div= soup.find('div', class_='product_image')
            img = img_div.find('img')
            img_src = img.get('src')

    # 노트들
            ul = soup.find('ul', class_='fragrancenotes')
            uls = ul.select("ul")

            for i in range(0, len(uls)):
                note = uls[i].find('li')
                words = note.text.split(',')
                if(i==0): 
                    top_notes = words
                elif(i==1): 
                    middle_notes = words
                else: 
                    base_notes = words
    
            data= {"id": purfume_id,
                   "image_src": img_src, 
                   "name": name, 
                   "top_notes": top_notes, 
                   "middle_notes": middle_notes, 
                   "base_notes": base_notes}
            purfume_id += 1
            print(data)

    except Exception as e:
        print(f'오류 발생: {url}, 오류 내용: {str(e)}')



# file_path = 'perfume_info.txt'

# with open(file_path, 'a', encoding='utf-8') as file:
#     for result in results:
#         file.write(result + '\n')  # 배열 내용을 파일에 쓰기

# print(f'결과가 {file_path}에 저장되었습니다.')
