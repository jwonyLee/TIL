# View 객체에 대해 설명하시오.

## View

사용자 인터페이스의 기본 구성 요소

## UiView

```swift
class UIView: UIResponder
```

화면의 직사각형 영역에 대한 콘텐츠를 관리하는 객체. 모든 뷰에 공통적인 동작을 정의하며 `UIButton`, `UIImageView`, `UILabel` 과 같은 모든 뷰 클래스의 상위 클래스

- 사용자와 상호 작용
    - 그리기 및 애니메이션  
        `Core Graphics`, `UIViewAnimations`, `CoreAnimation`

    - 레이아웃 및 하위보기 관리  
        오토레이아웃

    - 이벤트 처리  
        - `UIResponder` → 터치 및 기타 유형의 이벤트 응답  
        - 제스처 인식

### 스레딩

사용자 인터페이스에 대한 조작은 메인 스레드에서 해야 함. 메인 스레드가 필요하지 않을 수 있는 유일한 경우는 **뷰 객체를 생성**할 때 뿐이고, 그 외에 모든 조작은 메인 스레드에서 발생해야 함.

### 참고 자료

[UIView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview)