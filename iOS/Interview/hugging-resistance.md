# hugging, resistance에 대해서 설명하시오.

![hugging resistance](./image/hugging-resistance.png)

## Content hugging

늘어나지 않으려고 하는 힘, 최대 크기에 제한을 두는 것. 뷰를 안쪽으로 당겨 콘텐츠 주변에 꼭 맞도록 한다. 
→ 주어진 크기보다 작아질 수 있음

## Compression resistance

외부에서 압력을 줄 때 버티는 힘, 최소 크기에 제한을 두는 것. 콘텐츠를 자르지 않도록 뷰를 바깥쪽으로 밀어낸다.
→ 주어진 크기보다 커질 수 있음

Content hugging은 기본값이 250, Compression Resistance는 기본값이 750이다. 따라서 뷰를 줄이는 것보다 늘리는 게 더 쉽다.

| Place a label on a storyboard | Constraints |
| ----------------------------- | ----------- |
| ![Place a label on a storyboard](./image/storyboard.png) | ![Constraints](./image/constraint.png) |

![Error](./image/error.png)

| Right Label Content Hugging Priority = 750 | Left Label Content Hugging Priority = 750 | 
| ------------------------------------------ | ------------------------------------ |
| ![Right Label Content Hugging Priority = 750](./image/rightLabel.png) | ![Left Label Content Hugging Priority = 750](./image/leftLabel.png) |

## 참고 자료

[Anatomy of a Constraint](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/AnatomyofaConstraint.html#//apple_ref/doc/uid/TP40010853-CH9-SW21)

[Content hugging vs Compression resistance 차이점 알기!](https://ontheswift.tistory.com/21)

[[AutoLayout] Hugging priority와 Compression Resistance priority 비교](https://eunjin3786.tistory.com/43)