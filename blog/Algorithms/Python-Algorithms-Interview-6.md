# 파이썬 알고리즘 인터뷰 6장 - 문자열 조작

문자열을 다루는 유형의 문제를 더 풀어봐야겠다. 딱 문제만 봐서는 어떻게 해결해야할 지 감이 안 잡힌다. 😢


## [유효한 팰린드롬](https://leetcode.com/problems/valid-palindrome/)

### 내가 작성한 코드
```python
def isPalindrome(self, s: str) -> bool:
    filter_string = ""
    for a in s.lower():
        if a.isalnum():
            filter_string += a
    return filter_string == filter_string[::-1]
```

### 풀이1. 리스트로 변환
```python
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    # 팰린드롬 판별 여부
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True
```

### 풀이2. Deque 자료형을 이용한 최적화
```python
def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() !== strs.pop():
            return False
    
    return True
```

### 풀이3. 슬라이싱 사용
```python
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1] # 슬라이싱
```

## [문자열 뒤집기](https://leetcode.com/problems/reverse-string)

### 내가 작성한 코드
```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

### 풀이1. 투 포인터를 이용한 스왑
```python
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### 풀이2. 파이썬다운 방식
내가 작성한 코드와 동일

## [로그 파일 재정렬](https://leetcode.com/problems/reorder-data-in-log-files/)
```
💡 2개 이상의 조건으로 정렬할 때 람다를 사용해서 정렬하는 것을 알게되었다.
```
### 풀이1. 람다와 + 연산자를 이용
```python
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
```

## [가장 흔한 단어](https://leetcode.com/problems/most-common-word/)

```
💡 Counter 객체 사용 방법 숙지하기
```

### 내가 작성한 코드
```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = re.sub('[^\w]', ' ', paragraph.lower()).split()
    dic = dict()
    for word in words:
        if not word in banned:
            dic[word] = dic.get(word, 0) + 1
    return max(dic.keys(), key=lambda x: dic[x])
```

### 풀이1. 리스트 컴프리헨션, Counter 객체 사용
```python
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]
```

## [그룹 애너그램](https://leetcode.com/problems/group-anagrams/)

### 풀이1. 정렬하여 딕셔너리에 추가
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
```

## [가장 긴 팰린드롬 부분 문자열](https://leetcode.com/problems/longest-palindromic-substring/)

```
💡 투 포인터 개념 숙지하고 비슷한 유형의 문제 풀어보기
```

### 풀이1. 중앙을 중심으로 확장하는 풀이
```python
def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right -1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 orf s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, 
                        expand(i, i+1),
                        expand(i, i+2),
                        key=len)
    return result
```