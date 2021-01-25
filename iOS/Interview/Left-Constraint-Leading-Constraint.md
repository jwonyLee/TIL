# Left Constraint 와 Leading Constraint 의 차이점을 설명하시오.

`Left Constraint`는 어떤 객체의 왼쪽을 뜻하고, `Leading Constraint`는 어떤 객체의 앞쪽 가장자리를 뜻한다.

`Left Constrint`와 `Right Constraint`는 절대적이며 항상 화면 또는 컨트롤의 왼쪽 / 오른쪽을 참조한다. `Leading Constraint`와 `Trailing Constraint`는 device locale의 영향을 받는다. (장치별 국가 설정)

읽기 방향이 오른쪽에서 왼쪽인 locale(예: 히브리어, 아랍어)에서는 leading이 오른쪽이 되고 trailing이 왼쪽이 된다.

## 참고 자료

[Understanding Auto Layout](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853-CH7-SW1)

[Difference between leftAnchor and leadingAnchor?](https://stackoverflow.com/questions/32981532/difference-between-leftanchor-and-leadinganchor/32981750)
