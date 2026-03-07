# DVD Rental 샘플 데이터 설치 가이드 (DBeaver 기준)

PostgreSQL 학습을 위한 전 세계 표준 예제인 **DVD Rental 데이터베이스**를 다운로드하고 내 로컬 DB에 넣는 방법입니다.

---

## 1. 샘플 데이터 다운로드

1. [PostgreSQL Tutorial 다운로드 페이지](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)에 접속합니다.
2. 본문 중간의 **`Download DVD Rental Sample Database`** 링크를 클릭하여 `.zip` 파일을 다운로드합니다.
3. 압축을 풀면 **`dvdrental.tar`** 파일이 나옵니다. 이 경로를 잘 기억해 둡니다.

---

## 2. DBeaver에 데이터베이스(빈 그릇) 만들기


기존 `postgres` DB에 데이터가 섞이지 않도록 전용 빈 데이터베이스를 하나 새로 만듭니다.
> 🚨 **주의: "Cannot create a database... Enable 'Show all databases'" 에러가 날 경우**
> DBeaver는 기본적으로 접속한 단일 DB만 보여주도록 설정되어 있어 새 DB 생성이 막혀있습니다.
> 1. 내 연결(`localhost`)을 마우스 우클릭 -> **Edit Connection (연결 편집)** 클릭
> 2. **PostgreSQL** 탭으로 이동
> 3. **Show all databases (모든 데이터베이스 표시)** 체크박스를 체크하고 확인(OK) 클릭
> 4. 연결을 한 번 끊었다가 다시 연결(Disconnect -> Connect)하면 정상적으로 생성 가능합니다.

1. DBeaver를 열고, 왼쪽 탐색기에서 내 연결(`localhost`)을 펼칩니다.
2. `Databases` 폴더를 마우스 우클릭 -> **Create New Database (새 데이터베이스 생성)** 를 클릭합니다.
3. Database Name 칸에 **`dvdrental`** 이라고 입력하고 "확인(OK)"을 누릅니다.
4. 왼쪽 목록에 방금 만든 `dvdrental` 아이콘이 생겼는지 확인합니다.

---

## 3. 데이터 복원하기 (Restore) 

방금 만든 빈 데이터베이스(`dvdrental`)에 `.tar` 파일의 데이터를 들이붓는 과정입니다.

1. 왼쪽 목록에 생긴 **`dvdrental` 데이터베이스를 마우스 우클릭** 합니다.
2. 메뉴에서 **Tools (도구) -> Restore (복원)** 를 클릭합니다.
3. **Format** 항목을 `Custom or tar` 로 선택합니다. (버전에 따라 이미 선택되어 있을 수 있습니다.)
4. 화면 중간 **Input** 섹션 아래의 **`Backup file:`** 빈칸 가장 오른쪽에 있는 **작은 폴더 아이콘(📁)** 을 클릭하여, 아까 압축을 풀어둔 **`dvdrental.tar`** 파일을 찾아 선택합니다.
5. 우측 하단의 **"Start (시작)"** 버튼을 누릅니다.
   *(※ 만약 로컬 클라이언트 알림 창이 뜨면 확인/승인을 눌러줍니다.)*

---

## 4. 확인하기

복원이 끝났다면 데이터가 잘 들어왔는지 확인합니다.

1. `dvdrental` 데이터베이스를 펼쳐서 `Schemas` -> `public` -> `Tables` 경로로 들어갑니다.
2. `actor`, `film`, `customer` 등 **총 15개의 테이블**이 생성되어 있는지 확인합니다.
3. 새 SQL 편집기 창에서 아래 쿼리를 실행해 데이터가 출력되는지 봅니다.
   ```sql
   SELECT * FROM actor LIMIT 10;
   ```
