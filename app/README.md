# Simple FastAPI application
Back-end Architecture가 정상적으로 구성이 되었는지를 확인하는 용도로 제작된

간단한 CRUD 기능을 하는 FastAPI 기반의 백엔드 서버입니다.

## Application Stack
- Python 3.10.10
- FastAPI (with SQLAlchemy, pymysql)
- MariaDB
- Docker

## API Documents
Gitbook Link will be uploaded later.

## Database Schema
ERD will be uploaded later.

## How to run
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

```bash
# Poetry 환경이 로컬에 설치되어 있다면,
poetry install
```

### 2. Run server in your local
```bash
uvicorn app.main:app --reload
```

### 3. Access to API endpoint
API 서버가 정상적으로 작동이 되는지 다음 URL에 요청을 보내 확인할 수 있습니다.
```bash
curl http://localhost:8000/api/v1/ping
```

## TODO

- [X] 비동기 API endpoint update
- [X] Dockerize
- [ ] 컨테이너 동작 테스트
- [ ] Poetry 적용 테스트
