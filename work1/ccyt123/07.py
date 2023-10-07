class products:
    def __init__(self,ids,name,price,number,surplus):
        self.ids  = ids
        self.name = name
        self.price = price
        self.number = number
        self.surplus = surplus
    def display(self):
        print("商品序号：",self.ids)
        print("商品名：",self.name)
        print("单价：",self.price)
        print("总数量：",self.number)
        print("剩余数量：",self.surplus)
    def income(self):
        income = self.price*(self.number-self.surplus)
        print("已售出商品价值：",income)
    def setdata(self):
        self.ids = input("商品序号：")
        self.name = input("商品名：")
        self.price = input("单价：")
        self.number = input("总数量：")
        self.surplus = input("剩余数量：")
