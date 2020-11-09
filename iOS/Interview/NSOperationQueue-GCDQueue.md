# NSOperationQueue 와 GCD Queue 의 차이점을 설명하시오.

## NSOperationQueue

NSOperation 객체의 우선 순위 및 준비 상태에 따라 대기열에 있는 객체를 실행한다. Operation queue에 추가 된 작업은 작업이 완료되었다고 보고할 때까지 대기열에 남아있다. 작업이 추가된 후에는 대기열에서 작업을 직접 제거할 수 없다.

- Objective-C API

## GCD Queue (Dispatch Queue)

앱의 기본 스레드 또는 백그라운드 스레드에서 작업 실행을 직렬 또는 동시에 관리하는 개체

작업을 직렬 또는 동시에 실행. 디스패치 큐에 추가된 작업은 시스템에서 관리하는 스레드 풀에서 실행. 

작업 항목을 동기 또는 비동기 적으로 예약함

- 동기 → 해당 작업이 실행을 마칠 때까지 코드가 대기함
- 비동기 → 해당 작업이 다른 곳에서 실행되는 동안 코드가 계속 실행됨
```
⚠️ main queue에서 작업을 동기적으로 실행하려고 하면 교착상태(deadlock) 발생
```
- C API

## 차이점

1. `NSOperations`, `NSOperationQueues`를 사용할 때 오버헤드가 발생함. 
2. GCD는 작업을 추가할 때 바로 `Operation`으로 wrapping 해서 추가할 수 있는데, `NSOperationQueue`는 그게 안된다?
3. `NSOperation`는 작업을 일시 중지, 취소, 재개할 수 있음
4. KVO 사용 가능 (GCD 불가능)
5. 작업 간의 의존성 (작업 계층을 만들 수 있음)

### 참고 자료

[[Objective-C]NSOperation과 NSOperationQueue를 사용하는 방법 - 설명 및 예제](http://minsone.github.io/mac/ios/how-to-using-nsoperation-and-nsoperationqueue)

[NSOperation vs Grand Central Dispatch](https://stackoverflow.com/questions/10373331/nsoperation-vs-grand-central-dispatch)

[Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nsoperationqueue)