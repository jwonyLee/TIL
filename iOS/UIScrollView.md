# UIScrollView 만들기

강의대로 `UIScrollView`의 오토 레이아웃 제약사항을 0, 0, 0, 0을 주면 공포의 빨간줄이 뜬다. 😱 그리고 이런 오류가 뜬다.  

> scrollview has ambiguous scrollable content height and width

찾아보니까 Xcode 11부터 만드는 방법이 달라졌다. 아래 링크의 글이 설명이 잘 되어 있어서 해결 할 수 있었다.

요약하자면, `ScrollView` 내부의 `View`를 추가하고, 다음과 같은 제약사항을 `View`에 주면 된다.

```swift
View.bottom = Content Layout Guide.bottom
View.top = Content Layout Guide.top
View.leading = Content Layout Guide.leading
View.trailing = Content Layout Guide.trailing
View.width = Frame Layout Guide.width
View.height = Frame Layout Guide.height
```

`contentLayoutGuide`: `ScrollView`의 컨텐츠 영역과 관련된 오토 레이아웃 제약 조건을 만드려면 사용

`frameLayoutGuide`: `ScrollView` 자체를 포함하여 오토 레이아웃 제약 조건을 만드려면 사용

### 참고 자료
[[iOS] Xcode11 새로워진 UIScrollView 만들기 - Kyungmo's Blog](https://kyungmosung.github.io/2019/11/06/xcode-scrollview/)