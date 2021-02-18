# datascience


다음을 숙지하고 데이터 분석을 하면 흐름을 이해할수 있어 무작정하는것보다 이해도가 높을수 있다.

#### 데이터 분석 순서
1. Data Exploration 데이터 탐색
- 필요한 라이브러리: pandas
- 참고: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

1.1. 데이터 읽기
- df = pd.read_csv("파일이름")

데이터 내용 미리 보기
df.head()
df.tail()
df.sample()

컬럼종류보기
df.columns

요약정보 보기 -데이터 타입 및 결측치 확인
df.info()

행열의 갯수
df.shape

데이터의 기초통계량 확인
df.describe()

각 컬럼별 데이터 갯수
df.count()

해당 컬럼의 데이터의 종류와 각 데이터 갯수
df["컬럼이름"].value_counts()
ex. df["xyz_campaign_id"].value_counts()
1178    625
936     464
916      54
Name: xyz_campaign_id, dtype: int64







3. Visualization
4. Feature Engineering
5. Modeling
6. Predict

- 학습시키는 방법(기본중에 기본)
1. clf - 분류기 로드
2. clf.fit - train데이터 셋 학습
3. clf.predict - test데이터 예측
4. clf.score - 정확도 측정


