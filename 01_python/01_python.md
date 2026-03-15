# Python 시작하기: 초보자를 위한 완벽 가이드

이 문서는 Python을 처음 접하는 분들을 위해 만들어졌습니다. 프로그래밍의 기초부터 단위 테스트 작성까지, Python 개발에 필요한 핵심 개념들을 단계별로 안내합니다.

---

## 1. Python이란 무엇인가?

Python은 **가독성**이 뛰어나고 **문법이 간결**하여 초보자가 배우기 가장 좋은 프로그래밍 언어 중 하나입니다. 웹 개발, 데이터 과학, 인공지능, 자동화 등 매우 다양한 분야에서 활용됩니다.

- **장점**:
  - 배우기 쉽고 생산성이 높습니다.
  - 강력한 표준 라이브러리와 방대한 서드파티 패키지를 갖추고 있습니다.
  - 다양한 플랫폼(Windows, macOS, Linux)에서 동일하게 동작합니다.

---

## 2. 기본 문법

Python의 가장 기초적인 문법부터 알아봅시다.

### 변수와 자료형

변수는 데이터를 저장하는 공간입니다. Python은 변수에 값을 할당할 때 자료형을 자동으로 인식합니다.

```python
# 변수 할당
name = "Alice"      # str (문자열)
age = 30            # int (정수)
height = 172.5      # float (실수)
is_student = True   # bool (참/거짓)

print(f"{name}의 나이는 {age}세, 키는 {height}cm입니다.")
```

### 자료 구조

여러 데이터를 효율적으로 관리하기 위한 자료 구조입니다.

- **리스트 (List)**: 순서가 있고, 수정 가능한 데이터 모음. `[]`로 만듭니다.
  ```python
  fruits = ["사과", "바나나", "체리"]
  fruits.append("딸기")  # 추가
  print(fruits[1])     # "바나나" (인덱싱)
  ```

- **튜플 (Tuple)**: 순서가 있지만, **수정 불가능한** 데이터 모음. `()`로 만듭니다.
  ```python
  point = (10, 20)
  print(point[0])      # 10
  # point[0] = 15  # TypeError 발생!
  ```

- **딕셔너리 (Dictionary)**: `key`-`value` 쌍으로 이루어진 데이터 모음. `{}`로 만듭니다.
  ```python
  person = {"name": "Bob", "age": 25}
  print(person["name"])  # "Bob"
  person["email"] = "bob@test.com" # 추가/수정
  ```

- **집합 (Set)**: 중복을 허용하지 않는 순서 없는 데이터 모음. `{}`로 만듭니다.
  ```python
  numbers = {1, 2, 3, 2, 1}
  print(numbers)  # {1, 2, 3}
  ```

---

## 3. 제어 흐름

코드의 실행 순서를 제어하는 구문입니다.

### 조건문 (if)

조건이 참일 때만 특정 코드 블록을 실행합니다.

```python
score = 85
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
else:
    print("C 등급")
```

### 반복문 (for, while)

- **for**: 시퀀스(리스트, 튜플 등)의 각 요소를 순회합니다.
  ```python
  for fruit in ["사과", "바나나", "체리"]:
      print(fruit)
  ```

- **while**: 조건이 참인 동안 코드 블록을 반복합니다.
  ```python
  count = 0
  while count < 3:
      print(f"카운트: {count}")
      count += 1
  ```

---

## 4. 함수 (Functions)

재사용 가능한 코드 블록을 만드는 방법입니다. `def` 키워드로 정의합니다.

```python
def add(a, b):
    """두 숫자를 더한 결과를 반환합니다."""
    return a + b

result = add(5, 3)
print(result)  # 8
```

---

## 5. 객체 지향 프로그래밍 (OOP)

객체 지향 프로그래밍(OOP)의 개념과 실제 적용 방법에 대해 더 깊이 알고 싶다면 아래 문서를 참고하세요. 상속, 캡슐화, 다형성 등 핵심 개념과 실습 예제가 포함되어 있습니다.

> **[👉 05_python_oop_instructions.md 보기](./05_python_oop_instructions.md)**

---

## 6. 좋은 코드 설계를 위한 SOLID 원칙

유지보수와 확장이 용이한 코드를 작성하기 위한 SOLID 원칙에 대해 알아보세요. 아래 문서에서 각 원칙에 대한 자세한 설명과 Python 예제를 확인할 수 있습니다.

> **[👉 05_python_solid_instructions.md 보기](./05_python_solid_instructions.md)**

---

## 7. 단위 테스트 (Unit Testing) with Pytest

작성한 코드가 의도대로 정확히 동작하는지 검증하는 것은 매우 중요합니다. `pytest`는 Python에서 가장 널리 사용되는 테스트 프레임워크입니다.

### Pytest 기본

- `pip install pytest`로 설치합니다.
- 테스트 파일은 `test_*.py` 또는 `*_test.py` 형식으로 만듭니다.
- 테스트 함수는 `test_`로 시작해야 합니다.
- `assert` 문을 사용하여 결과가 예상과 같은지 검증합니다.

### 예제: 간단한 계산기 테스트

1.  **`calculator.py` 파일 작성**

    ```python
    # calculator.py
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b
    ```

2.  **`test_calculator.py` 파일 작성**

    ```python
    # test_calculator.py
    from . import calculator  # 같은 디렉토리의 calculator.py를 가져옴

    def test_add():
        """덧셈 함수를 테스트합니다."""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    def test_subtract():
        """뺄셈 함수를 테스트합니다."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(1, 5) == -4
    ```

3.  **테스트 실행**

    터미널에서 `pytest` 명령어를 실행하면 `test_`로 시작하는 파일과 함수를 자동으로 찾아 실행하고 결과를 보여줍니다.

    ```bash
    $ pytest
    ========================= test session starts ==========================
    ...
    collected 2 items

    test_calculator.py ..                                            [100%]

    ========================== 2 passed in ...s ============================
    ```

### 심화 학습

`tests_python/` 디렉토리에는 OOP와 SOLID 원칙에 대한 `pytest` 연습문제가 준비되어 있습니다. 이 테스트들을 통과시키면서 Python 실력을 한 단계 업그레이드해 보세요.

- **`tests_python/test_oop.py`**: OOP 개념을 코드로 구현하는 연습을 합니다.
- **`tests_python/test_solid.py`**: SOLID 원칙을 적용하여 코드를 리팩토링하는 연습을 합니다.

> **[👉 tests_python/ 디렉토리로 이동하여 실습하기](./tests_python/)**
