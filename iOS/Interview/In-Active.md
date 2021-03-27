# 앱이 In-Active 상태가 되는 시나리오를 설명하시오.

## Foreground

In-Active와 Active를 합쳐서 Foreground 라고 함

## In-Active

App이 실행 중이지만 이벤트를 받지 않는 상태

*보통 이 상태에 잠시 머물렀다가 다른 상태로 변경됨

- 시나리오 1. 사용자가 앱을 실행합니다.
    - `Not Running` → `In-Active` → `Active`
- 시나리오 2. 앱 실행 도중 홈 버튼을 누릅니다.
    - `Active` → `In-Active` → `Background`
- 시나리오 3. 앱을 다시 켭니다.
    - `Background` → `Active`
- 시나리오 4. 앱이 백그라운드에 있다가 Suspended 상태로 전이됩니다.
    - `Active` → `In-Active` → `Background` → `Suspended`

### 참고 자료

[iOS Application state](https://caution-dev.github.io/ios/2019/03/14/iOS-Application-state.html)

### 생각해보기

iOS 14부터 일부 인터페이스가 컴팩트하게 변경되었다. 기존(iOS 14 이전)에는 전화가 오면 앱에 상태가 Active → In-Active → Background로 변경되었는데, 이렇게 UI가 변경된 상황(앱을 가리지 않음)에서는 앱이 In-Active를 진입할까?
