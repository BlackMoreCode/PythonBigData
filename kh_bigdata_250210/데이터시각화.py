import matplotlib.pyplot as plt # 데이터 시각화에서 가장 많이 사용되는 라이브러리; 여기에서 pyplot 모듈을 가져온다
from statsmodels.genmod.families import Family

# plt.plot([10, 20, 30, 40]) # y축 데이터 (수직 방향); x축 값을 지정하지 않을시 0부터 값 시작하는 방향으로 자동생성
# plt.show()

# plt.plot([10, 20, 30, 40, 50, 60, 70], [10, 43, 25, 15, 10, 10, 0]) # x축, y축; 2개다 넣을시 x,y 순으로
# plt.show()

# 그래프 옵션
plt.rc("font", family='Malgun Gothic') # 윈도우용 한글 폰트 지정 예시
plt.title("제목 추가하기")
plt.plot([10, 20, 30, 40], label="X축", color='skyblue')
plt.plot([23, 45, 5, 55], label="Y축", color='pink')
# 범례 추가하기
plt.legend()

plt.show()