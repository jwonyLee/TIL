# Fast Enumeration 이란 무엇인지 설명하시오.

Fast Enumeration이라는 개념을 처음 봤다. 그래서 찾아보니 전혀 생소한 개념은 아니고 파이썬이나, 스위프트에서 배열이나 딕셔너리 같이 순회할 수 있는 컬렉션들을 순회할 때 사용하는 문법이다.

```swift
let arr: [Int] = [1, 2, 3, 4, 5]

for a in arr:
	print(a)
```

값을 읽는 정도만 사용한다면 for-in 문이 좋다. (컬렉션의 요소를 수정할 수 없음)

index를 직접 다뤄야하거나, 컬렉션의 요소를 수정해야하는 작업에서는 부적절하다.

> Fast enumeration is a language feature that allows you to efficiently and safely enumerate over the contents of a collection using a concise syntax.

> Fast enumeration은 간결한 구문을 사용하여 컬렉션의 내용을 효율적이고 안전하게 열거할 수 있는 언어 기능이다.

### 참고 자료

[Fast Enumeration](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocFastEnumeration.html)