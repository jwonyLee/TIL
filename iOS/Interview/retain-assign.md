# retain 과 assign 의 차이점을 설명하시오.

`Assign` 은 소스의 보유 수를 늘리지 않고 한 객체에서 다른 객체로의 참조를 만든다. 객체가 아닌 `primitive type`에 대해 적합하다.

```objectivec
if (obj1 != obj2) {
	[obj1 release];
	obj1 = nil;
	obj1 = obj2;
}
```

`Retain` 은 한 객체에서 다른 객체로의 참조를 만들고 원본 객체의 유지 수를 늘린다.

```objectivec
if (obj1 != obj2) {
	[obj1 release];
	obj1 = nil;
	obj1 = [obj2 retain];
}
```

## 참고 자료

[What is the difference between retain & assign?](https://www.mindstick.com/interview/12748/what-is-the-difference-between-retain-assign)

[[Obj-C] 접근자 @property, @synthesize, @dynamic / retain, copy, assign, atomic, nonatomic](https://jivepia.tistory.com/81)