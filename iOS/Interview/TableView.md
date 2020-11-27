# TableView를 동작 방식과 화면에 Cell을 출력하기 위해 최소한 구현해야 하는 DataSource 메서드를 설명하시오.

## 동작 방식

TableView가 화면에 나타나기 전에 데이터 소스 객체에게 테이블의 보이는 부분이나 그 근처에 있는 행에 대한 셀을 제공하도록 요청한다. `tableView(_:cellForRowAt:)` 는 다음과 같은 패턴으로 구현된다.

1. 테이블 뷰의 `dequeueReusableCell(withIdentifier:for:)` 메서드를 호출해서 셀 객체를 검색한다.
2. 사용자 지정 데이터로 셀을 구성한다.
3. 셀을 테이블뷰로 반환한다.

테이블 뷰는 테이블의 각 행에 대해 셀을 만들지 않는다. 대신 테이블뷰는 셀을 느리게 관리하여 테이블의 보이는 부분에 있거나 근처에 있는 셀만 요청한다. 셀을 느리게 생성하면 테이블에서 사용하는 메모리 양이 줄어든다. 

## 최소한 구현해야 하는 DataSource 메서드

### 행, 섹션의 개수를 제공하는 메서드

행의 개수는 필수적으로 구현해야 함

```swift
func numberOfSections(in tableView: UITableView) -> Int  // Optional 
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int
```

### 셀 모양을 정의하는 메서드

```swift
func tableView(_ tableView: UITableView, 
             cellForRowAt indexPath: IndexPath) -> UITableViewCell
```

### 참고 자료

[Apple Developer Documentation](https://developer.apple.com/documentation/uikit/views_and_controls/table_views/filling_a_table_with_data)