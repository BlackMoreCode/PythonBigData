# 데이터전처리 : 주어진 데이터를 분석에 적합하도록 가공하는 작업

import pandas as pd
import numpy as np
exam = pd.read_csv('exam.csv')
print(exam)

# query()를 사용해서 행제한 (조건에 맞는 행만 골라내기)
print(exam.query('nclass == 1')) # 1번인 클래스만 뽑아오기

print(exam.query('math > 50')) #조건문 사용; 수학 점수 50점 초과만 출력

# 1반이면서 수학 점수가 50점 이상 출력 (AND)
print(exam.query('nclass == 1 & math > 50'))

# 수학 점수가 90점 이상이거나 혹은 영어 점수가 90점 이상인 경우 출력 (OR)
print(exam.query('math >= 90 | english >= 90'))

# 필요한 변수만 추출하기 (열 제한)
print(exam['math'])

# 여러 열 출력
print(exam[['nclass', 'math', 'english']])

# 열 제거
print(exam.drop(columns='math'))

# 행 제한 query() 과 열제한 [] 조합하기
print(exam.query('nclass == 2')[['english', 'math']])

# 일부만 출력하기: 수학 점수가 50점 이상인 행만 추출한 다음, math 앞부분 5행까지 추출
print(exam.query('math >= 50')[['id', 'math']].head(8))

# 연습 문제: 11개의 컬럼 중에서 category(자동차 종류), cty(도시 연비) 추출해서 새로운 데이터 생성
mpg = pd.read_csv('mpg.csv')
new_mpg = mpg[['category', 'cty']]
print(new_mpg)

# 연습 문제 2: category(자동차 종류)가 'suv'인 자동차와 'compact'인 자동차중
# 어떤 자동차의 cty(도시 연비) 평균이 더 높은 것을 출력

# 데이터 프레임으로 읽기
df = pd.read_csv('mpg.csv')

# suv/compact 카테고리로 데이터프레임 필터링
suv_cty_mean = df[df['category'] == 'suv']['cty'].mean()
compact_cty_mean = df[df['category'] == 'compact']['cty'].mean()

# 결과 비교
if suv_cty_mean > compact_cty_mean:
    print("SUV의 도시 연비 평균이 더 높습니다:", suv_cty_mean)

else:
    print("Compact의 도시 연비 평균이 더 높습니다:", compact_cty_mean)


#연습문제 2 강사님 예시 (조금 더 쓰기 좋음)
suv = mpg.query('category == "suv"')['cty'].mean()
compact = mpg.query('category == "compact"')['cty'].mean()
if suv > compact:
    print(f"SUV : {suv}")
else:
    print(f"COMPACT : {compact}")

# 정렬하기
print(exam.sort_values('math', ascending=False)) #수학 성적 기준 오름차순 정렬

# 여러 정렬 기준 적용; 반별로 정렬하되, 성적은 높은순대로
print(exam.sort_values(['nclass', 'math'], ascending=[True, False]))

# 파생 변수 추가하기
# assign은 원본 데이터를 건드리지 않는다
exam.assign(total = exam['math'] + exam['english'] + exam['science'])
# print(exam) # 얘는 total 그러므로 보이지 않을 것이다. 실제로 없으니까.

# 이렇게 하면 원본 데이터를 변형한다
exam['total'] = exam['math'] + exam['english'] + exam['science']
print(exam)

# 데이터 변형 없이, 과학이 60점 이상이 참이면 pass, 아닐 시 fail
print(exam.assign(test = np.where(exam['science'] >= 60, 'pass', 'fail')))

# 체이닝 메서드 활용
print(exam.assign(total = exam['math'] + exam['english'] + exam['science']).sort_values('total', ascending=False))


# 연습문제 1
# mpg 데이터의 category는 자동차를 특징에 따라 ‘suv’, ‘compact’등 일곱 종류로 분류한 변수입니다.
# 어떤 차종의 도시 연비가 높은지 비교해 보려고 합니다. category별 cty 평균을 구해 보세요.
print(mpg['category'].unique())

suv = mpg.query('category == "suv"')['cty'].mean()
compact = mpg.query('category == "compact"')['cty'].mean()
midsize = mpg.query('category == "midsize"')['cty'].mean()
two_seater = mpg.query('category == "2seater"')['cty'].mean()
pickup = mpg.query('category == "pickup"')['cty'].mean()
minivan = mpg.query('category == "minivan"')['cty'].mean()
subcompact = mpg.query('category == "subcompact"')['cty'].mean()

print(suv, compact, midsize, two_seater, pickup, minivan, subcompact)

# 연습문제 2
# 앞 문제의 출력 결과는 category 값 알파벳순으로 정렬되어 있습니다.
# 어떤 차종의 도시 연비가 높은지 쉽게 알아볼 수 있도록 cty 평균이 높은 순으로 정렬해 출력하세요.
suv_list = mpg.query('category == "suv"')['cty']
print(suv_list.sort_values(ascending=False))

# 연습문제 3
# ‘어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려고 합니다.
# hwy 평균이 가장 높은 세 곳을 출력하세요.

print(mpg.groupby('manufacturer') \
.agg(mean_hwy = ('hwy', 'mean')) \
.sort_values('mean_hwy', ascending=False) \
.head(3))


# 연습문제 4
# 어떤 회사에서 ‘compact’ 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 회사별 ‘compact’ 차종 수를 내림차순으로 정렬해 출력하세요.

#방식 1
print(mpg.query('category == "compact"') \
  .groupby('manufacturer') \
  .agg(n = ('manufacturer', 'count')) \
  .sort_values('n', ascending=False))

#방식 2
print(mpg.query('category == "compact"') \
  .value_counts('manufacturer'))
