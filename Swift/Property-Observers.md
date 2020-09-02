# Property Observers

속성 관찰자는 속성 값이 바뀌는 것을 관찰하고 이에 대해 응답함. 속성 관찰자는 속성의 값을 설정할 때마다 호출되는데, 새로운 값이 속성의 **현재 값과 같더라도** 호출됨.

- `willSet`: 값이 지정되기 바로 전에 호출  
    새 속성 값을 상수 매개 변수로 전달. 이 매개변수의 이름을 따로 지정할 수도 있고, 지정하지 않는다면 `newValue`라는 기본 매개변수 이름으로 사용 가능
- `didSet`: 새 값이 저장된 바로 후에 호출  
    예전 속성 값을 가지고 있는 상수 매개변수를 전달. 이 매개변수에 이름을 따로 지정할 수도 있고, 지정하지 않는다면 `oldValue`라는 기본 매개변수 이름으로 사용 가능

### 참고 자료
[프로퍼티 get, set, didSet, willSet in iOS](https://medium.com/ios-development-with-swift/프로퍼티-get-set-didset-willset-in-ios-a8f2d4da5514)

[Swift 5.2: Properties (속성)](https://xho95.github.io/swift/language/grammar/property/2020/05/30/Properties.html)