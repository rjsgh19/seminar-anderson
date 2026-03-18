# GitHub 기초 튜토리얼 (실습형)

이 튜토리얼은 단순히 눈으로만 읽는 것이 아니라, **직접 터미널에 명령어를 하나씩 골라서 입력하며** 흐름을 이해하는 것을 목적으로 디자인 되었습니다. 
아래 순서대로 직접 타이핑하며 따라와 주세요!

*(명령어 앞의 `$` 또는 `(main)$` 등은 프롬프트를 의미합니다. 직접 타이핑할 때는 `$` 뒷부분 명령어만 입력하세요. 괄호 안의 글자는 **현재 내 위치(브랜치)**를 나타냅니다.)*

---

## 0. 시작하기 전에 (Git 설정 및 인증)

Git 설치가 완료되었다면, 누가 커밋(저장)을 남기는지 알아야 합니다. 터미널(또는 명령 프롬프트)을 열고 아래 명령어를 입력해 설정해 보세요.

```bash
# 본인의 이름과 이메일로 변경해서 입력하세요.
$ git config --global user.name "내 이름"
$ git config --global user.email "내 이메일@example.com"

# 설정이 잘 적용되었는지 확인
$ git config --list
```

---

## 1. 나의 첫 로컬 저장소 만들기 (`git init`)

작업할 새로운 폴더를 만들고, 그 폴더를 Git이 파일들을 관리(추적)하도록 만들어 봅시다.

```bash
# 1. 터미널에서 임의의 실습용 폴더를 만들고 그 안으로 이동합니다.
$ mkdir my-first-repo
$ cd my-first-repo

# 2. 이 폴더를 Git 저장소로 초기화합니다.
$ git init

# 3. 현재 상태를 확인합니다. (init 이후부터는 현재 브랜치가 main으로 표시되기 시작합니다 - 환경에 따라 master일 수 있음)
(main)$ git status
```
*💡 `git init`을 누르면 숨김 폴더인 `.git`이 생성되며, 이때부터 Git이 파일의 변경 사항을 추적할 준비를 마칩니다. `git status`는 현재 깃의 상태를 알려주는 아주아주 중요한 명령어이므로 작업 중 수시로 입력해보는 습관을 들이세요!*

---

## 2. 파일 만들고 저장하기 (`git add` & `git commit`)

### 2-1. 파일 생성 및 상태 확인
텍스트 파일을 하나 만들어 보겠습니다.

```bash
# 터미널에서 바로 hello.txt 파일 생성 (리눅스/맥 환경)
(main)$ echo "Hello, Git!" > hello.txt

# 상태 확인
(main)$ git status
```
*💡 빨간색 글씨로 `hello.txt`가 보일 것입니다. 이것은 아직 Git이 추적하지 않는 '새로운 파일(Untracked files)'이라는 뜻입니다.*

### 2-2. 장바구니에 담기 (`git add`)
파일의 변경사항을 '저장(Commit)'하기 전, 어떤 파일들을 실제로 저장할지 '장바구니(Staging Area)'에 담는 과정이 필요합니다.

```bash
# hello.txt를 장바구니에 담기
(main)$ git add hello.txt

# 만약 한 번에 모든 변경사항을 담고 싶다면 아래 점(.)을 씁니다.
# (main)$ git add .

# 상태 다시 확인
(main)$ git status
```
*💡 이제 `hello.txt`가 초록색으로 보입니다. "장바구니에 잘 담겼다(Changes to be committed)"는 뜻입니다.*

### 2-3. 실제 사진 찍기(저장하기) (`git commit`)
장바구니에 담긴 파일들을 묶어서, 메시지와 함께 확정적으로 영구 보존(저장)합니다. 게임의 '세이브'와 같습니다.

```bash
# 메시지와 함께 커밋하기
(main)$ git commit -m "첫 번째 커밋: hello.txt 파일 추가"

# 커밋된 역사(기록) 확인하기
(main)$ git log
```

---

## 3. 원격 저장소 연결하기 (`git remote`)

이제 내 컴퓨터의 (로컬) 저장소를 인터넷(GitHub 서버)에 올려봅시다.

1. [GitHub](https://github.com/) 에 로그인하세요.
2. 우측 상단의 `+` 버튼을 누르고 **New repository** 클릭.
3. Repository name에 `my-first-repo`라고 적고 **Create repository** 클릭.
   *(Initialize this repository with 부분은 아무것도 체크하지 마세요!)*

터미널로 돌아와서 복사한 명령어를 한 줄씩 차례대로 칩니다. (*아래 주소는 본인 것으로 변경해야 합니다*)

```bash
# 원격 저장소(origin) 연결
(main)$ git remote add origin https://github.com/내아이디/my-first-repo.git

# 기본 브랜치 이름을 'main'으로 명시
(main)$ git branch -M main

# 원격(GitHub 서버)으로 기록 밀어내기 (push)
(main)$ git push -u origin main
```
*💡 완료 후 GitHub 새로고침 시 `hello.txt`가 올라가 있습니다.*

---

## 4. 가지치기: 브랜치 (Branch)의 이해

브랜치는 **독립적인 평행 세계**를 만드는 것과 같습니다. 기존의 작업물에 영향을 주지 않고 새로운 기능을 개발하거나 테스트할 수 있습니다.

### 🌳 브랜치 시각화
```text
[ 브랜치 생성 전 (현재 머무는 곳: main) ]
(main)
  A --- B (현재 상태)

[ 브랜치 생성 후 (feature-login 분기 생성) ]
(main)
  A --- B
         \ 
          C --- D (feature-login: 여기서 로그인 기능을 새로 만듦)
```

### 4-1. 브랜치 다루기
```bash
# 1. 새 브랜치 만들기 및 이동을 한번에 하기
(main)$ git switch -c feature-login
# (의미: feature-login 브랜치를 create(-c) 하고 바로 그쪽으로 switch 하라)

# 2. 브랜치 목록 확인 (초록색, 또는 * 표시가 현재 위치)
(feature-login)$ git branch
```

### 4-2. 브랜치 영역에서 작업하기
```bash
(feature-login)$ echo "로그인 기능 추가!" >> login.txt
(feature-login)$ git add login.txt
(feature-login)$ git commit -m "로그인 관련 파일 추가"
```

*💡 현재 위치가 `feature-login`일 때는 `login.txt`가 보이지만, `git switch main`으로 본래 세계로 이동하면 `login.txt`는 감쪽같이 사라져서 보이지 않습니다! (완전히 독립된 공간이기 때문입니다)*

---

## 5. 지저분한 책상 임시 저장하기 (`git stash`)

다른 브랜치로 급하게 이동(`switch`)해야 하는데, 현재 파일들을 한창 수정 중이어서 아직 `commit`하기 전 상태일 때가 있습니다. 이 경우 상태가 꼬여서 이동이 거부됩니다.

이때 **서랍에 작업하던 내용을 임시로 쑤셔 넣고 책상을 깨끗하게 치우는 기능**이 `stash` 입니다.

```bash
# 1. 현재 작업 중이던 내용을 임시 저장소(서랍)에 넣음 (책상이 깨끗해짐!)
(feature-login)$ git stash

# 2. 이제 안전하게 다른 브랜치로 이동 가능
(feature-login)$ git switch main

# 3. 작업이 끝나고 원래 브랜치로 돌아와서 서랍에서 다시 내용물을 꺼내기
(main)$ git switch feature-login
(feature-login)$ git stash pop
```

---

## 6. 브랜치 합치기와 충돌 (Merge / Rebase / Conflict)

사과가 잔뜩 열린 사과 가지(`feature-login`)를 다 만들었다면, 원래의 뼈대(`main`)에 다시 합치는 과정이 필요합니다. 
합치는 방법은 크게 **Merge(병합)**와 **Rebase(재배치)** 두 가지가 있습니다.

### 6-1. Merge (병합)
두 개의 평행 세계를 하나로 **선형적으로 합치는** 일반적인 방법입니다.

```text
[ Merge 후 시각화 ]
(main)          A --- B --------- E (결과물)
                 \               /  (새로운 Merge Commit 이 발생!)
(feature-login)   C --- D -------
```

```bash
# 1. 기준이 되는 브랜치(main)로 이동
(feature-login)$ git switch main

# 2. feature-login 브랜치를 통째로 main으로 병합
(main)$ git merge feature-login
```

### 6-2. Rebase (재배치)
분기했던 가지의 시작점(base)을 다시 잡아, 마치 **처음부터 이어서 1자로 작업한 것처럼** 기록을 깔끔하게 만드는 방법입니다.
*(주의: 내가 이미 인터넷에 올린 브랜치를 Rebase하면 역사(history)가 꼬이므로 주의해야 합니다.)*

```text
[ Rebase 전 ]
(main)          A --- B --- C (본채에 누군가 C를 추가함)
                 \ 
(feature-login)   D --- E

[ Rebase 후 (base를 B에서 C로 변경함) ]
(main)          A --- B --- C 
                             \
(feature-login)               D' --- E' (깔끔한 1자형이 됨!)
```

```bash
# 1. 뽑아서 옮길 브랜치로 이동
(main)$ git switch feature-login

# 2. 시작점을 main의 최신 끝자락으로 옮기기
(feature-login)$ git rebase main
```

### 💥 6-3. Conflict (충돌) 해결하기
내가 수정한 파일의 **정확히 동일한 줄(Line)**을 다른 사람도 동시에 수정했다면 병합(`merge`) 과정에서 충돌이 납니다.

```bash
# git merge 시도 시 충돌이 나면 아래와 같은 에러가 발생합니다.
# CONFLICT (content): Merge conflict in 파일이름
```

충돌이 난 파일을 열어보면 Git이 어찌할 줄 몰라 양쪽 코드를 다 띄워놓았습니다.
```text
<<<<<<< HEAD (현재 내가 있는 브랜치의 내용)
나의 최신 로그인 코드 (아이디, 비밀번호)
=======
동료가 만든 로그인 코드 (이메일, 카카오로그인)
>>>>>>> feature-login (합치려던 브랜치의 내용)
```

**[해결 방법]**
1. 위 내용 중 `<<<<, ====, >>>>` 등 기호들을 모두 지우고, 최종적으로 내가 남기고 싶은 형태를 **직접 텍스트 편집기에서 타이핑하여 정리**합니다.
2. 정리가 끝났다면 다시 `git add`와 `git commit`을 해줍니다.
```bash
# (예를 들어 feature-login 병합 중 main에서 충돌이 났을 때)
(main)$ git add 충돌났던_파일
(main)$ git commit -m "로그인 충돌 해결 완료"
```

---

## 7. 최신 상태 내 컴퓨터로 당겨오기 (`git pull`)

팀원이 내용을 추가해서 GitHub(원격)의 `main`이 바뀌었다면, 내 로컬 컴퓨터의 `main`도 최신화 시켜줘야 합니다.

```bash
# 내 컴퓨터의 main 브랜치로 돌아옵니다.
(feature-login)$ git switch main

# 원격(origin)의 main 최신 내용을 당겨옵니다.
(main)$ git pull origin main
```

*(참고: `git pull`은 내부적으로 원격의 내용을 다운로드하는 `git fetch`와 그것을 내 로컬 브랜치에 합치는 `git merge`를 한 번에 연달아 수행하는 명령어입니다.)*

---

## 8. 실수 되돌리기 기초 (`restore`, `reset`, `amend`)

실수로 원치 않는 파일을 작업했거나, 저장을 잘못 했을 때 복구하는 방법입니다.

```bash
# 1. 어떤 파일을 수정했는데(add 전), 수정을 무시하고 마지막 세이브 지점(과거)으로 파일 되돌리기
(main)$ git restore <파일명>

# 2. 장바구니에 잘못 담은(add) 파일 빼기 (unstage)
(main)$ git restore --staged <파일명>

# 3. 방금 남긴 직전 커밋의 "메시지 글자"만 오타가 났을 때 살짝 다시 덮어쓰기
(main)$ git commit --amend -m "새롭게 수정한 커밋 메시지"

# 4. 아예 이전 커밋 상태들로 시간을 되돌리기 (최후의 수단, 조심해서 쓰세요)
(main)$ git reset --hard HEAD~1   # 1단계 전 커밋으로 모든 변경사항 강제로 날려버리고 되돌아감
```

---

## 9. 핵심 요약 (이것만 기억해도 반은 갑니다)

- `git clone <주소>`: 저장소를 내 컴퓨터로 통째로 다운받기
- `(main)$ git status` : 내 폴더 안의 깃 상태 확인 **(가장 자주 입력!)**
- `(main)$ git switch -c <브랜치명>` : 새 브랜치 만들고 이동
- `(main)$ git add <파일>`: 변경된 파일을 저장 후보에 올리기
- `(main)$ git commit -m "메시지"`: 장바구니에 담긴걸 확정 사진찍어 기록!
- `(main)$ git push`: 로컬 기록을 GitHub 본부로 업로드!
- `(main)$ git pull`: 본부에서 최신 변경사항을 다운로드 + 병합!
- `(main)$ git stash`: 하던 작업 임시 보관함에 넣기! 
- `(main)$ git merge <브랜치명>`: 다른 브랜치를 지금 위치로 끌어와서 합치기!

---
> **미션:** 지금 이 문서에 적힌 모든 명령어들의 뜻을 음미해 보며 따라 해보세요. 막히는 게 생기면 언제든 질문하세요!
