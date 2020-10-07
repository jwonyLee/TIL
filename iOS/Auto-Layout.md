# Auto Layout
> A layout engine that helps layout user interface(UI) based on the constraints you spectify.

> 사용자가 지정한 제약 조건에 따라 레이아웃 사용자 인터페이스(UI)를 지원하는 레이아웃 엔진이다.

안드로이드에서, Constraint Layout과 유사하다.

Auto Layout은 해당 뷰에 배치된 제약 조건을 기반으로 뷰 계층에 있는 모든 뷰의 크기와 위치를 동적으로 계산한다.

```
RedView.Leading = 1.0 * BlueView.trailing + 8.0
```

위의 제약사항 수식은 아래의 수식과 동일하다.

```
BlueView.Trailing = 1.0 * RedView.Leading - 8.0
```

여기서 등호(=)는 프로그래밍에서의 대입할 때 쓰는 대입 연산자가 아니라, 수학에서 같다 라고 표기하는 등호(프로그래밍으로 비유하면 ==)다.

## AutoLayout Attributes

- Size
    - Width
    - Height
- Position
    - Top
    - Left or Leading
    - Right or Trailing
    - Bottom
    - Center Y
    - Center X
- Baseline: 문자열에 밑 바닥 부분을 의미함
- Not An Attribute

Auto Layout의 수식은 `목적 아이템 = 베이스 아이템`의 연산 형태로 되어 있는데 Size와 관련된 Width, Height는 베이스 아이템이 없어서 Not An Attribute를 대신 사용할 수 있다.

```
View.height = 0.0 * NotAnAttribute + 40.0
```

```
💡 Auto Layout의 제약을 주는 방법은 정답이 여러가지가 있을 수 있다. 같은 레이아웃을 만들더라도 사람마다 다른 방식으로 만들 수가 있음.
```

## Content hugging
늘어나지 않으려고 하는 힘, 최대 크기에 제한을 두는 것

## Compression resistance
외부에서 압력을 줄 때 버티는 힘, 최소 크기에 제한을 두는 것

## Constraint with Code

### Anchor
#### 장점
- 코드가 간결해짐
- 컴파일 타임 때 오류를 발견하기 쉬움

#### 주의사항

- `View.Anchor.constraint`는 `NSConstraintLayout`의 인스턴스를 반환함

    ```swift
    let safeBottomAnchor = button.bottomAnchor.constraint(equalTo: safeArea.bottomAnchor)
    ```

    만약 인스턴스를 저장하고 싶지 않으면 아래 코드의 #2와 같이 바로 활성화 시켜주면 됨

- constraint를 만들어주고 활성화를 해줘야 동작

    ```jsx
    // #1
    let safeBottomAnchor = button.bottomAnchor.constraint(equalTo: safeArea.bottomAnchor)
    safeBottomAnchor.isActive = true

    // #2
    button.bottomAnchor.constraint(equalTo: safeArea.bottomAnchor).isActive = true
    ```

- constant의 음수, 양수
- `equalTo`, `lessThanOrEqualTo`, `greaterThanOrEqualTo`

### NSLayoutConstraint

NSLayoutConstraint initializer를 이용해서 제약을 줄 수 있음

```swift
let leading = NSLayoutConstraint(item: button,
                                 attribute: .leading,
                                 relatedBy: .equal,
                                 toItem: safeArea,
                                 attribute: .leading,
                                 multiplier: 1,
                                 constant: 16)
leading.isActive = true
```

여러 개의 NSLayoutConstraint가 있을 때, 한번에 활성화해줄 수 있음

```swift
NSLayoutConstraint.activate([leading, trailing, bottomView, bottomSafeArea])
```

#### 단점

NSLayoutConstraint initializer로 만들면 컴파일러가 오류를 검출해주지 않기 때문에 주의를 기울여서 사용해야 함

## Safe Area

컨텐츠를 안전하게 보여줄 수 있는 영역

`additionalSafeAreaInsets` 프로퍼티를 수정하여 Safe Area를 변경해줄 수 있다.

## Layout Margins

컨텐츠와 뷰 사이의 엣지를 뜻함

### 참고 자료
[Auto Layout Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html)