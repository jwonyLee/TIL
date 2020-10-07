# instance 메서드와 class 메서드의 차이점을 설명하시오.
instance 메서드는 객체의 인스턴스를 만들어야 사용할 수 있음

```swift
class Dog {

	func bark() {
		print("bow!")
	}
}

let dog: Dog = Dog()
dog.bark() // bow!
```

class 메서드는 초면...

---

## 인스턴스 메소드(Instance Methods)

특정 클래스, 구조체 또는 열거형 인스턴스에 속한 함수. 우리가 일반적으로 알고있는 그 함수가 맞음. 인스턴스 없이 독립적으로 호출할 수 없음.

## 타입 메소드(Type Methods)

클래스를 위한 타입 메소드는 `func` 키워드 앞에 `class` 키워드 작성, 구조체와 열거형을 위한 타입 메소드 앞에는 `static` 키워드 작성

다른 언어에서 정적 메소드(Static Method)라고 표현하는 걸, `Swift`에서는 클래스의 경우 `class`키워드를 붙이는 것이 차이인 거 같음.

`static` 키워드를 붙이면 `override`가 안되고, `class` 키워드를 붙이면 `override`가 되고, 상속이 가능하다.

```swift
class Dog {
	class func bark() {
		print("bow!")
	}
}

Dog.bark() // bow!
```

### 참고 자료

[[Swift]Methods 정리](http://minsone.github.io/mac/ios/swift-methods-summary)