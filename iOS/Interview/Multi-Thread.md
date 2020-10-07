# 멀티 쓰레드로 동작하는 앱을 작성하고 싶을 때 고려할 수 있는 방식들을 설명하시오.

- 공유자원에 접근할 때 충돌이 일어나지 않도록 처리해줘야 한다.

---

- UI와 관련된 작업은 메인 스레드에서 구현
- Mutable한 인스턴스는 스레드에 안전하지 않음(Thread-unsafe), 읽기 전용으로만 사용하다면 문제가 발생하지 않음
- 프로퍼티 원자성
    - 어떤 프로퍼티를 두 개의 스레드가 참조하고 있는 상황에서 해당 프로퍼티 접근자 메서드가 atomic하지 않는다면 값에 대한 싱크가 맞지 않아 문제가 발생할 수 있음
    - Mutable한 인스턴스가 변경 중에 동시 접근할 경우가 없다면 nonatomic으로 사용해도 무방함
- 스레드 관련 작업은 GCD를 통해 처리
    - GCD: Grand Central Dispatch
    - 클로저 블록 안에 있는 특정 작업을 큐에 올리고, 해당 큐를 특정 스레드에 실행하는 방식
- 구조체가 파라미터로 전달될 때 스레드에 안전(Thread-safe)

### 참고 자료

[[iOS] 멀티 스레드(Multi Thread) 구현 시 고려해야될 것들](https://gwangyonglee.tistory.com/47)

### 스터디

- Dispatch Queue
- Quality of Service(QoS)
- asyncAfter
- 멀티 스레딩을 사용하는 이유

Queue에서 Thread로 넘기는 구조

직접적으로 스레드를 관리하지 않고 Queue를 활용해 작업을 분산 처리