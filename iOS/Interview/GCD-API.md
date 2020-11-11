# GCD API 동작 방식과 필요성에 대해 설명하시오.

**동작 방식**

해야 할 일(코드)을 Operation으로 Wrapping한 다음에, Queue에 넣는다. Queue에서 남는 스레드에 작업을 배분한다.

**필요성**

웹에서 이미지를 다운 받아서 사용자에게 보여준다고 했을 때, 비동기로 처리하지 않는다면 이미지를 다운받는 동안 다른 작업을 할 수 없기 때문에 앱이 멈춘다. 이렇게 비용이 많이 들어가는? 작업을 메인 스레드에서 진행하면 사용자가 다른 작업을 할 수 없기 때문에 필요하다고 생각한다.

---

## DispatchQueue

```swift
class DispatchQueue: DispatchObject
```

DispatchQueue는 애플리케이션이 블록 객체 형태로 작업을 제출할 수 있는 FIFO Queue

- DispatchQueue는 작업을 직렬 또는 동시에 실행함
- DispatchQueue에 제출된 작업은 시스템에서 관리하는 스레드 풀에서 실행됨
- 앱의 기본 스레드를 나타내는 DispatchQueue를 제외하고 시스템은 작업을 실행하는 데 사용하는  스레드에 대해 보장하지 않음

main queue에서 작업 항목을 동기적으로 실행하려고 하면 교착 상태(deadlock)가 발생

### 동작 방식

```swift
DispatchQueue.main.async {
	print("main sync")
}
```

`DispatchQueue.main`

- main thread queue
- 기본적으로 Serial Queue(직렬 큐)로 동작

`DisptchQueue.global`

- background thread queue
- 기본적으로 Concurrent Queue(병렬 큐)로 동작
- `QoS`를 이용해 우선 순위를 정해줄 수 있음
    - User-interactive: 즉시 완료해야하는 작업을 나타냄. UI 업데이트, 이벤트 처리 등에 사용. 메인 스레드에서 실행되어야 함.
    - User-initiated: 사용자 상호 작용을 계속하는 데 필요한 작업을 기다리고 있을 때 사용.
    - Utility: 사용자에게 표시되는 진행률 표시가 있는 장기 실행 작업을 나타냄. 계산, I/O, 네트워킹, 연속 데이터 피드 및 유사한 작업에 사용. 우선 순위가 낮은 글로벌 큐에 매핑
    - Background: 사용자가 직접 알지 못하는 작업을 나타냄. 유저 관리 및 사용자 상호 작용이 필요하지 않고 시간에 민감하지 않은 기타 작업에 사용.

작업을 main 스레드 혹은 global 스레드에서 할 지와 동기, 비동기를 지정하여 `DispatchQueue`에 보낸다. 이렇게 보내진 작업은 시스템에 의해 각 스레드로 보내져서 작업이 이루어진다.

### 필요성

기존에 스레드를 사용하려면 개발자가 직접 스레드를 생성하고 관리해야 했다. GCD를 사용하면 스레드 생성, 유지, 삭제 등을 개발자가 신경쓸 필요 없이 해야할 작업(코드)를 큐에 예약하기만 하면 된다.

### 참고 자료

[https://developer.apple.com/documentation/dispatch](https://developer.apple.com/documentation/dispatch)

[https://developer.apple.com/documentation/dispatch/dispatchqueue](https://developer.apple.com/documentation/dispatch/dispatchqueue)

[https://www.raywenderlich.com/5370-grand-central-dispatch-tutorial-for-swift-4-part-1-2](https://www.raywenderlich.com/5370-grand-central-dispatch-tutorial-for-swift-4-part-1-2)

[https://ginjo.tistory.com/16](https://ginjo.tistory.com/16)