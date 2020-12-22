# 앱의 콘텐츠나 데이터 자체를 저장/보관하는 특별한 객체를 무엇이라고 하는가?

## UserDefaults

키-값 형태로 데이터를 저장하고, 사용할 수 있는 데이터 저장소

사용자 기본 설정과 같은 단일 데이터 값에 적합함

`SomeObject`는 `Codable`을 채택하고 있음

### 저장

```swift
if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
	do {
		try UserDefaults.standard.setObject(appDelegate.someObject, forKey: "someObject")
	} catch {
		print(error.localizedDescription)
	}
}
```

### 사용

```swift
do {
	let someObject = try UserDefaults.standard.getObject(forKey: "someObject", castTo: SomeObject.self)
	if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
		appDelegate.someObject = someObject
	}
} catch {
	print(error.localizedDescription)
}
```

## 참고 자료

[Apple Developer Documentation - UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)

[iOS ) 왕초보를 위한 User Defaults사용해보기(switch)](https://zeddios.tistory.com/107)

[Apple Developer Documentation - Data and Storage](https://developer.apple.com/documentation/bundleresources/information_property_list/data_and_storage)

[Call function when if value in NSUserDefaults.standardUserDefaults() changes](https://stackoverflow.com/questions/36608645/call-function-when-if-value-in-nsuserdefaults-standarduserdefaults-changes)