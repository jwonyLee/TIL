# 파이썬 알고리즘 인터뷰 7장 - 배열

문제가 전체적으로 어려워서 풀지 못했다. 일단 다음 8장으로 넘어가기 전에 배열과 관련된 문제들을 푸는 데 시간을 쏟아야겠다.

> 배열은 값 또는 변수 엘리먼트의 집합으로 구성된 구조로, 하나 이상의 인덱스 또는 키로 식별된다.

## 두 수의 합

브루트 포스 방식으로 풀었다. 비슷하게 풀어서 따로 적지는 않았음

### 풀이1. 브루트 포스로 계산
시간 복잡도 → O(n^2)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### 풀이2. in을 이용한 탐색
모든 조합을 비교하지 않고 타겟에서 첫 번째 값을 뺀 값 tartget - n 이 존재하는지 탐색하는 방식으로 풀 수 있음  
시간 복잡도 → O(n^2)이지만 같은 시간 복잡도라도 in 연산 쪽이 훨씬 더 가볍고 빠름
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)
```

### 풀이3. 첫 번째 수를 뺀 결과 키 조회
시간 복잡도 → O(n)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[tartget - num]
```

### 풀이4. 조회 구조 개선
전체를 모두 저장할 필요 없이 정답을 찾게 되면 함수를 바로 빠져나올 수 있음. 그러나 두 번째 값을 찾기 위해 어차피 매번 비교해야 하기 때문에 앞서 풀이에 비해 성능상의 큰 이점은 없을 거 같음  
시간 복잡도 → O(n)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i
```

### 풀이5. 투 포인터 이용
> 투 포인터란 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정하는 방식  

투 포인터를 이용해서 풀 수 없는 문제

### 풀이6. 고(Go) 구현

성능 개선의 효과가 크지만, 해당 언어를 사용할 줄 몰라서 적지 않았음

## 빗물 트래핑

빗물 트래핑과 비슷한 유형의 문제(쇠막대기)를 잘 못 푸는 편이라서... 일단 이번에도 풀이를 머리에 담아두는 걸로 넘어갔다. 

### 풀이1. 투 포인터를 최대로 이동
시간 복잡도 → O(n)
```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max),
                              max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
```

### 풀이2. 스택 쌓기
시간 복잡도 → O(n)
```python
def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼냄
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        stack.append(i)
    return volume
```

## 세 수의 합

이 문제는 봐도 음.. 잘 모르겠다. 다음에 한 번 더 보기

### 풀이1. 브루트 포스로 계산
시간 복잡도 → O(n^3)
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append((nums[i], nums[j], nums[k]))
    return results
```

### 풀이2. 투 포인터로 합 계산
시간 복잡도 → O(n^2)
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results
```

## 배열 파티션 I

### 내가 작성한 코드
```python
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    sum = 0
        
    for i in range(len(nums)):
        if i % 2 == 0:
            sum += nums[i]
    return sum
```

### 풀이1. 오름차순 풀이
```python
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum
```

### 풀이2. 짝수 번째 값 계산
```python
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum
```

### 풀이3. 파이썬다운 방식
```python
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
```

## 자신을 제외한 배열의 곱

### 내가 작성한 코드
이 코드는 시간 초과로 실패가 뜬다. 들어오는 값이
> [-1,-1,1,-1,-1,1,-1,-1,-1,1,1,-1,1,1,1,1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,1,-1,1,-1,-1,1,-1,-1,1...

이 정도로 길 때 실패했다. 😢
```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    output = []
    
    for i, n in enumerate(nums):
        output.append(reduce((lambda x, y: x * y), nums[:i] + nums[i+1:]))
    return output
```

### 풀이1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out
```

## 주식을 사고팔기 가장 좋은 시점

### 풀이1. 브루트 포스로 계산
시간 복잡도 → O(n^2)
```python
def maxProfit(self, prices: List[int]) -> int:
    max_price = 0
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices))):
            max_price = max(prices[j] - price, max_price)
    return max_price
```

### 풀이2. 저점과 현재 값과의 차이 계산
시간 복잡도 → O(n)
```python
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
```