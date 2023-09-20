import requests
from bs4 import BeautifulSoup

results = []

for page in range(1, 1237):
    response = requests.get(f'https://basenotes.com/directory/?search=&type=fragrances&page={page}', headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
    if response.status_code == 200:
        print(page)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        a_tags = soup.select('div[id=searchresults] a')
        for a in a_tags:
            results.append(a.get('href'))
        # print(a.get('href'))
    else : 
        print(f'페이지 {page}에 대한 요청이 실패했습니다. 응답 코드: {response.status_code}')


# 결과를 .txt 파일에 저장
file_path = 'perfume_url.txt'

with open(file_path, 'a', encoding='utf-8') as file:
    for result in results:
        file.write(result + '\n')  # 배열 내용을 파일에 쓰기

print(f'결과가 {file_path}에 저장되었습니다.')


# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# ndu = soup.select('div[class=nduList]')
# for nduu in ndu:
#     nduuu = nduu.select('a')
#     strn = str(nduuu[0])
#     startIndex = strn.find('"')
#     endIndex = strn.find('"',startIndex+1)
#     print("https://www.fragrantica.com" + strn[startIndex+1:endIndex])