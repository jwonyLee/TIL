# UIKit 클래스들을 다룰 때 꼭 처리해야하는 애플리케이션 쓰레드 이름은 무엇인가?

> **Important**  
> Use UIKit classes only from your app’s main thread or main dispatch queue, unless otherwise indicated. This restriction particularly applies to classes derived from UIResponder or that involve manipulating your app’s user interface in any way.

UIKit 클래스는 앱의 기본 스레드 혹은 `DispatchQueue.main`에서만 사용해야 한다. 이 제한은 `UIResponder`에서 파생되거나 앱의 사용자 인터페이스를 조작하는 것과 관련된 클래스에 적용된다.



## 참고 자료

- [Why must UIKit operations be performed on the main thread? - Stack Overflow](https://stackoverflow.com/questions/18467114/why-must-uikit-operations-be-performed-on-the-main-thread)
- [UIKit | Apple Developer Documentation](https://developer.apple.com/documentation/uikit)