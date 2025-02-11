# 기능 테스트 (Functionality Testing)
- 게임의 각 기능이 기획대로 정상적으로 작동하는지 검증하는 테스트
- 게임 내 버튼, UI, 시스템, 캐릭터, 아이템, 스킬, 퀘스트 등이 올바르게 동작하는지 확인하는 것이 핵심
- 사용자가 실제로 경험하는 기능을 테스트하여 플레이 중 발생할 수 있는 버그를 찾는 것이 목적


# 기능 테스트에서 검증하는 항목 (예시)
1. 로그인 / 회원가입 테스트
- 아이디와 비밀번호를 입력했을 때 정상 로그인되는지 확인
- 틀린 비밀번호 입력 시 적절한 오류 메시지가 나오는지 확인
- 회원가입 시 닉네임 중복 체크가 정상적으로 동작하는지

- 예시
- TC-001
    - 테스트 케이스 : 올바른 아이디 / 비밀번호 입력 후 로그인
    - 예상 결과 : 로그인 성공
    - 실제 결과 : (테스트 후 기록)
    - 상태 : Pass/Fail 기록
- TC-002
    - 테스트 케이스 : 잘못된 비밀번호 입력 후 로그인
    - 예상 결과 : "비밀번호 오류" 메시지 표시
    - 실제 결과 : (테스트 후 기록)

2. 캐릭터 이동 & 조작 테스트
- 이동 키 입력 시 캐릭터가 정상적으로 움직이는지 확인
- 특정 지형에 부딪혔을 때 정상적으로 멈추는지
- 카메라 회전이 정상적으로 동작하는지

- 예시
- TC-003
    - 테스트 케이스 : "시작하기" 버튼 클릭
    - 예상 결과 : 게임 시작 화면으로 이동
    - 실제 결과 : -
    - 상태 : -
- TC-004
    - 테스트 케이스 : "설정" 버튼 클릭
    - 예상 결과 : 설정 창이 열림
    - 실제 결과 : -
    - 상태 : -
