import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import os  # 파일 존재 여부 확인을 위해 추가

# .txt 파일 경로 지정
file_path = 'perfume_data_2.txt'
# file_path = 'p_url.txt'

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

# 기본 열 이름 정의
columns = ['id', 'image_src', 'name', 'top_notes', 'middle_notes', 'base_notes', 'notes']

dataList = []
# user-agent는 각자 컴퓨터에 맞는 걸로
purfume_id = 0
for url in urls:
    try:
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
        if response.status_code == 200:

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            # spans = soup.select('span[class=h1_fragname]')
            # 향수 이름
            name_span = soup.find('span', class_='h1_fragname')
            name = name_span.text

            # 향수 이미지
            img_div = soup.find('div', class_='product_image')
            img = img_div.find('img')
            img_src = img.get('src')

            # 노트들
            ul = soup.find('ul', class_='fragrancenotes')
            uls = ul.select("ul")
            if len(uls) == 1:
                note = uls[0].find('li')
                print(uls[0].text)
                notes = uls[0].text
                data = {
                    "id": purfume_id,
                    "image_src": img_src,
                    "name": name,
                    "notes": notes
                }
            else:
                for i in range(0, len(uls)):
                    note = uls[i].find('li')
                    # words = note.text.split(',')
                    if (i == 0):
                        top_notes = note.text
                    elif (i == 1):
                        middle_notes = note.text
                    else:
                        base_notes = note.text

                data = {
                    "id": purfume_id,
                    "image_src": img_src,
                    "name": name,
                    "top_notes": top_notes,
                    "middle_notes": middle_notes,
                    "base_notes": base_notes,
                    "notes": top_notes + middle_notes + base_notes
                }
            purfume_id += 1
            dataList.append(data)
            # print(dataList)
            print(data)

          # 일정 횟수(예: 200)마다 새로운 엑셀 파일로 저장
            if purfume_id % 200 == 0:
                # DataFrame 생성
                df = pd.DataFrame(dataList, columns=columns)

                # 'id' 열을 인덱스로 설정
                df.set_index('id', inplace=True)

                # 새로운 엑셀 파일로 저장
                excel_file_name = f'perfume_data_{7+purfume_id // 200}.xlsx'
                df.to_excel(excel_file_name, index=False)

                # dataList 비우기
                dataList = []

    except Exception as e:
        print(f'오류 발생: {url}, 오류 내용: {str(e)}')

# 남은 데이터를 엑셀 파일에 저장
if dataList:
    # DataFrame 생성
    df = pd.DataFrame(dataList, columns=columns)

    # 'id' 열을 인덱스로 설정
    df.set_index('id', inplace=True)

    # 마지막 엑셀 파일로 저장
    excel_file_name = f'perfume_data_{(purfume_id // 200) + 1}.xlsx'
    df.to_excel(excel_file_name, index=False)