# speech_to_text_dir.py는 directory에 있는 파일들에 whisper를 적용하여 txt파일들을 만들고, 한문장씩 추출하여 한줄에 나타내는 함수입니다.

import whisper
import subprocess
import os
import re
import time

# directory에 있는 파일들의 이름을 불러와 리스트에 저장하는 함수
def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_list.append(filename)
    return file_list


# whisper을 통해 txt 파일을 생성하는 함수
def speech_to_text(input_data, output_path):

    model_size = "medium" # 모델의 크기를 결정하는 부분 (tiny, small, medium, large 등) (customize)

    model = whisper.load_model(model_size)
    result = model.transcribe(input_data)

    # 파일 쓰기
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result["text"])



# txt파일을 문장단위로 전처리 해주는 함수
def merge_and_split(input_file, output_file):
    lines=list()
    with open(input_file, 'r') as infile:
        for line in infile:
            lines.append(line.rstrip('\n'))

    # 여러 줄을 하나의 텍스트로 합침
    merged_text = ' '.join(lines)

    # ".?"을 기준으로 나눔
    sentences = re.split(r'[.?]+',merged_text)  # 구분자를 정의하는 부분 (customize)

    with open(output_file, 'w') as outfile:
        for sentence in sentences:
            outfile.write(sentence.strip() + '\n')



# 초단위의 시간을 시, 분, 초로 나타내주는 함수
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

# directory에 있는 파일들의 이름을 list에 저장하는 부분
input_path = '/home/elicer/practice/speech_data/wave/'  # input data들이 있는 directory 지정 (customize)
input_datas = get_file_list(input_path)

# Main
# 프로그램 runtime 계산
start_time = time.time()

for input_data in input_datas:
    m_start_time = time.time()

    input_data_ = input_path + input_data
    output_path = '/home/elicer/practice/speech_data/txt/' + input_data + '.txt'  # output data들을 저장할 directory 지정 (txt 파일) (customize)
    output_filename_rm = '/home/elicer/practice/speech_data/txt/' + input_data + '_rm.txt' # txt파일에서 merge_and_split 함수 적용한 결과 저장할 directory 지정 (customize)

    speech_to_text(input_data_, output_path)
    
    merge_and_split(output_path, output_filename_rm)

    m_end_time = time.time()
    m_run_time = m_end_time - m_start_time
    m_hours, m_minutes, m_seconds = format_time(m_run_time)
    print(input_data,"is done.", f"[{m_hours}:{m_minutes}:{m_seconds}]")

end_time = time.time()
run_time = end_time - start_time
hours, minutes, seconds = format_time(run_time)
print(f"total run time: {hours}:{minutes}:{seconds}.")