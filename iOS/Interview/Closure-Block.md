# Swift의 클로저와 Objective-C의 블록은 어떤 차이가 있는가?

일반적인 클로저에 대한 내용은 [탈출 클로저에 대하여 설명하시오.](./Escaping-Closure.md) 문서 참고

## 두 줄 요약

1. Swift의 클로저는 값 타입(value type) 변수를 캡쳐할 때 명시적으로 캡쳐 리스트를 작성하지 않으면 reference capture가 일어난다.
2. Objective-C의 블럭은 값 타입(value type) 변수를 캡쳐할 때 기본적으로 value copy이며, reference copy로 변경하려면 캡쳐할 변수를 선언할 때 `__block` 키워드를 명시하면 된다.

## Capture

Swift의 클로저에서 변수를 캡쳐할 때는 명시적인 캡쳐 리스트를 작성하지 않으면 value type 변수 임에도 불구하고 reference capture가 일어난다.

```swift
var integer = 42

let closure = {
	print("Integer is: \(integer)")
}

integer = 84
closure()
// Prints "Integer is: 84"
```

value copy를 하려면 capture list를 만들어서 변수를 명시해주면 된다.

```swift
var integer = 42

let closure = { [integer] in
	print("Integer is: \(integer)")
}

integer = 84
closure()
// Prints "Integer is: 42"
```

Objective-C의 block은 기본 동작이 value copy이다.

```objectivec
int integer = 42;

void (^block) (void) =^{
	NSLog(@"Integer is: %i", integer);
};

integer = 84;
block();
// Prints "Integer is: 42"
```

이를 reference copy로 변경하려면 capture할 변수 선언시에 `__block` 키워드를 명시하면 된다.

```objectivec
__block int integer = 42;

void (^block) (void) =^{
	NSLog(@"Integer is: %i", integer);
};

integer = 84;
block();
// Prints "Integer is: 84"
```

## Block

일반적으로 객체는 힙(heap)에 할당되지만 블럭은 스택(stack)에 할당되는 객체다. 실행속도 최적화를 위해 기본적으로 스택에 할당 하게된다.

## 참고 자료

[Swift Closure vs. Objective-C Block 차이점 비교 분석](https://www.letmecompile.com/swift-closure-vs-objective-c-block/)