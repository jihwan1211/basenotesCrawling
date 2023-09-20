import requests
from bs4 import BeautifulSoup

# # .txt 파일 경로 지정
# file_path = 'perfume_url.txt'

# # URL을 저장할 리스트 생성
# urls = []

# # .txt 파일에서 URL 읽어오기
# with open(file_path, 'r', encoding='utf-8') as file:
#     for line in file:
#         # 각 줄에서 줄바꿈 문자 및 공백 제거하여 URL 추출
#         url = line.strip()
#         if url:
#             urls.append(url)

# # URLs 리스트 확인
# print(urls)

response = requests.get('https://basenotes.com/fragrances/no-5-by-chanel.10210628', headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# spans = soup.select('span[class=h1_fragname]')
# 향수 이름
# name_span = soup.find('span', class_='h1_fragname')
# name = name_span.text

# 향수 이미지
# img_div= soup.find('div', class_='product_image')
# img = img_div.find('img')
# img_src = img.get('src')

# 탑 노트
# ul = soup.find('ul', class_='fragrancenotes')
# uls = ul.select("ul")
# # print(lis)

# for ul in uls:
#     a=ul.find('li')
#     words = a.text.split(',')
#     print(words)






# URL 리스트를 순회하며 크롤링
# for url in urls:
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             # 웹 페이지의 HTML 내용을 추출
#             html = response.text

#             # BeautifulSoup를 사용하여 HTML 파싱 및 원하는 데이터 추출
#             soup = BeautifulSoup(html, 'html.parser')
            
#             # 원하는 작업 수행 (예: 데이터 추출 또는 가공)

#             # 결과 출력 또는 다른 작업 수행
#             print(f'크롤링 성공: {url}')
#         else:
#             print(f'크롤링 실패: {url}, 응답 코드: {response.status_code}')
#     except Exception as e:
#         print(f'오류 발생: {url}, 오류 내용: {str(e)}')


# file_path = 'perfume_url.txt'

# with open(file_path, 'a', encoding='utf-8') as file:
#     for result in results:
#         file.write(result + '\n')  # 배열 내용을 파일에 쓰기

# print(f'결과가 {file_path}에 저장되었습니다.')
