# Autorelease Pool을 사용해야 하는 상황을 두 가지 이상 예로 들어 설명하시오.

- command-line 도구와 같이 UI 프레임워크를 기반으로 하지 않는 프로그램을 작성하는 경우
- 많은 임시 객체를 생성하는 루프를 작성하는 경우
루프 내에서 autorelease pool을 사용하여 다음 반복 전에 해당 객체를 삭제할 수 있다. 루프에서 autorelease pool 블록을 사용하면 애플리케이션의 최대 메모리 공간을 줄이는 데 도움이 된다.

    ```objectivec
    NSArray *urls = <# An array of file URLs #>;
    for (NSURL *url in urls) {
     
        @autoreleasepool {
            NSError *error;
            NSString *fileContents = [NSString stringWithContentsOfURL:url
                                             encoding:NSUTF8StringEncoding error:&error];
            /* 문자열을 처리하여, 더 많은 객체를 만들고 autorelease 한다. */
        }
    }
    ```

- 보조 스레드를 생성하는 경우
스레드가 실행되자마자 고유한 autorelease pool을 만들어야 한다. 그렇지 않으면 응용 프로그램에서 객체가 누출된다.