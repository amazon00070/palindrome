class zhengshu:
    def __init__(self,x):
        self.x = x
    #取得实例的长度
    def lenth(self):
        l_i = -1
        l_x = self.x
        if l_x == 0:
            l_i = 0
        else:
            while l_x != 0:
                l_x = int(l_x / 10)
                l_i = l_i + 1
        self.wei = l_i
    #取得实例的第n位数字
    def post(self,n):
        return int(self.x / pow(10,n) % 10)
    #将实例展开存放于数组.expand_list
    def expand(self):
        self.expand_list = []
        l_x = self.x
        while l_x != 0:
            self.expand_list.append(l_x % 10)
            l_x = int(l_x / 10)
    #返回是否是回文数
    def palindrome(self):
        self.lenth()
        a.expand()
        yes_or_no = 1
        for i in range(0,int(self.wei / 2) + 1):
            if a.expand_list[i] != a.expand_list[self.wei - i]:
                yes_or_no = 0
        return yes_or_no
a = zhengshu(123321)
print(a.palindrome())
a = zhengshu(1234)
print(a.palindrome())
