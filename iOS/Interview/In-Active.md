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

[iOS Application state](https://caution-dev.github.io/ios/2019/03/14/iOS-Application-state.html)