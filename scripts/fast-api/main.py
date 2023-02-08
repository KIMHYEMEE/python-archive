# ref: https://facerain.club/fast-api-tutorial-1/

# pip install fastapi
# pip install uvicorn


from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# 실행
## CMD에서 main 파일 위치 연결
## D 드라이브인 경우, `D:` 입력 후, cd를 통해 원하는 위치로 연결
##
## 실행명령
### uvicorn main:app --reload
##
## 결과 확인
### 링크: http://127.0.0.1:8000/items/5?q=test
### 결과: {"item_id":5, "q":"test"}
### 대화형 API: http://127.0.0.1:8000/docs