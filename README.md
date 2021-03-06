# datascience


다음을 숙지하고 데이터 분석을 하면 흐름을 이해할수 있어 무작정하는것보다 이해도가 높을수 있다.

#### 데이터 분석 순서
데이터 생성/수집 -> 데이터 저장 -> 전처리(통계분석, 시각화, Feature Engineer) ->기계학습(모델선정, 하이퍼파라미터 투닝, 데이터 학습) -> 오차분석(데이터 검증, 테스트 데이터, 잔차분석) -> 모델배포


1. Data Exploration 데이터 탐색(EDA)-> 2. Visualization 시각화를 통한 데이터 인사이트 얻기 -> 3. Feature Engineering 아웃라이어나 결측치 처리 -> 4. Modeling (DT, RF, XGB.. 등등 모델링 -> hyperparameter tuning) 및 학습 -> 5. Predict 정확도 

1. Data Exploration 데이터 탐색
- 필요한 라이브러리: pandas
- 참고: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

1.1. 데이터 읽기
- df = pd.read_csv("파일이름")

1.2. 데이터 내용 미리 보기
- df.head()
- df.tail()
- df.sample()

1.3. 컬럼종류보기
- df.columns

1.4. 요약정보 보기 -데이터 타입 및 결측치 확인
- df.info()

1.5. 행열의 갯수
- df.shape

1.6. 데이터의 기초통계량 확인
- df.describe()

1.7. 각 컬럼별 데이터 갯수
- df.count()

1.8 결측치 갯수 확인
df.isnull().sum()

1.9. 해당 컬럼의 데이터의 종류와 각 데이터 갯수
- df["컬럼이름"].value_counts()

ex. df["xyz_campaign_id"].value_counts()

1178    625

936     464

916      54

Name: xyz_campaign_id, dtype: int64






---------------------------------------

2. Visualization
- 필요한 라이브러리: matplotlib, seaborn
---------------------------------------
3. Feature Engineering
- 결측지, outliner제거
---------------------------------------
4. Modeling & Predict
- 학습시키는 방법(기본중에 기본)

4.1. clf - 분류기 로드
- from sklearn.ensemble import RandomForestClassifier
- rf_clf = RandomForestClassifier(n_estimators=100)

4.2. clf.fit - train데이터 셋 학습
- rf_clf.fit(x_train, y_train)

4.3. clf.predict - test데이터 예측
- y_pred = rf_clf.predict(x_test)

4.4. clf.score - 정확도 측정
- rf_clf.score(x_test, y_test)


