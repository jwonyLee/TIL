# Remove line for between cell in TableView

If you want remove line for between cell in `TableView` using code, you can write `tableView.separatorStyle = .none`.
It's important to note that, It cannot be done when initializing the TableView.

## 🚫 Bad
```swift
let tableView = UITableView().then {
    $0.separatorStyle = .none
}
```

## 👍 Correct
```swift
let tableView = UITableView().then {
    // set tableView
}

override func viewDidLoad() {
    super.viewDidLoad()
        
    tableView.separatorStyle = .none
}
```