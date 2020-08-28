# 최대공약수(Greatest Common Divisor)
- 두 정수 n과 m의 최대공약수는 n과 m의 공약수 중에 가장 큰 정수다.

## 유클리드 호제법(Euclidean algorithm)
- a를 b로 나눈 나머지를 r이라고 했을 때
- a와 b의 최대 공약수를 `(a, b)`라고 하면
- `(a, b) = (b, r)`이 성립한다.
- r이 0이면 b는 최대 공약수가 된다.


### 재귀함수를 이용한 방법
```python
def gcd(m,n):
	if m < n:
		m, n = n, m
	if n == 0:
		return m
    if m % n == 0:
		return n
	else:
		return gcd(n, m%n)
```

### 재귀함수를 이용하지 않은 방법
```python
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)
```

### 참고하면 좋은 글
[최대공약수](https://ko.wikipedia.org/wiki/최대공약수)

[유클리드 호제법](https://ko.wikipedia.org/wiki/유클리드_호제법)