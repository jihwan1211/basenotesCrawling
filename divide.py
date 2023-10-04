# 입력 파일 경로
input_file = 'perfume_url.txt'

# 분할된 파일의 기본 이름
output_file_base = 'perfume_data'

# 분할 크기
batch_size = 2000

def split_file(input_file, output_file_base, batch_size):
    with open(input_file, 'r', encoding='utf-8') as input_f:
        data = input_f.readlines()
    
    num_batches = len(data) // batch_size + 1
    
    for batch_num in range(num_batches):
        start_idx = batch_num * batch_size
        end_idx = (batch_num + 1) * batch_size
        batch_data = data[start_idx:end_idx]
        
        # 분할된 파일 이름 설정
        output_file = f'{output_file_base}_{batch_num + 1}.txt'
        
        # 분할된 데이터를 새로운 파일에 저장
        with open(output_file, 'w', encoding='utf-8') as output_f:
            output_f.writelines(batch_data)

if __name__ == "__main__":
    split_file(input_file, output_file_base, batch_size)
