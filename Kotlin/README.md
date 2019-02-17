
# 목차

1.  [OpenJDK Install](#openjdk-install)
2.  [Kotlin Compiler Install](#kotlin-compiler-install)
3.  [Kotlin Compile & Execute](#kotlin-compile---execute)
4.  [Hello World 출력](#hello-world-출력)

  

## OpenJDK Install

```shell
$ sudo apt-get install openjdk-8-jre
```

  

```shell
$ java -version

openjdk version "1.8.0_191"

OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-2ubuntu0.18.04.1-b12)

OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

  

## Kotlin Compiler Install

```shell
$ sudo apt-get install unzip -y
```

```shell
$ sudo apt-get install zip -y
```

```shell
$ curl -s https://get.sdkman.io | bash
```

```shell
$ sdk install kotlin
```
```shell
$ kotlin -version

Kotlin version 1.3.21-release-158 (JRE 1.8.0_191-8u191-b12-2ubuntu0.18.04.1-b12)
```

  

## Kotlin Compile &amp; Execute

코틀린 코드 컴파일

```shell
$ kotlinc <소스파일 또는 디렉터리> -include-runtime -d <jar 이름.jar>
```

jar 파일 실행

```shell
$ java -jar <jar 이름>
```

  

## Hello World 출력

```kotlin
fun main(args: Array<String>) {
    println("Hello World!")
}
```

  

-  `fun` 함수 선언 키워드
- 함수를 최상위 수준에 정의할 수 있음. 클래스 안에 함수를 넣어야 할 필요가 없음.
-  `args` 변수명
-  `: Array<String>` 변수 혹은 파라미터 타입 지정(변수 혹은 파라미터 뒤에 작성)
- 배열 처리를 위한 문법이 따로 존재하지 않음
-  `println` 코틀린 표준 라이브러리는 여러 가지 표준 자바 라이브러리 함수를 간결하게 사용할 수 있게 감싼 래퍼wrapper를 제공.
- 세미콜론을 붙이지 않아도 됨

  

## Kotlin의 특징

- 정적 타입 지정 언어

    - 컴파일 시점에 모든 식의 타입을 지정해야 함
- 타입 추론 `type interence` (식이 본문인 함수의 경우)
    - 컴파일러가 타입을 분석해 프로그래머 대신 프로그램 구성 요소의 타입을 정해주는 기능
- 타입 지정 생략 가능
    - 컴파일러가 초기화 식(변수에 저장될 값)을 분석해서 변수 타입을 지정.
    - 초기화 식이 없다면 컴파일러가 타입 추론 불가능. 이런 경우에는 타입을 반드시 지정해야 함.

  

## 변수 `Variable`

### `val`
- 변경 불가능한 참조를 저장하는 변수
- 자바의 경우 `final` 변수에 해당
- 블록을 실행할 때 정확히 한 번만 초기화되야 함
- 참조 자체는 불변일지라도 그 참조가 가리키는 객체의 내부 값은 변경될 수 있음

### `var`

- 변경 가능한 참조를 저장하는 변수
- 자바의 일반 변수에 해당
- 변수의 값을 변경할 수 있지만 변수의 타입은 고정됨

> - 기본적으로 모든 변수를 `val` 키워드를 사용해 불변 변수로 선언하여 사용. 꼭 필요한 때에만 var로 변경  
> - 변경 불가능한 참조와 변경 불가능한 객체를 부수 효과가 없는 함수와 조합해 사용하면 코드가 함수형 코드에 가까워진다.