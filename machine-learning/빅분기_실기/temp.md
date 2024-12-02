# pandas

##  1유형

* DataFrame.resample()
* `df.astype({'column name' : 'type'})` - 타입 변경

* 구간분할
  * `pd.cut` vs `pd.qcut`

* 결측값
  * 결측값 제거: `df.dropna()`
  * 결측값 변경
    * `df.fillna(df.mean())`
    * `df.fillna(df.median())`
    * `df.fillna(df.mode().iloc([0]))`
  * 참고: https://haeunning.tistory.com/12
  * 비율에 따른 랜덤 대치

### 꿀팁
* get_dummies
  * LabelEncoder, OneHotEncoding 대신 사용할 수 있는 함수
  * `pd.get_dummies(DataFrame, )`
    * NaN도 하나의 라벨 칼럼으로 처리해서 결측치 처리가 필요 없음.
  * `drop_first=True`면 LabelEncoder, 아니면 OneHotEncoder

##  2유형

### 범주형 데이터
어떤 범주형 데이터(열)에 대하여 train 데이터셋과 test 데이터셋 사이에 차집합이 있는 경우에는 두 데이터셋 간의 합집합을 만들 필요가 있음.

predict한 분류를 원복시켜야 하는 경우에는 `encoder.inverse_transform(y_pred)` 또는 `scaler.inverse_transform(y_pred)`