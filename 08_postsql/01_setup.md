# PostgreSQL 설치 가이드 (Direct Installation)

이 가이드는 Docker를 사용하지 않고 운영체제에 직접 PostgreSQL을 설치하는 방법을 설명합니다.

---

## 💻 1. Windows

Windows 환경에서는 EnterpriseDB에서 제공하는 공식 인스톨러를 사용하는 것이 가장 쉽습니다.

### 설치 단계
1. **다운로드**:
   - [EnterpriseDB 다운로드 페이지](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)에 접속합니다.
   - Windows x86-64 버전용 최신 PostgreSQL 인스톨러를 다운로드합니다.
2. **인스톨러 실행**:
   - 다운로드한 `.exe` 파일을 실행합니다.
   - 기본 설정으로 'Next'를 계속 누릅니다.
   - **설치 구성요소**: PostgreSQL Server, pgAdmin 4 (GUI 툴), Stack Builder (추가 도구), Command Line Tools 모두 체크된 상태로 둡니다.
   - **데이터 디렉토리**: 기본 경로에 둡니다.
   - **비밀번호 설정 (매우 중요!)**: 최고 관리자 계정인 `postgres` 사용자의 비밀번호를 입력합니다. 이 비밀번호는 반드시 기억해야 합니다.
   - **포트 번호 (Port)**: 기본값인 `5432`를 유지합니다.
3. **설치 완료**:
   - 설치가 완료되면 psql(커맨드라인)이나설치된 pgAdmin 4를 실행하여 `postgres` 계정과 설정한 비밀번호로 데이터베이스에 접속할 수 있습니다.

---

## 🐧 2. Ubuntu (Linux)

Ubuntu에서는 공식 APT 패키지 매니저를 사용하여 간단하게 설치할 수 있습니다.

### 설치 단계
1. **패키지 목록 업데이트**:
   터미널을 열고 다음 명령어를 실행합니다.
   ```bash
   sudo apt update
   ```
2. **PostgreSQL 설치**:
   PostgreSQL 본체와 추가 유틸리티(contrib)를 함께 설치합니다.
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```
3. **설치 확인 및 서비스 상태 확인**:
   설치가 완료되면 서비스가 자동으로 실행됩니다. 상태를 확인해 봅니다.
   ```bash
   sudo systemctl status postgresql
   ```
4. **접속 테스트 및 비밀번호 설정 (매우 중요!)**:
   기본적으로 Ubuntu 시스템 사용자 `postgres`가 생성되며, 초기에는 비밀번호가 없습니다.
   DB 클라이언트(DBeaver 등)에서 외부 접속을 하려면 반드시 비밀번호를 설정해야 합니다.
   ```bash
   # 1. postgres 사용자로 전환하여 psql 쉘 접속
   sudo -i -u postgres psql
   ```
   psql 쉘에 접속한 상태(프롬프트가 `postgres=#` 모양일 때)에서 아래 명령어를 입력하여 비밀번호를 설정합니다.
   ```sql
   -- 2. 비밀번호 설정 (원하는 비밀번호 입력 후 엔터)
   \password postgres
   ```
   > 💡 비밀번호 설정이 끝났으면 `\q` 를 입력하고 엔터를 눌러 psql 쉘을 종료합니다.

---

## 🍏 3. macOS

macOS에서는 패키지 관리자인 `Homebrew`를 사용하거나, `Postgres.app`이라는 맥 전용 앱을 사용하는 두 가지 방법이 있습니다. 여기서는 개발자들이 가장 많이 사용하는 **Homebrew** 방식과 가장 직관적인 **Postgres.app** 방식을 소개합니다.

### 방법 A: Homebrew 사용 (추천)
1. 터미널을 열고 Homebrew를 이용해 설치합니다.
   ```bash
   brew install postgresql
   ```
2. **서비스 실행**:
   백그라운드에서 PostgreSQL을 실행하고, 맥을 켤 때마다 자동 실행되도록 설정합니다.
   ```bash
   brew services start postgresql
   ```
3. **접속 테스트 및 비밀번호 설정 (선택사항)**:
   맥 사용자 이름으로 기본 권한이 주어집니다. 외부 툴(DBeaver) 접속을 위해 `postgres` 계정의 비밀번호를 설정해두는 것이 좋습니다.
   ```bash
   # 1. 터미널에서 psql 쉘 접속
   psql postgres
   ```
   psql 쉘에 접속한 상태에서 아래 명령어로 비밀번호를 설정합니다.
   ```sql
   -- 2. 비밀번호 설정 (원하는 비밀번호 입력 후 엔터)
   \password postgres
   ```
   > 💡 비밀번호 설정이 끝났으면 `\q` 를 입력하고 엔터를 눌러 psql 쉘을 종료합니다.

### 방법 B: Postgres.app 사용 (가장 쉬운 방법)
터미널 환경이 익숙하지 않다면 이 방법을 추천합니다.
1. [Postgres.app 공식 사이트](https://postgresapp.com/)에 접속하여 최신 버전(Installer 포함)을 다운로드합니다.
2. 다운로드한 `.dmg` 파일을 열고, 코끼리 아이콘을 `Applications(응용 프로그램)` 폴더로 드래그 앤 드롭합니다.
3. 런치패드에서 Postgres를 찾아 실행합니다.
4. "Initialize" 버튼을 누르면 서버가 시작됩니다.
5. 앱 화면에 나타나는 데이터베이스 이름(일반적으로 Mac 사용자 이름)을 더블 클릭하면 바로 터미널을 통해 데이터베이스에 접속됩니다.
