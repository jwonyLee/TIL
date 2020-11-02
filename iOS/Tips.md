# iOS Tips
- `Delegate` 채택 작업은 `extension`으로 빼는 게 좋다.
- `Colors.Assets`을 만들고, 그 안에 사용자 지정 컬러를 저장해 놓으면 `UIColor.init(named: String)`을 이용해서 호출할 수 있다.

## Remove line for between cell in TableView

If you want remove line for between cell in `TableView` using code, you can write `tableView.separatorStyle = .none`.
It's important to note that, It cannot be done when initializing the TableView.

### 🚫 Bad
```swift
let tableView = UITableView().then {
    $0.separatorStyle = .none
}
```

### 👍 Correct
```swift
let tableView = UITableView().then {
    // set tableView
}

override func viewDidLoad() {
    super.viewDidLoad()
        
    tableView.separatorStyle = .none
}
```