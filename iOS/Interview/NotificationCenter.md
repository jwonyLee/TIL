# NotificationCenter 동작 방식과 활용 방안에 대해 설명하시오.

## 동작 방식

1. 옵저버를 등록한다.
2. 시스템에서 등록된 옵저버를 감시하면서 변경사항이 발생하면 1을 등록한 객체에게 알려준다.

## 활용 방안

다른 객체의 변경 사항을 알고 싶을 때? → 화면의 가로세로 전환되었을 때 라던가

---

## 동작 방식

### 구성 요소

- 객체 A : listener
- 객체 B : sender
- NotificationCenter

1. 객체 A는 객체 B의 어떠한 행위를 관찰하기 위해 NotificationCenter에 옵저버를 등록한다.

    옵저버에는 어떤 객체를 관찰할 것인지, 어떤 행위를 관찰할 것인지 등이 들어감

2. 객체 A가 어떠한 행위를 한다. 
3. 객체 A는 알림을 생성하고 NotificationCenter에 post함
4. NotificationCenter는 객체 B에게 등록한 옵저버에 대한 알림이 발생했다고 알려줌

## 활용 방안

몇 번 사용해보기는 했는데, 아직 잘 모르겠다. 활용 방안도 찾아봤는데 검색 능력 부족으로 못 찾겠음

### 참고 자료

[Using Notification Center In Swift (How To) - LearnAppMaking](https://learnappmaking.com/notification-center-how-to-swift/)