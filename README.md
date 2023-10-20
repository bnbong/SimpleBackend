# SimpleBackend
Python based simple CRUD Backend server using EFK stack and Jenkins.

This server was build for the purpose of learning backend architecture and CI/CD.
Other features can be added later(not sure).

# Backend Architecture
 - CI/CD - Jenkins
 - Backend - Python (FastAPI)
 - Reverse Proxy - Nginx
 - Database - MariaDB
 - Container - Docker
 - Logging - EFK (Elastic Search & Fluentd & Kibana)
 - Monitoring - Uptime Kuma & Heimdall

# CheckLists

- [ ] ElasticSearch 데이터 생명 주기 설정
- [ ] SSL 인증서 발급 및 Https 적용
- [ ] API 문서 작성 및 스키마 작성
- [ ] Jenkins CI/CD 파이프라인 작성 및 확인
- [ ] Scheduler worker 확인

# Application Documents
 - README [Link](./app/README.md)
 - Gitbook Link (will be added later)

# How to run
1. Clone this repository
2. Run `docker-compose up -d --build`

# How to contribute
1. Fork this repository
2. Create your feature branch
3. Go to application folder `cd application`
4. Run `python -m venv venv`
5. Install dependencies `pip install -r requirements.txt`
6. Commit your changes
7. Make sure your code is formatted by `black`
8. Make pull request

# 인프라 초기 설정

### Requirements
- Python 3.10 이상 버전
- Docker

## 1. docker compose 설정 및 실행

***비밀번호를 포함한 계정 정보는 주석처리 되어 있습니다. 초기 설정(비밀번호 생성 등) 이후 해당 계정을 다시 적용시켜야하므로 반드시 초기 실행에서는 주석 상태를 유지하세요.***

Default EFK stack Memory Limit - 2GB

```bash
docker compose up -d
```

## 2. 초기 설정

### 비밀번호 설정

도커 컨테이너에 접속하여 비밀번호를 설정합니다.
이때, 비밀번호는 ElasticSearch가 기본적으로 제공하는 기능을 활용하여 자동으로 비밀번호를 생성합니다.

```bash
docker exec -it <elasticsearch_container> /bin/bash
```

```bash
bash bin/elasticsearch-setup-passwords auto
```

***위 두번째 명령어의 출력 내용을 반드시 기록해두세요.***

## 3. 비밀번호 적용

### 실행중인 도커 컨테이너 중지

```bash
docker compose down
```

### 주석 처리 해제

`fluentd.conf`, `kibana.yml` 파일에서 주석 처리된 부분을 모두 해제한 후, 비밀번호를 입력합니다.

### 실행

```bash
docker compose up -d
```

# Jenkins 초기 설정

추가 예정
