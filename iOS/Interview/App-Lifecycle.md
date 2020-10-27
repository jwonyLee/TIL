# 상태 변화에 따라 다른 동작을 처리하기 위한 앱델리게이트 메서드들을 설명하시오.

상태 변화: 앱의 라이프 사이클을 의미. 뷰의 라이프 사이클과 다름

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool
```

앱이 처음 시작될 때 실행  
`launchOptions` 앱이 실행되게 된 이유 등이 포함

```swift
func applicationWillResignActive(_ application: UIApplication)
```

앱이 active 에서 inactive로 바뀔 때 실행  
홈 버튼을 누르면 App이 포커스를 잃으면서 실행된다고 함

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

앱이 background 상태일 때 실행  
공유자원 해제, 유저 데이터 저장 등의 로직 구현

```swift
func applicationWillEnterForeground(_ application: UIApplication)
```

앱이 background에서 foreground로 이동될 때 실행  
보통 API를 통해 앱의 상태를 갱신할 때 사용 (버전 체크 등)

```swift
func applicationDidBecomeActive(_ application: UIApplication)
```

앱이 active 상태가 되어 실행중 일 때

```swift
func applicationWillTerminate(_ application: UIApplication)
```

앱이 종료될 때 실행

### 참고 자료

[앱 생명주기(App Lifecycle) vs 뷰 컨트롤러 생명주기(ViewController Lifecycle) in iOS](https://medium.com/ios-development-with-swift/앱-생명주기-app-lifecycle-vs-뷰-생명주기-view-lifecycle-in-ios-336ae00d1855)

[[iOS] AppDelegate의 역할과 메소드 - JingyuJung's Blog](http://monibu1548.github.io/2018/08/28/appdelegate/)