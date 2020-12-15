# 모든 View Controller 객체의 상위 클래스는 무엇이고 그 역할은 무엇인가?

Container ViewController

- `UINavigationController`
- `UITabBarController`
- `UITableViewController`
- `UIPageViewController`
- `UISplitViewController`
- `UIPopoverController`
- 등등

위와 같은 뷰 컨트롤러들은 `UIViewController`를 상속받는다.

## UIViewController

UIKit 앱의 뷰 계층 구조를 관리하는 객체

```swift
class UIViewController: UIResponder
```

뷰 컨트롤러의 주요 책임

- 기본 데이터의 변경에 대한 응답으로 뷰의 콘텐츠를 업데이트
- 뷰와 사용자 상호 작용에 응답
- 뷰 크기 조정 및 전체 인터페이스의 레이아웃 관리
- 앱에서 다른 뷰 컨트롤러를 포함한 다른 객체와 조정

### 참고 자료

[[iOS 앱 만들기 005] 뷰 컨트롤러의 종류 · Wireframe](https://soooprmx.com/archives/4496)

### 스터디

UIResonder: 이벤트가 발생하면, UIKit은 이를 처리할 수 있도록 앱의 리스폰더 객체에 전달