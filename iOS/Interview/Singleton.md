# Singleton 패턴을 활용하는 경우를 예를 들어 설명하시오.

- 여러 객체에서 공용으로 객체를 사용하고 싶을 때 사용한다.
- 일반적으로는 `shared`라는 이름의 상수를 만든다.
- `static` 키워드를 붙인다.
- 이니셜라이저를 `private`으로 만들어서, 외부에서 생성을 못하게 해야 한다.

```swift
class Singleton {
	static let shared: Singleton = Singleton()
	
	var numOfCookie: Int
	
	private init()
}

Singleton.shared.numOfCookie = 5
```

iOS에서는 네트워크 쪽에서 사용한다고 했던 거 같음...

---

iOS에서 주로 사용하는 싱글톤 패턴의 객체

```swift
let screen = UIScreen.main
let userDefaults = UserDefaults.standard
let application = UIApplication.shared
let fileManager = FileManager.default
let notification = NotificationCenter.default
```

### 참고 자료

[[NAROTi][iOS 개발] Singleton Pattern](https://velog.io/@naroti/iOS-개발-Singleton-Pattern-q4k3uzgf0n)