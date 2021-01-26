# ARC란 무엇인지 설명하시오.

## RC(Reference Counting)

애플에서 메모리를 관리하는 방법

- 메모리를 할당하거나, 메모리 포인터를 **참조**할 때 레퍼런스 카운트 증가
- 사용을 완료하면 레퍼런스 카운트 감소

## MRC(Manual Reference Counting)

- 개발자가 직접 참조 관리

## ARC(Automatic Reference Counting)

- 컴파일 타임에 자동으로 구문 분석 후 적절하게 레퍼런스 감소 코드 삽입
- 실행 중에 별도의 메모리 관리가 이루어지지 않음
- 참조 카운팅은 클래스의 **인스턴스에만** 적용
    - 구조체와 열거체는 참조 타입이 아니라, 값 타입이라서 참조의 형태로 저장되거나 전달되지 않음
    - 값 타입(value type)은 스택이라는 정적 메모리 공간에 생기는 것이라서 메모리 관리의 대상이 아님

### ARC의 작동 방식

클래스에 대한 인스턴스를 새로 생성할 때마다, ARC는 해당 인스턴스 정보를 저장하기 위한 메모리를 할당한다. 이 메모리는 해당 인스턴스의 타입 정보 및, 그 인스턴스와 결합된 모든 저장 속성의 값들을 함께 가지고 있다.

인스턴스가 더 이상 필요하지 않을 경우, ARC는 해당 인스턴스가 사용하고 있는 메모리를 해제하여 확보한다. 그 메모리는 다른 용도로 사용할 수 있고, 이는 클래스 인스턴스가 더 이상 필요없는 경우 메모리 공간을 차지하지 않음을 보장한다.

인스턴스가 필요한 동안에 해당 인스턴스가 사라지지 않게 하기 위해, ARC는 각각의 클래스 인스턴스를 참조하는 속성, 상수, 변수를 추적한다. ARC는 해당 인스턴스에 대한 활성화된(active) 참조가 하나라도 존재한다면 인스턴스의 할당을 해제하지 않는다.

이것을 가능하게 하기 위해, 클래스 인스턴스를 속성, 상수, 변수에 할당할 때마다, 해당 속성, 상수, 변수는 그 인스턴스에 대한 **강한 참조(strong reference)**를 만든다. 이 참조를 강한(strong) 참조라고 하는 이유는 이것이 해당 인스턴스를 꽉 쥐고 있어서, 해당 강한 참조가 남아 있는 동안 할당이 해제되는 것을 허용하지 않는다.

### 클래스 인스턴스 사이의 강한 참조 순환

클래스 인스턴스에 대한 강한 참조를 없애는 것이 절대로(never) 안되는 경우가 있다. 이는 두 클래스 인스턴스가 서로에 대한 강한 참조를 쥐고 있어서, 각 인스턴스가 서로 계속 살아있게 될 때 발생한다. 이를 강한 참조 순환(strong reference cycle)이라고 한다.

![arc-1](./image/arc-1.png)

![arc-2](./image/arc-2.png)

`john`과 `unit4A` 변수의 강한 참조를 끊더라도, 참조 개수는 0으로 떨어지지 않고, 인스턴스는 ARC에 의해 해제되지 않는다.

강한 참조 순환은 `Person`과 `Apartment` 인스턴스가 해제되는 것을 막으므로, 앱에서 메모리 누수를 발생시킨다. (`Person` 인스턴스와 `Apartment` 인스턴스 사이의 강한 참조가 남아 있으므로)

### 클래스 인스턴스 사이의 강한 참조 순환 해결하기

- 약한 참조 (weak reference)

    다른 인스턴스의 수명이 더 짧을 때 사용한다. (다른 인스턴스의 할당이 먼저 해제되는 경우)

- 무소속 참조 (unowned reference)
다른 인스턴스가 같거나 더 긴 수명을 가질 때 사용한다.

약한 참조와 무소속 참조는 참조 순환에 있는 인스턴스 하나가 다른 인스턴스를 강하게 쥐고 있지 않아도(without) 참조하도록 해준다. 이 인스턴스들은 강한 참조 순환을 생성하지 않아도 서로를 참조할 수 있다.

### Weak References (약한 참조)

참조하는 인스턴스를 강하게 쥐지 않는 참조 → ARC가 참조된 인스턴스를 처분하는 것을 중지하지 않음

> ARC가 약한 참조를 `nil`로 설정할 때는 property observers가 호출되지 않는다.

### Unowned References (무소속 참조)

다른 인스턴스가 같은 수명 또는 더 긴 수명을 가지고 있을 때 사용

항상 값을 가지고 있어야 하고, 옵셔널이 될 수 없으며, ARC는 절대로 무소속 참조의 값을 `nil`로 설정할 수 없음

> 무소속 참조는 해당 참조가 해제되지 않은 인스턴스만 항상 참조한다고 확신할 수 있을때만 사용
해당 인스턴스가 해제된 후에 무소속 참조의 값에 접근하려고 하면, 런타임 에러가 발생

### 참고자료

[프로퍼티 get, set, didSet, willSet in iOS](https://medium.com/ios-development-with-swift/프로퍼티-get-set-didset-willset-in-ios-a8f2d4da5514)

[Swift 5.2: Properties (속성)](https://xho95.github.io/swift/language/grammar/property/2020/05/30/Properties.html)

[[iOS Swift] RC, ARC 와 MRC 란? 그리고 Strong, Weak, Unowned 는? 간단하게 적어봤습니다.](https://medium.com/@jang.wangsu/ios-swift-rc-arc-와-mrc-란-그리고-strong-weak-unowned-는-간단하게-적어봤습니다-988a293c04ac)

[Swift 5.3: Automatic Reference Counting (자동 참조 카운팅)](https://xho95.github.io/swift/language/grammar/arc/automatic/reference/counting/2020/06/30/Automatic-Reference-Counting.html#fn:reference-type)