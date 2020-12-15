# 앱이 시작할 때 main.c 에 있는 UIApplicationMain 함수에 의해서 생성되는 객체는 무엇인가?

결론: `UIApplication` 싱글턴 객체가 생성됨

---

## UIApplicationMain(_ :_ :_ :_ :)

응용 프로그램 객체 및 응용 프로그램 대리자를 만들고 이벤트 주기를 설정함

---

```swift
func UIApplicationMain(_ argc: Int32, 
                     _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>, 
                     _ principalClassName: String?, 
                     _ delegateClassName: String?) -> Int32
```

### Parameters

**argc**

argv의 인수 개수. 일반적으로 main에 해당하는 매개변수

**argv**

인수의 가변 목록. 일반적으로 main에 해당하는 매개 변수

**principalClassName**

`UIApplication` 클래스 또는 하위 클래스의 이름. nil을 지정하면 `UIApplication`이 가정된다.

**delegateClassName**

응용 프로그램 대리자가 인스턴스화되는 클래스의 이름. principalClassName이 `UIApplication`의 서브 클래스를 지정하면 서브 클래스를 대리자로 지정할 수 있다. 하위 클래스 인스턴스는 응용 프로그램 위임 메시지를 받는다. 응용 프로그램의 기본 nib 파일에서 델리게이트 객체를 로드하는 경우 nil을 지정함

### Return Value

정수 값이 지정 되었더라도 이 함수는 반환하지 않는다. 사용자가 홈 버튼을 눌러 iOS 앱을 종료하면 애플리케이션이 백그라운드로 이동함

### Discussion

이 함수는 주 클래스에서 응용 프로그램 객체를 인스턴스화하고 지정된 클래스에서 대리자를 인스턴스화하고 (있는 경우) 응용 프로그램에 대한 대리자를 설정한다. 또한 응용 프로그램의 실행 루프를 포함하여 기본 이벤트 루프를 설정하고 이벤트 처리를 시작한다. 응용 프로그램의 Info.plist 파일이 NSMainNibFile 키와 값에 유효한 nib 파일 이름을 포함하여 로드 할 기본 bib 파일을 지정하는 경우 이 함수는 해당 nib 파일을 로드한다.

선언된 반환 타입이 있음에도 불구하고, 이 함수는 반환하지 않는다.

## UIApplication

```swift
class UIApplication: UIResponder
```

### Overview

모든 iOS 앱에는 정확히 하나의 `UIApplication` 인스턴스 (또는 매우 드물게 `UIApplication`의 하위 클래스)가 있다. 앱이 시작되면 시스템은 `UIApplicationMain(_:_:_:_:)` 함수를 호출한다. among its other tasks, 이 함수는 싱글톤 `UIApplication` 객체를 만든다. 그 후 공유 클래스 메서드를 호출하여 객체에 액세스한다.

애플리케이션 객체의 주요 역할은 들어오는 사용자 이벤트의 초기 라우팅을 처리하는 것이다. 컨트롤 객체(`UIControl` 클래스의 인스턴스)에 의해 전달된 작업 메시지를 적절한 대상 객체에 전달한다. 애플리케이션 객체는 open windows (`UIWindow` 객체) 목록을 유지하며 이를 통해 앱의 `UIView` 객체를 검색 할 수 있다.

`UIApplication` 클래스는 `UIApplicationDelegate` 프로토콜을 준수하고 프로토콜의 일부 메서드를 구현해야 하는 대리자를 정의한다. 애플리케이션 객체는 대리자에게 앱 시작, 메모리 부족 경고 및 앱 종료와 같은 중요한 런타임 이벤트를 알려 적절히 응답 할 수 있는 기회를 제공한다.

앱은 `openURL(_:)` 메서드를 통해 이메일 또는 이미지 파일과 같은 리소스를 협력적으로 처리할 수 있다. 예를 들어 이메일 URL로 이 메서드를 호출하는 앱은 메일 앱을 시작하고 메시지를 표시한다.

이 클래스의 API를 사용하면 장치별 동작을 관리할 수 있다.

`UIApplication` 객체를 사용하여 다음과 같은 동작을 수행할 수 있다:

- 들어오는 터치 이벤트를 일시적으로 중단 → `beginIgnoringInteractionEvents()`
- 원격 알림 등록 → `registerForRemoteNotifications()`
- UI 실행 취소-다시 실행 트리거 → `applicationSupportsShakeToEdit`
- URL 체계를 처리하기 위해 등록된 앱이 설치되어 있는지 확인 → `canOpenURL(_:)`
- 백그라운드에서 작업을 완료 할 수 있도록 앱 실행 확장 → `beginBackgroundTask(expirationHandler:)`, `beginBackgroundTask(withName:expirationHandler:)`
- 로컬 알림 예약 및 취소 → `scheduleLocalNotification(:)`*,* `cancelLocalNotification(:)`
- 원격 제어 이벤트 수신 조정 → `beginReceivingRemoteControlEvents()`, `endReceivingRemoteControlEvents()`
- 앱 수준 상태 복원 작업 수행 (상태 복원 동작 관리 작업 그룹의 방법)

### Subclassing Notes

대부분의 앱은 `UIApplication`을 하위 클래스화할 필요가 없다. 대신 앱 델리게이트를 사용하여 시스템과 앱 간의 상호 작용을 관리한다.

앱이 수신 이벤트를 시스템이 처리하기 전에 처리해야하는 경우 (매우 드문 경우) 사용자 지정 이벤트 또는 작업 전달 메커니즘을 구현할 수 있다. 이렇게하려면 `UIApplication`을 하위 클래스로 만들고 `sendEvent(_ :)` 및 / 또는 `sendAction(_:to:from:for:)` 메서드를 재정의한다. 인터셉트하는 모든 이벤트에 대해 이벤트를 처리 한 후 [super sendEvent:event]를 호출하여 시스템에 다시 전달한다. 이벤트 차단은 거의 필요하지 않으며 가능하면 피해야 한다.

### 참고 자료

[앱델리게이트 이해하기 (iOS앱 만들기 - 01) · Wireframe](https://soooprmx.com/archives/4454)

[UIApplicationMain - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/1622933-uiapplicationmain)

[UIApplication - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiapplication)