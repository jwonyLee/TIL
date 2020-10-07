# Extension

구조체, 클래스, 열거형, 프로토콜 타입에 새로운 기능을 추가할 수 있다. 기능을 추가하려는 타입을 구현한 소스 코드를 알지 못하거나 볼 수 없다 해도, 타입만 안다면 그 타입의 기능을 확장할 수도 있다.

익스텐션이 타입에 추가할 수 있는 기능

- 연산 타입 프로퍼티, 연산 인스턴스 프로퍼티
- 타입 메서드, 인스턴스 메서드
- 이니셜라이저
- 서브스크립트
- 중첩 타입
- 특정 프로토콜을 준수할 수 있도록 기능 추가
```
⚠️ 기존에 존재하는 기능은 재정의 할 수 없음
```