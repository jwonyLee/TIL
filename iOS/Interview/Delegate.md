# Delegate 패턴을 활용하는 경우를 예를 들어 설명하시오.

`Delegate`의 사전적 정의: 위임(자)

`Protocol`을 이용해서 권한을 위임하고 일을 처리하는 방식의 디자인 패턴이다.

이걸 어떻게 권한을 위임하냐면, 아래 코드처럼 같은 프로토콜을 채택한 클래스에게 권한을 위임한다. (뇌피셜 코드)

```swift
protocol ADelegate {
}

class A {
	var delegate: ADelegate
}

class B: ADelegate {
	a.delegate = self
}
```

---

# Delegate Pattern

클래스나 구조체가 자신의 책임이나 임무를 다른 타입의 인스턴스에게 위임하는 디자인 패턴. 책무를 위임하기 위해 정의한 프로토콜을 준수하는 타입은 자신에게 위임될 일정 책무를 할 수 있다는 것을 보장.

이해하기 쉬운 예제가 있어서 번역했는데, 번역한 글을 올리는 걸 원하지 않으셔서 링크로 대체

[Delegation in Swift Explained (How To) - LearnAppMaking](https://learnappmaking.com/delegation-swift-how-to/)