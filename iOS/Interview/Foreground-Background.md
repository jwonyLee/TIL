# 앱이 foreground에 있을 때와 background에 있을 때 어떤 제약사항이 있나요?

## Background Mode

1. Not Running
2. Foreground (Inactive, Active)
3. Background
4. Suspend

## Foreground 제약사항

모르겠음

## Background 제약사항

- 사용자에 의한 이벤트를 받지 못함
- 시간 제약이 있음: 최소 10분?, 추가 실행 시간이 필요하면 `UIApplication.beginBackgroundTaskWithName:expirationHandler:` 혹은 `UIApplication.beginBackgroundTaskWithExpirationHandler:` 를 실행한다.

### 참고 자료

[Apple Developer Documentation](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background/about_the_background_execution_sequence)

[App Programming Guide for iOS - Background Execution (3)](https://wnstkdyu.github.io/2018/06/09/appprogrammingguidebackgroundexecution/)