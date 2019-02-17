# 목차
1. [OpenJDK Install](#openjdk-install)  
2. [Kotlin Compiler Install](#kotlin-compiler-install)  
3. [Kotlin Compile & Execute](#kotlin-compile-&-execute)  
4. [Hello World 출력](#hello-world-출력)

# OpenJDK Install
```shell
$ sudo apt-get install openjdk-8-jre
```

```shell
$ java -version
openjdk version "1.8.0_191"
OpenJDK Runtime Environment (build 1.8.0_191-8u191-b12-2ubuntu0.18.04.1-b12)
OpenJDK 64-Bit Server VM (build 25.191-b12, mixed mode)
```

# Kotlin Compiler Install
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

# Kotlin Compile & Execute
코틀린 코드 컴파일
```shell
$ kotlinc <소스파일 또는 디렉터리> -include-runtime -d <jar 이름.jar>
```
jar 파일 실행
```shell
$ java -jar <jar 이름>
```

# Hello World 출력
```kotlin
fun main(args: Array<String>) {
    println("Hello World!")
}
```

- `fun`  함수 선언 키워드  
- 함수를 최상위 수준에 정의할 수 있음. 클래스 안에 함수를 넣어야 할 필요가 없음.
- `args` 변수명  
- `: Array<String>` 변수 혹은 파라미터 타입 지정(변수 혹은 파라미터 뒤에 작성)
- 배열 처리를 위한 문법이 따로 존재하지 않음
- `println` 코틀린 표준 라이브러리는 여러 가지 표준 자바 라이브러리 함수를 간결하게 사용할 수 있게 감싼 래퍼wrapper를 제공.
- 세미콜론을 붙이지 않아도 됨