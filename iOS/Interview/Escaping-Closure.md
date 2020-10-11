# 탈출 클로저에 대하여 설명하시오.
## 클로저

일정 기능을 하는 코드를 하나의 블록으로 모아놓은 것

- 변수나 상수가 선언된 위치에서 참조(Reference)를 획득(Capture)하고 저장할 수 있음
- 클로저의 세 가지 형태
    - 이름이 있으면서 어떤 값도 획득하지 않는 전역함수의 형태
    - 이름이 있으면서 다른 함수 내부의 값을 획득할 수 있는 중첩된 함수의 형태
    - 이름이 없고 주변 문맥에 따라 값을 획득할 수 있는 축약 문법으로 작성한 형태

```swift
{ (Parameter) -> ReturnType in
    // code
}
```

## 탈출 클로저

함수의 전달인자로 전달한 클로저가 함수 종료 후에 호출될 때 클로저가 함수를 탈출(Escape)한다고 표현함

클로저를 매개변수로 갖는 함수를 선언할 때 매개변수 이름의 콜론(:) 뒤에 `@escaping` 키워드를 사용하여 클로저가 탈출하는 것을 허용한다고 명시해줄 수 있음

비동기 작업을 하는 함수들은 completion handler를 클로저 형태로 받는 경우가 많다. 이 때 받은 클로저는 함수의 작업이 완료될 때까지 호출되지 않는다. 실행 순서를 보장하고 싶을 때? 사용한다.

### 참고 자료

스위프트 프로그래밍 3판, 야곰 지음

[탈출 클로저 (@escaping closure)](https://jinios.github.io/swift/2018/06/13/escaping/)

### 스터디

```swift
func callBack(fn: () -> void) {
    let f = fn
    fn()
}
```
- 매개변수로 받은 클로저를 내부 변수에 저장할 수 없음
    - non escaping parameter may only be called
```swift
func callBack(fn: @escaping () -> void) {
    let f = fn
    f()
}
```
- 클로저의 기본값이 non-excaping인 이유
    → 컴파일러가 코드를 최적화하는 과정에서 성능 향상
- 탈출
    - 클로저가 안에 있다가 바깥에서 벗어나서 실행하게되는걸.. 탈출이라고 한다
```swift
class Server { 
    static var persons: [Person] = [] 
    
    static getPerson(completion: @escaping (Bool, [Person]) -> Void) {
    // 순서 2. 
        Alamofire.request(urlRequest).responseJSON { 
            response in persons.append(데이터) DispatchQueue.main.async { 
                // 순서 3. 
                completion(true, persons) 
            }
        } 
    }
}
// Usage, ex) ViewController.swift
// 순서 1.
Server.getPerson { (isSuccess, persons) in 
    // 순서 4. 
    if isSuccess { 
        // update UI
    }
}
```
- 탈출 클로저임을 명시한 경우, 클로저 내부에서 해당 타입의 프로퍼티나 메서드, 서브스크립트 등에 접근하기 위해서는 반드시 `self` 키워드를 사용해야 한다.
- 비탈출의 경우 반드시 명시해줄 필요는 없다. (선택적)
- 스위프트 프로그래밍 3판 267p, withoutActuallyEscaping 읽기
- 값 타입의 경우, 탈출 클로저는 mutable reference를 캡쳐링 할 수 없기 때문에 에러가 발생함
