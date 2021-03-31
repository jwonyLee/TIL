# URLRequest

> A URL load request that is independent of protocol or URL scheme.

프로토콜 또는 URL scheme와 독립적인 URL load request이다.

## Overview

`URLRequest`는 load request의 두 가지 필수 속성을 캡슐화한다:
- 로드할 URL 및 로드하는 데 사용되는 정책
- HTTP와 HTTPS 요청의 경우 `URLRequest`에는 HTTP 메서드 (GET, POST 등) 및 HTTP 헤더 포함

## Using

매개변수로 세 가지 값이 들어가는데, 이 중 `url`을 제외한 두 가지 매개 변수는 기본값이 지정되어 있어서 직접 명시하지 않아도 된다.
- `url`  
    리퀘스트를 요청할 URL
- `cachePolicy: URLRequest.CachePolicy = .useProtocolCachePolicy`  
    리퀘스트에 대한 캐시 정책
- `timeoutInterval: TimeInterval = 60.0`  
    리퀘스트에 대한 제한 시간 간격

```swift
var webView: WKWebView!

// webView 초기화 코드 생략

override func viewDidLoad() {
    super.viewDidLoad()

    let url = URL(string: "https://google.com")!
    webView.load(URLRequest(url: url))
}
```


## 참고 자료

- [URLRequest | Apple Developer Documentation](https://developer.apple.com/documentation/foundation/urlrequest)