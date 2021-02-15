# 강한 순환 참조 (Strong Reference Cycle) 는 어떤 경우에 발생하는지 설명하시오.

```swift
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```

```swift
var john: Person?
var unit4A: Apartment?
```

```swift
john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")
```

![referenceCycle01](https://docs.swift.org/swift-book/_images/referenceCycle01_2x.png)

특정 `Person` 인스턴스와 `Apartment` 인스턴스를 만들고 할당하면 위 그림과 같이 강력한 참조가 생성된다. 이렇게 만든 인스턴스를 연결하여 `Person` 인스턴스가 아파트를 갖고 `Apartment` 인스턴스에 임차인이 있도록 한다.

```swift
john!.apartment = unit4A
unit4A!.tenant = john
```

![referenceCycle02](https://docs.swift.org/swift-book/_images/referenceCycle02_2x.png)

이렇게 두 인스턴스를 연결하면 두 인스턴스 간에 강한 순환 참조가 생성된다. 그래서 `Person` 인스턴스와 `Apartment` 인스턴스의 참조를 끊어도 참조 횟수가 0으로 떨어지지 않는다.

```swift
john = nil
unit4A = nil
```

![referenceCycle03](https://docs.swift.org/swift-book/_images/referenceCycle03_2x.png)

이러한 강한 순환 참조를 해결하려면 속성을 `weak` 키워드를 이용해 약한 참조를 한다.

```swift
class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    weak var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```

## 참고 자료

[Automatic Reference Counting - The Swift Programming Language (Swift 5.3)](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)