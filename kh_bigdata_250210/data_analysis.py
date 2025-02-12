# data_analysis.py
import csv


def get_gender_data(region, csv_path='./gender.csv'):
    """
    주어진 지역(region)에 해당하는 남녀 인구 데이터를 CSV 파일에서 읽어 반환합니다.

    :param region: 검색할 지역 문자열
    :param csv_path: CSV 파일 경로 (기본값: './gender.csv')
    :return: {'male': [남성 인구 데이터], 'female': [여성 인구 데이터]}
    """
    male_data = []
    female_data = []

    with open(csv_path, encoding='cp949') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # CSV 파일의 첫번째 컬럼에 지역명이 포함되어 있다면 데이터를 추출
            if region in row[0]:
                # 남성 데이터: 인덱스 3부터 103까지, 음수로 변환 (차트 그리기를 위해)
                male_data = [-int(i) for i in row[3:104]]
                # 여성 데이터: 인덱스 106부터 끝까지
                female_data = [int(i) for i in row[106:]]
                break  # 해당 지역을 찾으면 반복 종료

    return {'male': male_data, 'female': female_data}
