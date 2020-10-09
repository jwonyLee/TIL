# 최대값

1. `sys` 모듈을 이용하는 방법
```python
import sys

max_size = sys.maxsize
```

2. `float()` 을 이용하는 방법
```python
max_size = float('inf')
```

# 인덱스와 값을 같이 사용하기

```python
numbers = [1, 5, 7, 9, 3, 2]

for index, value in enumerate(numbers):
    print(f'index: {index} value: {value}')
```

```python
index: 0 value: 1
index: 1 value: 5
index: 2 value: 7
index: 3 value: 9
index: 4 value: 3
index: 5 value: 2
```