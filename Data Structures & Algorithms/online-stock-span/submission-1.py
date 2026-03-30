class StockSpanner:

    def __init__(self):
        self.arr = []
        

    def next(self, price: int) -> int:
        # self.arr.append(price)
        # res = 0
        # for i in range(len(self.arr)-1,-1,-1):
        #     if self.arr[i] <= price:
        #         res+=1
        #     else:
        #         break
        # return res
        res = 1
        while self.arr and self.arr[-1][0] <= price:
            val, span = self.arr.pop()
            res += span
        self.arr.append((price,res))
        return res




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)