# class ListNode:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#
# class Stack:
#     def __init__(self):
#         self.head =None
#         self.size=0
#     def is_empty(self):
#         return self.size == 0
#     def push(self,value):
#         new_node=ListNode(value)
#         new_node.next=self.head
#         self.head =new_node
#         self.size+=1
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from an empty stack")
#         value = self.head.value
#         self.head=self.head.next
#         self.size-= 1
#         return value
# stack=Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
#
# for _ in range(5):
#     print(stack.pop())

#https://leetcode.com/problems/valid-parentheses/
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack=[]
#         mapping = {
#             ')':'(',
#             '}':'{',
#             ']':'['
#         }
#
#         for char in s:
#             # 스택 마지막 요소 꺼내서 확인, 비어있으면 #반환
#             if char in mapping:
#                 top_element =stack.pop() if stack else '#'
#                 if mapping[char] != top_element:
#                     return False
#             else :
#                 stack.append(char)
#         return not stack

#https://leetcode.com/problems/remove-duplicate-letters/
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         if not s:
#             return ""
#
#         for char in sorted(set(s)):
#             suffix = s[s.index(char)]
#             if set(s) == set(suffix):
#                 return char +self.removeDuplicateLetters(suffix.replace(char,""))
#         return ""

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         if not s:
#             return ""
#
#         # 문자열의 문자 빈도수 계산
#         counter = {char: 0 for char in set(s)}
#
#         for char in s:
#             counter[char] += 1
#
#         # 사전순으로 가장 작은 문자의 인덱스 찾기
#         min_idx = 0
#         for i, char in enumerate(s):
#             if char < s[min_idx]:
#                 min_idx = i
#             counter[char] -= 1
#             if counter[char] == 0:
#                 break
#         return s[min_idx] + self.removeDuplicateLetters(s[min_idx + 1:].replace(s[min_idx], ""))

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         last_occurrence = {c: i for i, c in enumerate(s)}
#         stack = []
#         in_stack = set()
#
#         for i, c in enumerate(s):
#             if c not in in_stack:
#                 while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
#                     in_stack.remove(stack.pop())
#                 stack.append(c)
#                 in_stack.add(c)
#
#         return ''.join(stack)

# https://leetcode.com/problems/daily-temperatures/
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
#
#         for i, cur in enumerate(temperatures):
#             while stack and cur > temperatures[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)
#
#         return answer
# https://leetcode.com/problems/implement-queue-using-stacks/
# class MyQueue:
#
#     def __init__(self):
#         self.input=[]
#         self.output=[]
#
#     def push(self, x: int) -> None:
#         self.input.append(x)
#
#     def pop(self) -> int:
#         self.peek()
#         return self.output.pop()
#     def peek(self) -> int:
#         if not self.output:
#             while self.input:
#                 self.output.append(self.input.pop())
#         return self.output[-1]
#
#     def empty(self) -> bool:
#         return self.input == [] and self.output==[]

# https://leetcode.com/problems/implement-stack-using-queues/
# class MyStack:
#
#     def __init__(self):
#         self.q=collections.deque()
#
#     def push(self, x: int) -> None:
#         self.q.append(x)
#         for _ in range(len(self.q)-1):
#             self.q.append(self.q.popleft())
#
#     def pop(self) -> int:
#         return self.q.popleft()
#
#     def top(self) -> int:
#         return self.q[0]
#
#     def empty(self) -> bool:
#         return len(self.q)==0
#
#
# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()

# https://leetcode.com/problems/design-circular-queue/
# class MyCircularQueue:
#
#     def __init__(self, k: int):
#         self.q= [None]*k
#         self.maxlen=k
#         self.p1=0
#         self.p2=0
#
#     def enQueue(self, value: int) -> bool:
#         if self.q[self.p2] is None:
#             self.q[self.p2]=value
#             self.p2=(self.p2 + 1)%self.maxlen
#             return True
#         else:
#             return False
#     def deQueue(self) -> bool:
#         if self.q[self.p1] is None:
#             return False
#         else:
#             self.q[self.p1]=None
#             self.p1=(self.p1+1)%self.maxlen
#             return True
#     def Front(self) -> int:
#         return -1 if self.q[self.p1] is None else self.q[self.p1]
#
#     def Rear(self) -> int:
#         return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
#
#     def isEmpty(self) -> bool:
#         return self.p1 == self.p2 and self.q[self.p1] is None
#
#     def isFull(self) -> bool:
#         return self.p1 == self.p2 and self.q[self.p1] is not None

import requests
import json

city = "Seoul"
apikey = "#################"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

print(type(result.text))
