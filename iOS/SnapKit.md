# How to impose navigationController constraints created on the storyboard

1. Created a `Navigation Controller` on the Storyboard.
2. Other `view` are created using code.

If you want something view component to be positioned 8 apart from the top of navigation controller, just do something like this. (used `SnapKit`)
```swift
view.snp.makeConstraint {
    $0.top.equalTo(self.view.safeAreaLayoutGuide.snp.top).offset(8)
}
```