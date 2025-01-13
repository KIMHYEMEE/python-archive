# python-archive

## 1. plt에서 한글 깨짐 [링크](https://github.com/KIMHYEMEE/python-archive/blob/main/scripts/encoding_kor.py)
- matplotlib.pyplot 을 활용한 figure에서 한글이 깨져 보이는 경우 처리 방법
- 한글 글꼴로 설정
- 예시, '맑은 고딕'
## 2. xlsx 파일 내부 구성 방식 [링크](https://github.com/KIMHYEMEE/python-archive/blob/main/scripts/xlsx_formatting.py)
- 하나의 시트(sheet)에 여러개의 데이터프레임 넣기
- 시트(sheet) 내 string 입력하기
- 여러 개의 시트(sheet) 만들기
## 3. Fast API [링크](https://github.com/KIMHYEMEE/python-archive/tree/main/scripts/fast-api)
- fast API 서버 구현
- 주석 참고
## 4. 연속적으로 발생하는 값끼리 같은 인덱스 맵핑 [링크](https://github.com/KIMHYEMEE/python-archive/blob/main/scripts/seq_idx_mapping.py)
- 예: ['a','b','a','a','c','c','c'] -> [1,2,3,3,4,4,4]
## 5. Dynamic Time Warping (DTW) [링크](https://github.com/KIMHYEMEE/python-archive/blob/main/scripts/dtw.py)

![DTW 예제](https://github.com/hoon-bari/comments/assets/121400054/f3382a02-ffcb-48d7-ad2f-8f3423b5bc6a)

- 시계열 데이터 간 유사성 판단 지표. 두 시계열 간 길이가 달라도 비교할 수 있음. 단, 시작시점과 종료시점은 같은 패턴의 종료여야 함
- `distance`: 종점에서의 누적 거리 (정량적 유사도 값으로서 활용)
- `opt_path`: 두 시계열 데이터 간 같은 지점으로 정의된 위치(pair) 현황

### 5-1. Dynamic Time Warping Barycenter Averaging (DBA)
- DTW 개념을 활용하여 여러 시계열 데이터의 평균 산출

## 6. Scheduling 기본 알고리즘
### 6-1. WSPT (Weighted Shortest Processing Time first)
- `single machine`에서 `weighted completion time`을 목적함수로 하는 문제에서 이론적으로 증명 완료된 방법론 (`1||sum(wc)`, [WSPT 실행코드](./scripts/scheduling/wspt.py))

### 6-2. LPT (Longest Processing Time first)
- `parallel machines`에서 `makespan`을 목적함수로 하는 문제를 푸는 방법론 (`Pm||Cmax`, [LPT 실행코드](./scripts/scheduling/lpt.py))
- balancing the load over the various machines
- 최적을 보장하지 않지만, 실행이 빠름 (최적 대비 최대 33% 높은 목적함수 결과를 보임이 증명됨)

### 6.3 ILP (Integer Linear Programming)
- `parallel machines`에서 `makespan`을 목적함수로 하는 문제의 최적해를 산출하는 방법론 (`Pm||Cmax`, [ILP 실행코드](./scripts/scheduling/ilp.py))
- 최적임을 보장하지만, 작업 및 설비 수가 많아질수록 연산량이 기하급수적으로 늘어, 최적해를 얻는데 시간 소요가 많아짐