# Global DispatchQueue 의 Qos 에는 어떤 종류가 있는지, 각각 어떤 의미인지 설명하시오.

## QoS (Quality-of-service)

Qos는 원래 네트워크에서 사용하는 용어로 서비스의 중요도에 따라 중요한 서비스에 더 많은 자원을 할당하는 것, 또는 이 중요도를 뜻하는 말

적절하게 QoS를 지정하면 앱의 에너지 효율이 좋아짐

```swift
enum DispatchQoS.QoSClass
```

### userInteractive

메인 스레드에서 작업하거나 사용자 인터페이스를 새로 고치거나 애니메이션을 수행하는 등 사용자와 상호 작용하는 작업

### Initiated

사용자가 시작한 작업으로 저장된 문서를 열거나 사용자가 사용자 인터페이스에서 무언가를 클릭 할 때 작업을 수행하는 등 즉각적인 결과가 필요할 때 사용

### default

기본값

### utility

완료하는데 약간의 시간이 걸리고 데이터 다운로드 또는 가져오기와 같이 즉각적인 결과가 필요하지 않은 작업

### background

인덱싱, 동기화 및 백업과 같이 백그라운드에서 작동하고 사용자에게 표시되지 않는 작업

### unspecified

## 참고 자료

[DispatchQueue의 Qos](https://jcsoohwancho.github.io/2019-10-09-DispatchQueue%EC%9D%98Qos/)

[Prioritize Work with Quality of Service Classes](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html#//apple_ref/doc/uid/TP40015243-CH39-SW1)

[iOS ) Prioritize Work with Quality of Service Classes](https://zeddios.tistory.com/521)

[DispatchQueue - Apple Developer Documentation](https://developer.apple.com/documentation/dispatch/dispatchqueue)