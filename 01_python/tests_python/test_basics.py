import pytest

# =============================================================================
# 실습 1: 함수 구현하기 (기본)
#
# 목표: Python의 기본 함수 작성법을 익힙니다.
#
# 아래에 주어진 각 함수의 내부를 채워 모든 테스트를 통과시키세요.
# 'pass' 키워드는 지우고 자신의 코드를 작성하세요.
# =============================================================================

def get_grade(score: int) -> str:
    """
    점수(score)를 받아 학점을 반환하는 함수를 작성하세요.

    - 90점 이상: "A"
    - 80점 이상 90점 미만: "B"
    - 70점 이상 80점 미만: "C"
    - 70점 미만: "F"

    조건문(if, elif, else)을 사용해야 합니다.
    """
    # TODO: 여기에 코드를 작성하세요.
    pass


def sum_of_evens(numbers: list[int]) -> int:
    """
    정수 리스트(numbers)를 받아 짝수의 합만 계산하여 반환하는 함수를 작성하세요.

    반복문(for)과 조건문(if)을 사용해야 합니다.
    `num % 2 == 0` 코드를 사용하면 짝수를 판별할 수 있습니다.
    """
    # TODO: 여기에 코드를 작성하세요.
    pass


def find_longest_word(words: list[str]) -> str:
    """
    문자열 리스트(words)에서 가장 긴 단어를 찾아 반환하는 함수를 작성하세요.

    만약 가장 긴 단어가 여러 개라면, 리스트에 먼저 나타나는 단어를 반환하세요.
    리스트가 비어있다면 빈 문자열 ""을 반환하세요.
    `len(word)`로 단어의 길이를 알 수 있습니다.
    """
    # TODO: 여기에 코드를 작성하세요.
    pass


def count_word_frequency(text: str) -> dict[str, int]:
    """
    문자열(text)을 받아 각 단어의 빈도를 계산하여 딕셔너리로 반환하는 함수를 작성하세요.

    - 모든 단어는 소문자로 변환하여 계산합니다.
    - 구두점(마침표, 쉼표 등)은 단어의 일부가 아닙니다.
      (힌트: `word.strip('.,?!')`를 사용해 보세요.)
    - `text.split()`를 사용하면 공백을 기준으로 단어를 나눌 수 있습니다.
    """
    # TODO: 여기에 코드를 작성하세요.
    pass


# =============================================================================
# 테스트 코드 (여기를 수정하지 마세요)
# =============================================================================

@pytest.mark.parametrize("score, expected_grade", [
    (95, "A"),
    (90, "A"),
    (85, "B"),
    (80, "B"),
    (71, "C"),
    (70, "C"),
    (69, "F"),
    (0, "F"),
])
def test_get_grade(score, expected_grade):
    assert get_grade(score) == expected_grade


def test_sum_of_evens_basic():
    assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12


def test_sum_of_evens_with_negatives():
    assert sum_of_evens([-2, -1, 0, 1, 2]) == 0


def test_sum_of_evens_all_odd():
    assert sum_of_evens([1, 3, 5, 7]) == 0


def test_sum_of_evens_empty_list():
    assert sum_of_evens([]) == 0


def test_find_longest_word_basic():
    assert find_longest_word(["apple", "banana", "cherry"]) == "banana"


def test_find_longest_word_tie():
    assert find_longest_word(["cat", "dog", "eel"]) == "cat"


def test_find_longest_word_empty_list():
    assert find_longest_word([]) == ""


def test_find_longest_word_with_numbers():
    assert find_longest_word(["1", "22", "333"]) == "333"


def test_count_word_frequency_basic():
    text = "hello world hello"
    expected = {"hello": 2, "world": 1}
    assert count_word_frequency(text) == expected


def test_count_word_frequency_case_insensitive():
    text = "Apple apple banana"
    expected = {"apple": 2, "banana": 1}
    assert count_word_frequency(text) == expected


def test_count_word_frequency_with_punctuation():
    text = "Hello, world! Hello."
    expected = {"hello": 2, "world": 1}
    assert count_word_frequency(text) == expected


def test_count_word_frequency_empty_string():
    assert count_word_frequency("") == {}
