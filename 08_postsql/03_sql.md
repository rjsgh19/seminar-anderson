# PostgreSQL 입문자를 위한 SQL 101 가이드

이 문서에서는 PostgreSQL을 기반으로 한 SQL의 가장 핵심적인 기초 지식부터 실무에서 자주 쓰이는 명령어까지 모두 다룹니다.

## 1. SQL 명령어의 실행 순서 (매우 중요!)

**실제 데이터베이스 처리(실행) 순서 (Execution Order):**
1. **`FROM`**: 어떤 테이블에서 데이터를 가져올지 머릿속에 표를 펼칩니다. (JOIN이 있다면 여기서 테이블들을 합칩니다.)
2. **`WHERE`**: 펼친 테이블에서 조건에 맞지 않는 불필요한 행(Row)들을 걸러냅니다. (이 시점에선 아직 그룹화하기 전입니다.)
3. **`GROUP BY`**: 살아남은 행들을 특정 컬럼 기준으로 그룹(Group) 지어 묶어줍니다.
4. **`HAVING`**: 그룹화된 결과 중에서 조건에 맞는 그룹만 다시 걸러냅니다. (`WHERE`는 개별 행을, `HAVING`은 그룹을 필터링합니다.)
5. **`SELECT`**: 최종적으로 화면에 보여줄 컬럼만 선택하고, 계산식이나 함수를 적용합니다.
6. **`ORDER BY`**: 뽑아낸 결과들을 지정한 기준에 따라 정렬합니다.
7. **`LIMIT` / `OFFSET`**: 정렬된 결과의 맨 위에서부터 몇 개의 데이터만 가져올지 잘라냅니다.

> 💡 **Tip:** `SELECT`에서 `AS`를 사용해 만든 컬럼 별칭(Alias)을 `WHERE`에서는 사용할 수 없으나, `ORDER BY`에서는 사용할 수 있는 이유도 바로 이 **실행 순서** 때문입니다. (`WHERE`가 `SELECT`보다 먼저 실행되므로 별칭을 아직 모름)

---

## 2. 실습용 예제 데이터 (Employees 테이블)

모든 예제는 다음 `employees` (직원) 데이터를 기준으로 설명합니다.

| emp_id | name | department | salary | join_date |
|---|---|---|---|---|
| 1 | 김철수 | 영업부 | 3000 | 2021-01-15 |
| 2 | 이영희 | 마케팅 | 3500 | 2020-05-20 |
| 3 | 박지성 | 개발부 | 5000 | 2018-03-10 |
| 4 | 최승범 | 영업부 | 3200 | 2022-07-01 |
| 5 | 정수연 | 개발부 | 4500 | 2019-11-11 |
| 6 | 강호동 | 개발부 | 2800 | 2023-01-05 |

---

## 3. SQL 기초 명령어 101

### 3.1 `SELECT` & `FROM`: 데이터 조회하기
테이블에서 데이터를 가져오는 가장 기본적인 명령어입니다.
```sql
-- employees 테이블의 모든 컬럼(*) 및 모든 행 조회
SELECT * 
FROM employees;

-- 특정 컬럼(name, salary)만 조회
SELECT name, salary 
FROM employees;
```

### 3.2 `WHERE`: 조건으로 데이터 필터링하기
특정 조건을 만족하는 데이터만 걸러냅니다.
```sql
-- 급여(salary)가 3500 이상인 직원만 조회
SELECT name, department, salary
FROM employees
WHERE salary >= 3500;

-- 영업부 소속이면서 동시에 급여가 3100 이상인 직원 조회 (AND 연산자)
SELECT name, salary
FROM employees
WHERE department = '영업부' AND salary >= 3100;
```

### 3.3 `ORDER BY`: 데이터 정렬하기
결과를 오름차순(ASC, 기본값) 또는 내림차순(DESC)으로 정렬합니다.
```sql
-- 급여가 높은 순서대로(내림차순) 정렬
SELECT name, salary
FROM employees
ORDER BY salary DESC;
```

### 3.4 `LIMIT` & `OFFSET`: 출력 개수 제한하기 (PostgreSQL 지원)
조회되는 데이터의 개수를 제한합니다. 보통 페이지네이션(Pagination)이나 상위 N개를 뽑을 때 사용합니다.
```sql
-- 급여가 가장 높은 상위 3명만 조회
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- 급여가 가장 높은 1등은 건너뛰고(OFFSET 1), 2등부터 3명 조회
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3 OFFSET 1;
```

---

## 4. 데이터 집계와 그룹핑 (Aggregation & Grouping)

### 4.1 기본 집계 함수
여러 행의 데이터를 하나로 합쳐서 계산해줍니다.
- `COUNT()`: 데이터 개수
- `SUM()`: 합계
- `AVG()`: 평균
- `MAX()` / `MIN()`: 최댓값 / 최솟값

```sql
-- 전체 직원의 수와 평균, 최고 급여 계산
SELECT 
    COUNT(emp_id) AS total_employees, 
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary
FROM employees;
```

### 4.2 `GROUP BY`: 그룹별로 묶어서 집계하기
부서별 평균 급여, 연도별 가입자 수 등 특정 기준에 따라 데이터를 묶어서 요약할 때 사용합니다.
```sql
-- 부서별 직원 수와 평균 급여 조회
SELECT 
    department, 
    COUNT(emp_id) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

**결과 예시:**
| department | emp_count | avg_salary |
|---|---|---|
| 영업부 | 2 | 3100 |
| 마케팅 | 1 | 3500 |
| 개발부 | 3 | 4100 |

### 4.3 `HAVING`: 그룹화된 결과에 조건 걸기
`WHERE`는 집계 전 개별 행에 조건을 걸고, `HAVING`은 `GROUP BY`로 요약된 **그룹 단위의 결과**에 조건을 겁니다.
```sql
-- '부서별 평균 급여'를 구한 뒤, 그 평균 급여가 4000 이상인 부서만 출력
SELECT 
    department, 
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) >= 4000;
```

---

## 5. 고급 데이터 분석: Window Functions (파티션 및 순위)

데이터를 `GROUP BY` 하면 원래의 상세한 행(Row)들이 하나로 뭉쳐져 사라집니다. 하지만 **윈도우 함수(Window Function)를 사용하면 원래의 개별 행 데이터를 그대로 유지하면서도, 그룹별 통계를 계산하거나 순위를 매길 수 있습니다.** 이를 위해 `PARTITION BY` 구문을 사용합니다.

### 5.1 `PARTITION BY` + `RANK()`: 그룹 내 순위 매기기
부서 안에서 누가 급여를 제일 많이 받는지 순위를 매겨봅시다.
```sql
SELECT 
    name, 
    department, 
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank_in_dept
FROM employees;
```
- `PARTITION BY department`: 이름처럼 부서 단위로 쪼개어 "파티션(창)"을 나눕니다.
- `ORDER BY salary DESC`: 그 나뉘어진 부서 안에서 급여 순으로 내림차순 정렬하여 순위(RANK)를 매깁니다.

**결과 예시:** 부서별로 1등부터 순위가 따로 매겨진 것을 볼 수 있습니다.
| name | department | salary | rank_in_dept |
|---|---|---|---|
| 최승범 | 영업부 | 3200 | 1 |
| 김철수 | 영업부 | 3000 | 2 |
| 이영희 | 마케팅 | 3500 | 1 |
| 박지성 | 개발부 | 5000 | 1 |
| 정수연 | 개발부 | 4500 | 2 |
| 강호동 | 개발부 | 2800 | 3 |

### 5.2 `PARTITION BY` + 집계 함수: 행을 유지하며 합계/평균 구하기
직원 개개인의 월급 데이터를 보면서, 동시에 그 직원이 속한 부서의 평균 급여도 한 화면에 같이 출력하고 싶을 때 사용합니다.
```sql
SELECT 
    name, 
    department, 
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees;
```
**결과 예시:** 개별 직원의 내역이 사라지지 않으면서, 우측에 부서별 평균(`dept_avg_salary`) 값이 추가로 붙습니니다.
| name | department | salary | dept_avg_salary |
|---|---|---|---|
| 김철수 | 영업부 | 3000 | 3100 |
| 최승범 | 영업부 | 3200 | 3100 |
| 이영희 | 마케팅 | 3500 | 3500 |
| 박지성 | 개발부 | 5000 | 4100 |
...

## 6. 요약 치트시트 (Cheat Sheet)
- `SELECT`: 가져올 컬럼(열) 선택 (5번째 실행)
- `FROM`: 기준으로 삼을 테이블 지목 (1번째 실행)
- `WHERE`: 조건에 맞는 데이터 골라내기 (그룹으로 묶기 전 필터) (2번째 실행)
- `GROUP BY`: 특정 카테고리 기준으로 묶어서 통계/요약 데이터 만들기 (3번째 실행)
- `HAVING`: `GROUP BY`로 묶인 결과들 중에서 조건에 맞는 그룹만 골라내기 (4번째 실행)
- `ORDER BY`: 결과물 줄 세우기 (6번째 실행)
- `LIMIT`: 깔끔하게 원하는 개수만큼만 데이터 잘라내기 (7번째 실행)
- `OVER (PARTITION BY ...)`: `GROUP BY`처럼 데이터를 뭉개지 않고, 원래 행을 유지한 채 그룹별 통계나 순위를 개별 행 옆에 붙이고 싶을 때 사용하는 마법의 키워드!
