# 특정 객체를 autorelease 하기 위해 필요한 사항과 과정을 설명하시오.

`Foundation`에서는 `autorelease pool`이라는 기능을 사용하여 함수 내에서 생성한 객체들을 적절한 시점에 한 번에 해제할 수 있도록 해주는 방법을 제공한다.

## ARC를 사용하는 경우

autorelease pool을 직접 사용할 수 없고, `@autoreleasepool` 블록을 사용한다.

```objectivec
NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
// Codebenefitting from a local autorelease pool.
[pool release];
```

```objectivec
@autoreleasepool {
	// Code benefitting from a local autorelease pool.
}
```

`@autoreleasepool` 블록은 직접 인스턴스를 사용하는 것보다 더 효율적이다.

## ARC를 사용하지 않는 경우?

객체의 참조 카운트를 감소시킬 때 `release` 대신 `autorelease`를 사용하면 된다.

```objectivec
Person *aPerson = [[Person alloc] init];
// [aPerson release]; delete now
[aPerson autorelease]; // delete later
```

## 참고 자료

[Objective-C의 autorelease 이해하기(1)](https://nephilim.tistory.com/120)

[Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsautoreleasepool)

[[Objective-C] Objective-C의 메모리 관리 방법 · Wireframe](https://soooprmx.com/archives/4174)