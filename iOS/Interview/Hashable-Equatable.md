# Hashable

정수 해시 값을 제공하고 `Dictionary`의 키가 될 수 있는 타입

`String`, `integer`, `Boolean` 등 표준 라이브러리의 많은 타입은 `Hashable` 을 준수한다. 

`Hashable` 프로토콜은 `Equatable` 프로토콜을 상속받고 있기 때문에, `Hashable` 프로토콜을 채택한 구조체, 열거형에서는 `Equatable`도 같이 준수하게 된다.

```swift
struct GridPoint {
	var x: Int
	var y: Int
}
```

```swift
extension GridPoint: Hashable {
	static func == (lhs: GridPoint, rhs: GridPoint) -> Bool {
		return lhs.x == rhs.x && lhs.y == rhs.y
	}

	func hash(into hasher: inout Hasher) {
		hasher.combine(x)
		hasher.combine(y)
	}
}
```

# Equatable

== 및 ≠ 연산자를 사용하여 값이 동일한지 판단할 수 있는 타입

Swift 표준 라이브러리의 대부분의 기본 타입은 `Equable`을 준수한다.

---

- 다른 객체가 동일한 해시를 가질 수 있기 때문에 먼저 해시 값을 비교하고, 해시 값이 같다면 == 연산을 통해 객체를 비교한다.
- `Hashable` 객체를 Map(Dictionary)의 키로 사용할 수 있다. Map의 키는 중복될 수 없다. 시스템은 키의 해시 값을 이용해 중복을 확인한다.

### 참고 자료

[Why does Hashable require Equatable?](https://forums.swift.org/t/why-does-hashable-require-equatable/16817)

[What is the use of Hashable and Equatable in Swift? When to use which?](https://stackoverflow.com/questions/34915836/what-is-the-use-of-hashable-and-equatable-in-swift-when-to-use-which)