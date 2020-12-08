# UIWindow 객체의 역할은 무엇인가?

> The backdrop for your app’s user interface and the object that dispatches events to your views.

사용자 인터페이스에 배경을 제공하고, 중요한 이벤트 처리 행동을 제공하는 객체

```swift
class UIWindow: UIView
```

- 앱의 콘텐츠를 표시할 기본 윈도우 제공
- 추가 콘텐츠를 표시하려면 필요한 경우 추가 `window`를 만듦

일반적으로 `Xcode`에서 `iOS` 프로젝트를 만들면 스토리 보드에서 자동으로 생성함 → 스토리보드를 사용하지 않는 경우 `window`를 직접 만들어야 함

- z축 설정
- `window`를 표시하고 이를 키보드 이벤트의 대상으로 만듦
- `window`의 좌표계간에 좌표 값을 변환
- `window`의 루트 뷰 컨트롤러 변경
- `window`가 표시되는 화면 변경

`window`에는 고유한 시각적 모양이 없음. 대신 `window`의 루트 뷰 컨트롤러에서 관리하는 하나 이상의 `view`를 호스팅함

## 키보드 상호 작용 이해
터치 이벤트는 발생한 `window`로 전달되는 반면, 관련 좌표 값이 없는 이벤트는 `key window`로 전달됨. 한 번에 하나의 `window`만 `key window`가 될 수 있으며 `window`의 속성을 사용하여 상태를 확인할 수 있음. 대부분의 경우 앱의 기본 `window`는 `key window`이지만 `UIKit`은 필요에 따라 다른 `window`를 지정할 수 있음

어떤 `window`가 핵심인지 알아야하는 경우 `didBecomeKeyNotification`과 `didResignKeyNotification`을 구독하면 된다. (Notification) 시스템은 앱의 `key window` 변경에 대한 응답으로 알림을 보냄.