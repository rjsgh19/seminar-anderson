# DBeaver 설치 및 PostgreSQL 연결 가이드

이 문서에서는 Windows, macOS, Ubuntu 등 모든 운영체제에서 무료로 사용할 수 있는 가장 훌륭한 범용 데이터베이스 클라이언트 툴인 **DBeaver (Community Edition)**를 설치하고, PostgreSQL 데이터베이스에 연결하는 방법을 단계별로 설명합니다.

---

## 🚀 1. DBeaver 설치하기 (운영체제별)

### 💻 Windows
1. **[DBeaver Community 다운로드 페이지](https://dbeaver.io/download/)**로 이동합니다.
2. `Windows (installer)` 버튼을 클릭하여 `.exe` 파일을 다운로드합니다.
3. 다운로드한 파일을 실행하고 "다음(Next)" 버튼만 계속 클릭하여 설치를 완료합니다. (기본 설정 사용)

### 🍏 macOS
1. **[DBeaver Community 다운로드 페이지](https://dbeaver.io/download/)**로 이동합니다.
2. `Mac OS X (dmg)` (사양에 따라 Intel 또는 Apple Silicon) 버전을 다운로드합니다.
   - *팁: 모를 경우 터미널에서 Homebrew를 사용하면 더 편합니다.*
   ```bash
   brew install --cask dbeaver-community
   ```
3. `.dmg` 파일인 경우 실행 후 애플리케이션 폴더로 아이콘을 드래그합니다.

### 🐧 Ubuntu (Linux)
터미널을 열고 아래 명령어를 순서대로 복사하여 붙여넣으면 설치가 완료됩니다.
```bash
sudo snap install dbeaver-ce
```
*(또는 공식 홈페이지에서 `.deb` 패키지를 다운로드 받아 더블클릭하여 설치할 수도 있습니다.)*

---

## 🔌 2. PostgreSQL 데이터베이스 연결하기

DBeaver 설치가 끝났다면 이제 내 컴퓨터 안에 설치된(또는 외부에 있는) PostgreSQL 데이터베이스와 연결할 차례입니다.

### 1단계: 새 연결 만들기
1. DBeaver를 실행합니다.
2. 왼쪽 상단 메뉴나 화면 가운데에 있는 **플러그 아이콘("새 연결" 또는 "New Database Connection")**을 클릭합니다.
   *(단축키: `Ctrl` + `Shift` + `N` 또는 `Cmd` + `Shift` + `N`)*
3. 나타나는 데이터베이스 목록 창에서 **코끼리 모양 아이콘인 `PostgreSQL`**을 선택하고 "다음(Next)"을 누릅니다.

### 2단계: 연결 정보 (Connection Settings) 입력하기
**"Main" 탭** 화면에 아래와 같이 빈칸을 채워줍니다. 내 컴퓨터에 설치된 기본 DB에 연결하는 기준입니다.

* **Host**: `localhost` (내 컴퓨터를 의미합니다.)
* **Port**: `5432` (기본 포트 번호입니다. 건드리지 마세요.)
* **Database**: `postgres` (기본으로 생성되는 데이터베이스 이름입니다.)
* **Username**: `postgres` (관리자 계정 이름입니다.)
* **Password**: *PostgreSQL을 처음 설치할 때 설정했던 가장 중요한 <u>그 비밀번호</u>를 입력합니다.*

> 💡 **Tip:** "Save password locally(로컬에 비밀번호 저장)" 체크박스를 켜두시면 다음부터 더블클릭만으로 접속할 수 있습니다.

### 3단계: 드라이버 다운로드 (최초 1회만)
만약 DBeaver를 방금 막 처음 설치했다면, PostgreSQL과 대화하기 위한 언어 파일(JDBC Driver)을 받아야 합니다.
1. "Test Connection (연결 테스트)" 버튼이나 "완료(Finish)"를 누릅니다.
2. **"Driver download"** 라는 팝업 창이 뜰 것입니다. 여기서 반드시 **"Download (다운로드)"** 버튼을 클릭해 줍니다. (인터넷이 연결되어 있어야 합니다.)

### 4단계: 연결 확인 완료!
1. 왼쪽 **"데이터베이스 탐색기(Database Navigator)"** 창 패널에 코끼리 모양 아이콘으로 `localhost`가 추가된 것을 확인할 수 있습니다.
2. 방금 추가한 항목을 마우스 우클릭 -> **"SQL 편집기(SQL Editor) 열기"**를 클릭하거나 단축키(F3)를 누릅니다.
3. 오른쪽에 열린 하얀 메모장 같은 화면에 쿼리를 입력할 수 있습니다. 아래 쿼리를 복사하여 붙여넣고 `Ctrl` + `Enter` (맥은 `Cmd` + `Enter`)를 눌러 실행해 봅시다.

```sql
SELECT version();
```
화면 아래 결과창(Result 탭)에 현재 설치된 PostgreSQL의 버전 정보가 예쁘게 표 형태로 출력된다면 **설치 및 접속이 완벽하게 성공**한 것입니다! 🎉

이제 이 SQL 편집기 창에서 마음껏 문법 연습을 시작하시면 됩니다.
