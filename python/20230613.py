def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key_item = arr[i]
        j = i - 1
        while j >= start and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


def merge(arr, start, mid, end):
    if arr[mid - 1] < arr[mid]:
        return

    left = arr[start:mid]
    right = arr[mid:end]

    k = start
    i = 0
    j = 0

    while start + 1 < mid and mid + j < end:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if start + i < mid:
        arr[k:end] = left[i:]
    if mid + j < end:
        arr[k:end] = right[j:]


def timsort(arr):
    min_run = 2
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, mid, end)
        size *= 2

    return arr


a = ['f', 'g', 'h', 'z', 's', 'b', 'c', 'd']

print(timsort(a))

https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # solution 1 : 리스트로 변환
        # 전처리를 위해 입력 문자열에 영문, 숫자만을 추출 -> 모두 소문자로 변환
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop(0) 0번째 index pop
                return False
        return True

        # solution 2 : 데크를 이용한 최적화
        #
        strs = deque()  # 앞뒤로 추출 가능
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

        # solution 3 : 정규표현식, 슬라이싱 사용
        # 문자열을 모두 소문자로 변환 -> 정규식을 통한 알파벳과 숫자 이외의 문자를 제거
        # list[::-1] 기능을 통해 리스트를 뒤집고 문자열이 같은지 비교
        import re


s = s.lower()
s = re.sub('[^a-z0-9]', '', s)
return s == s[::-1]


