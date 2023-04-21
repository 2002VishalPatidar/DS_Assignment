class Stack():
    def __init__(self):
        self.item=[]
        self.n=0
    def __len__(self):
        return self.n
    def isEmpty(self):
        return self.n==0
    def push(self,item):
        self.item.append(item)
        self.n+=1
    def pop(self):
        ele=self.item.pop()
        self.n-=1
        return ele
    def getPeek(self):
        if self.n>0:
            return self.item[-1]
        return "Stack is empty"
    def getStackitem(self):
        return [self.item[i] for i in range(self.n)]
def reversing(data):
    x=Stack()
    for i in data:
        x.push(i)
    y=Stack()
    while not x.isEmpty():
        y.push(x.pop())
    return "".join(y.getStackitem())

print(reversing("123456789"))