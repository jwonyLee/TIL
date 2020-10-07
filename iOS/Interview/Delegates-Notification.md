# Delegates와 Notification 방식의 차이점에 대해 설명하시오.

# Delegates

- Protocol을 정의하여 사용
- 많은 객체들에게 이벤트를 알려주는 것이 어렵고 비효율적임

많은 객체에게 delegate를 사용해서 이벤트를 알려줘야한다면, 아래와 같은 방식으로 할 수 있지 않을까?

```swift
class Bakery {
	var delegates: [BakeryDelegate?]
	
	func makeCookie() {
		var cookie: Cookie = Cookie()
		cookie.size = 6
		cookie.hasChocolateChips = true

		notifyWasBaked(for: cookie)
	}

	func notifyWasBaked(for cookie: Cookie) {
		for d in delegates {
			d?.cookieWasBaked(cookie)
		}
	}

}
```

# Notification

- Notification Center라는 싱글턴 객체를 사용
- 다수의 객체들에게 동시에 이벤트 발생을 알려줄 수 있음
- 발행 이후 정보를 받을 수 없음
- 추적이 쉽지 않음  
→ 변화가 언제 일어나는지 캐치를 못함 
→ Center에서 관리하기 때문에?

### 참고 자료

[[iOS] Delegate, Notification, KVO 비교 및 장단점 정리](https://you9010.tistory.com/275)

[Delegation, Notification, 그리고 KVO](https://medium.com/@Alpaca_iOSStudy/delegation-notification-그리고-kvo-82de909bd29)