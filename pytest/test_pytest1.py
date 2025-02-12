import pytest

# pytest -v : 테스트 상세 결과 출력
# pytest -s : print() 같은 출력도 보이게 실행
# pytest -k "test_name" : 특정 이름이 포함된 테스트만 실행
# pytest --maxfail=2 : 2개 실패하면 즉시 종료
# pytest --html=report.html : HTML 테스트 리포트 생성

# fixture : 반복되는 테스트 환경을 자동으로 설정할 때 사용

# -------------------------------------------------------------------------

# pytest 실습 문제
"""
add(x, y) 함수를 만든다
x + y의 결과가 기대값과 같은지 pytest로 검증한다.
"""

# 조건
"""
add(2, 3) --> 5 
add(-1, 1) --> 0
"""

@pytest.mark.parametrize("x, y, expected", [(2,3,5), (-1,1,0)])
def test_add(x, y, expected):
    assert x + y == expected

# -------------------------------------------------------------------------

# pytest 실습 문제
"""
fruits = ["apple", "banana", "cherry"] 리스트에서 특정 값이 존재하는지 확인
"banana"가 리스트 안에 포함되어 있는지 assert로 검증
"""

@pytest.fixture
def sample_fruits():
    return ["apple", "banana", "cherry"]

def test_list(sample_fruits):
    assert sample_fruits[1] == "banana"
    assert "banana" in sample_fruits

# -------------------------------------------------------------------------

# pytest 실습 문제
"""
문자열 "pytest is great"가 "pytest"로 시작하는지 확인하는 테스트를 작성
assert "pytest is great".startswith("pytest") 사용
"""

@pytest.fixture
def sample_string():
    return "pytest is great"

def test_string(sample_string):
    assert sample_string.startswith("pytest")

# -------------------------------------------------------------------------

# pytest 실습 문제
"""
multiply(x, y) 함수를 만든다.
@pytest.mark.parametrize를 사용하여 여러 개의 테스트 데이터를 한 번에 실행한다.
"""

@pytest.mark.parametrize("x, y, expected", [(4,2,8), (2,6,12)])
def test_multiply(x, y, expected):
    assert x * y == expected

# -------------------------------------------------------------------------

# pytest 실습 문제
"""
@pytest.fixture를 사용하여 **테스트 데이터(딕셔너리)**를 생성
딕셔너리에 "username": "test_user", "password": "secure123"를 넣고
"username"이 "test_user"인지 확인하는 테스트 작성
"""

@pytest.fixture
def sample_data():
    return {"username": "test_user", "password":"secure123"}

def test_data(sample_data):
    assert sample_data["username"] == "test_user"
    assert sample_data["password"] == "secure123"

# -------------------------------------------------------------------------