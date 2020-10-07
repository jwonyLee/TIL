# Codable

```swift
public typealias Codable = Decodable & Encodable
```

## Decodable, Encodable

사용자 정의 데이터 타입을 다른 형식으로 쉽게 인코딩하고 디코딩할 수 있는 청사진을 제시하는 프로토콜

## Codable을 활용할 수 있는 Foundation 프레임워크의 대표적인 클래스
| Foundation 프레임워크의 클래스 | 효과 |
| ------------------------- | --- |
| JSONEncoder, JSONDecoder | Codable 프로토콜을 준수하는 타입의 데이터를 JSON 문자열로 변환하거나 JSON 문자열을 타입의 인스턴스로 변환할 수 있음 |
| NSKeyedArchiver, NSKeyedUnarchiver | Codable 프로토콜을 준수하는 타입의 데이터를 JSON 문자열로 변환하거나 JSON 문자열을 타입의 인스턴스로 변환할 수 있음 |
| PropertyListEncoder, PropertyListDecoder | Codable 프로토콜을 준수하는 타입의 데이터를 프로퍼티 리스트 데이터로 변환하거나 프로퍼티 리스트 데이터를 타입의 인스턴스로 변환할 수 있음 |

## CodingKey

`CodingKey` 프로토콜을 활용하면 `JSON` 객체의 키 값과 프로퍼티의 이름이 서로 달라도 값을 매칭해줄 수 있음.

```swift
struct Animal: Codable {
	var species: String
	var age: Int
	var birth: Date

	enum CodingKeys: String, CodingKey {
		case species
		case age
		case birth = "date_of_birth"
	}
}
```

## 특정 Key, Value가 없는 경우

`JSON`데이터에 특정 키가 없는 경우, `Codable`을 사용하면 `keyNotFound` 에러가 발생한다. 이러한 상황을 방지해주기 위해서, `init(from decoder: Decoder)`를 호출해서 기본값을 넣어주는 방식으로 해결할 수 있다. 혹은 옵셔널로 처리해도 된다. JSON 값이 null이 들어오는 경우를 생각해야 한다면, 변수를 옵셔널로 선언한다.

### 참고 자료

[[Swift4]Codable, 현실의 Codable 그리고 Extension](http://minsone.github.io/programming/swift-codable-and-exceptions-extension)