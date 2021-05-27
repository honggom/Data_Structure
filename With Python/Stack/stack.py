class Stack():

    # 초기화
    def __init__(self):
        self.stack = []

    # 데이터 삽입
    def push(self, item):
        self.stack.append(item)

    # 맨 위 데이터 리턴 및 삭제
    def pop(self):
        if self.isEmpty():
            return 'empty..'
        return self.stack.pop()

    # 맨 위 데이터 리턴
    def peek(self):
        if self.isEmpty():
            return 'empty..'
        return self.stack[-1]

    # 스택이 비어있는지 확인
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False


s = Stack()

s.push(1)
s.push(3)
s.push(512)

print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.isEmpty())
print(s.peek())