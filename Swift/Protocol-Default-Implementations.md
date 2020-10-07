# 익스텐션과 프로토콜의 결합

프로토콜의 익스텐션에서는 프로토콜이 요구하는 기능을 실제로 구현해줄 수 있다. 이렇게 프로토콜과 익스텐션을 결합하면 코드의 재사용성이 월등히 증가한다.

이처럼 프로토콜의 요구사항을 익스텐션을 통해 구현하는 것을 프로토콜 초기구현(Protocol Default Implementations)라고 한다.

```swift
protocol SomeProtocol {
	func something()
}

extension SomeProtocol {
	func something() {
		print("like this!")
	}
}
```

이렇게 익스텐션을 통해 구현하면, 동일한 프로토콜을 채택한 모든 클래스나 구조체에서 해당 함수를 구현할 필요가 없다. 만약, 익스텐션으로 구현한 공통적인 기능 외에 추가적인 작업이 필요하다면 채택한 클래스나 구조체 내부에서 재작성하면 된다.

```swift
class SomeClass: SomeProtocol {
	func something() {
		print("why not?")
	}
}
```

프로토콜 초기구현에 제네릭을 사용하면 타입에 대해 더욱 유연하게 동작할 수 있다.