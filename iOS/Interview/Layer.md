# UIView 에서 Layer 객체는 무엇이고 어떤 역할을 담당하는지 설명하시오.

## layer

렌더링에 사용되는 뷰의 Core Animation 레이어

```swift
var layer: CALayer { get }
```

이 프로퍼티는 절대 nil일 수 없음. 

~~view는 layer의 delegate이므로 view를 다른 CALayer 객체의 delegate로 만들면 안됨.~~ 

레이어 객체가 뷰에 의해 생성된 경우 일반적으로 뷰는 자신을 레이어의 delegate로 자동 할당하는데 해당 관계는 변경되어선 안됨

## CALayer

이미지 기반 컨텐츠를 관리하고 해당 컨텐츠에 대해 애니메이션을 수행할 수 있는 객체

```swift
class CALayer: NSObject
```

레이어의 기본 작업 → 개발자가 제공하는 시각적 컨텐츠를 관리

## CALayer를 사용하는 이유

- 레이어의 위치와 크기
- 레이어의 배경색
- 레이어에 그려질 컨텐츠 (이미지를 출력하거나 Core Graphic를 통해 그려진 그래픽 등)
- 레이어의 모서리가 둥글게 그려져야 하는지
- 레이어에 그림자 추가하기
- 레이어에 외곽선 그리기

3D transform, masking contents, animation을 할 수 있는 기능 제공

[layer - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/1622436-layer)

[[CoreAnimation]Layer](http://minsone.github.io/mac/ios/coreanimationlayer-and-view)

[CALayer](https://melod-it.gitbook.io/sagwa/graphics-and-games/core-animation/calayer)