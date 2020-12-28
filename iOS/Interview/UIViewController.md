# 앱 화면의 콘텐츠를 표시하는 로직과 관리를 담당하는 객체를 무엇이라고 하는가?

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

뷰 컨트롤러의 유형
- 콘텐츠 뷰 컨트롤러는 앱 콘텐츠의 개별 부분을 관리하며 사용자가 만드는 기본 뷰 컨트롤러 유형
- 컨테이너 뷰 컨트롤러는 다른 뷰 컨트롤러(하위 뷰 컨트롤러라고 함)에서 정보를 수집하고 탐색을 용이하게 하거나 해당 뷰 컨트롤러의 콘텐츠를 다르게 표시하는 방식으로 정보 제공

### 뷰 관리

![뷰 컨트롤러와 뷰 간의 관계](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/Art/VCPG_ControllerHierarchy_fig_1-1_2x.png)

![컨테이너 뷰 컨트롤러](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/Art/VCPG_ContainerViewController_fig_1-2_2x.png)

컨테이너 뷰 컨트롤러는 자체 뷰와 하나 이상의 하위 뷰 컨트롤러에서 루트 뷰를 관리한다. 컨테이너는 자식의 콘텐츠를 관리하지 않는다. 컨테이너의 디자인에 따라 루트 뷰만 관리하고 크기를 조정하고 배치한다. 위 이미지는 Split View Controller와 하위 컨트롤러 간의 관계를 보여준다. Split View Controller는 하위 뷰의 전체 크기와 위치를 관리하지만 하위 뷰 컨트롤러는 해당 뷰의 실제 콘텐츠를 관리한다.

### 참고 자료

[The Role of View Controllers](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)