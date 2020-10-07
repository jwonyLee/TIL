# KVO 동작 방식에 대해 설명하시오.

Notification Center와 비슷하게 동작하는 거 같다. 다른 점이라고 하면, KVO는 프로퍼티를 감지하고, Notification Center는 객체를 감지한다는 점?

---

# KVO: Key-Value Observing

A 객체에서 B 객체의 프로퍼티가 변화됨을 감지할 수 있는 패턴. 프로퍼티의 상태에 반응하는 형태.

- `NSObject`를 상속받아야 하고, 클래스에서만 사용 가능
- `@objc dynamic`
- Key Path
    - Key Path를 이용하여 값을 변경하거나 접근할 수 있다.

    ```swift
    \Type.Path.Path.Path
    ```

## 동작 방식

1. 감지하려는 객체에 옵저버를 등록한다.
    - Key Path: 감시하고자 하는 프로퍼티 지정
    - Options: 값이 변화할 때, 어떤 시점의 값을 돌려받을 지 지정
    - old: 변경 이전 값, oldKey로 참조
    - new: 새로 변경된 값, newKey로 참조
    - initial: 옵저버 등록이 완료되기 전에 옵저버에게 알림을 한 번 보냄. 현재의 값을 newKey에 담아서 보냄
    - prior: 변경이 일어날 때, 변경 전후로 알림을 별도로 보냄.
2. 객체의 변화가 일어났을 때 옵저버의 메시지를 받는다.
3. 감시를 중단하고 싶으면 옵저버를 제거하면 된다.
    - iOS9 이전에는 객체가 해제되기 전에 옵저버를 제거하지 않으면 메모리 릭이나 크래시 등이 발생하였음, iOS9 이후에는 시스템이 자동으로 제거해주기 때문에 직접 제거하지 않아도 됨.

### 참고 자료

[KVO(Key-Value Observing)](https://velog.io/@delmasong/KVOKey-Value-Observing)

[Swifty하게 KVO 사용하기](https://wnstkdyu.github.io/2018/05/20/swiftykvo/)

[Key-Value Observing](https://wnstkdyu.github.io/2018/05/01/kvoprogrammingguide/)

[Key-Value Observing(Key-Value Observing)](https://jcsoohwancho.github.io/2019-11-30-KVO(Key-Value-Observing)/)

### 스터디하면서 알게된 점
- Based on KVC
- willSet, didSet과 비슷하지만 KVO는 타입 선언 밖에서 옵저버를 추가함
- Objective-C runtime에 의존함
- Notification works by replacing your accessors.
- this means that direct ivar access will not produce notifinations!