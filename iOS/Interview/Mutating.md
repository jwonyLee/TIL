# mutating 키워드에 대해 설명하시오.

구조체에서, 함수가 내부 변수의 값을 수정하려면 `mutating` 키워드를 붙여야 한다.

```swift
struct Person {

	var name: String

	mutating func modify(name: String) {
		self.name = name
	}
}
```

---

값 타입(구조체와 열거형)의 인스턴스 메서드에서 자신 내부의 값을 변경하고자 할 때 사용하는 키워드

> Structures and enumerations are value types. By default, the properties of a value type cannot be modified from within its instance methods.  
> 
> However, if you need to modify the properties of your structure or enumeration within a particular method, you can opt in to mutating behavior for that method. The method can then mutate (that is, change) its properties from within the method, and any changes that it makes are written back to the original structure when the method ends.

보통 값 타입의 프로퍼티는 인스턴스 메서드에서 수정할 수 없다. 

그러나 구조체나 열거형의 인스턴스 메서드에서 프로퍼티를 수정하길 원한다면 `mutating`을 채택해서 할 수 있다. `mutating`을 채택하면 메서드 내에서 프로퍼티를 변경할 수 있으며 메서드가 종료되면 변경 내용이 원래 구조에 다시 기록된다. 

> The method can also assign a completely new instance to its implicit self property, and this new instance will replace the existing one when the method ends.

> Assigning to self Within a Mutating Method  
> 
> Mutating methods can assign an entirely new instance to the implicit self property. The Point example shown above could have been written in the following way instead:

Mutating 메서드는 암시적인 속성인 `self`에 완전히 새로운 인스턴스를 할당할 수 있다. 

```swift
struct Point {
  var x = 0.0 y = 0.0
  mutating func moveBy(x deltaX: Double, y deltaY: Double) {
    self = Point(x: x + deltaX, y: y + deltaY)
  }
}
```

### 참고 자료

[Methods - The Swift Programming Language (Swift 5.3)](https://docs.swift.org/swift-book/LanguageGuide/Methods.html)

[Swift 5.2: Methods (메소드)](https://xho95.github.io/swift/language/grammar/method/2020/05/03/Methods.html)