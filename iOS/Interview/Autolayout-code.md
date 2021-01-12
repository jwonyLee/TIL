# 오토레이아웃을 코드로 작성하는 방법은 무엇인가? (3가지)

## 1. Layout Anchors

```swift
// Get the superview's layout
let margins = view.layoutMarginsGuide
 
// Pin the leading edge of myView to the margin's leading edge
myView.leadingAnchor.constraint(equalTo: margins.leadingAnchor).isActive = true
 
// Pin the trailing edge of myView to the margin's trailing edge
myView.trailingAnchor.constraint(equalTo: margins.trailingAnchor).isActive = true
 
// Give myView a 1:2 aspect ratio
myView.heightAnchor.constraint(equalTo: myView.widthAnchor, multiplier: 2.0).isActive = true
```

## 2. NSLayoutConstraint Class

1 의 방식과 달리 레이아웃에 영향을 주지 않더라도 각 매개 변수에 대한 값을 지정해야 한다.

```swift
NSLayoutConstraint(item: myView, attribute: .leading, relatedBy: .equal, toItem: view, attribute: .leadingMargin, multiplier: 1.0, constant: 0.0).isActive = true
 
NSLayoutConstraint(item: myView, attribute: .trailing, relatedBy: .equal, toItem: view, attribute: .trailingMargin, multiplier: 1.0, constant: 0.0).isActive = true
 
NSLayoutConstraint(item: myView, attribute: .height, relatedBy: .equal, toItem: myView, attribute:.width, multiplier: 2.0, constant:0.0).isActive = true
```

iOS 8 또는 OS X 10.10 또는 이전 버전을 지원해야하는 경우가 아니라면 Layout Anchors 방식으로 마이그레이션하는 것이 권장됨

## 3. Visual Format Language

문자열과 같은 ASCII를 이용해 제약 조건을 정의할 수 있음

```swift
let views = ["myView" : myView]
let formatString = "|-[myView]-|"
 
let constraints = NSLayoutConstraint.constraints(withVisualFormat: formatString, options: .alignAllTop, metrics: nil, views: views)
 
NSLayoutConstraint.activate(constraints)
```

| 제약 조건 | Visual Format Language | Image |
| ------- | ---------------------- | ----- |
| 표준 공간 | `[button]-[textField]` | ![표준 공간](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/standardSpace.png) |
| 폭 제약 | `[button(>=50)]` | ![폭 제약](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/widthConstraint.png) |
| Superview에 연결 | `|-50-[purpleBox]-50-|` | ![Superview에 연결](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/connectionToSuperview.png) |
| 수직 레이아웃 | `V: [topField]-10-[bottomField]` | ![수직 레이아웃](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/verticalLayout.png) |
| 플러시 뷰 | `[maroonView][blueView]` | ![플러시 뷰](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/flushViews.png) |
| 우선 순위 | `[button(100@20)]` | ![우선 순위](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/priority.png) |
| 동일한 폭 | `[button1(==button2)]` | ![동일한 폭](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/equalWidths.png) |
| Multiple Predicates | `[flexibleButton(>=70, <=100)]` | ![Multiple Predicates](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/multiplePredicates.png) |
| A Complete Line of Layout | `|-[find]-[findNext]-[findField(>=200)]=|` | ![A Complete Line of Layout](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/Art/completeLayout.png) |


## 참고 자료

[Programmatically Creating Constraints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/ProgrammaticallyCreatingConstraints.html#//apple_ref/doc/uid/TP40010853-CH16-SW1)

[Visual Format Language](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html#//apple_ref/doc/uid/TP40010853-CH27-SW1)