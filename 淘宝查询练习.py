# -*- coding:utf-8 -*-
from pymysql import connect


class TB:
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, database="tao_bao", user='root', password="71209269")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        """执行sql语句"""
        self.cursor.execute(sql)
        find_content = self.cursor.fetchall()
        for temp in find_content:
            print(temp)

    def select_all(self):
        # 查询全部
        sql = "select * from goods"
        self.execute_sql(sql)

    def select_name(self):
        # 查询商品名称
        sql = "select name,price from goods"
        self.execute_sql(sql)

    def select_cates(self):
        # 查询种类
        sql = "select name from goods_cates"
        self.execute_sql(sql)

    def data_menu(self):
        while True:
            print("-------淘宝搜索---------")
            print("1 查询所有商品 2 查询商品分类 3 查询种类 4 购买物品 0 退出")
            num = input("请输入要查询的功能：")
            if num == "1":
                self.select_all()
            elif num == "2":
                self.select_name()
            elif num == "3":
                self.select_cates()
            elif num == "4":
                self.place_an_order()
            elif num == "0":
                break
            else:
                print("输入错误请重新输入")

    def sign_in(self):
        """注册界面"""
        print("————————注册界面————————")
        try:
            customer_user = input("请输入账户：")
            password = int(input("请输入密码："))
            address = input("请输入地址：")
            telephone = int(input("请输入电话："))
        except Exception as rat:
            return print("输入错误请重新输入")
        # 将输入信息插入至customers表格
        sql = "insert into customers values('%d','%s','%s','%d','%d')" % (0, customer_user, address, telephone, password)
        self.cursor.execute(sql)
        self.conn.commit()
        print("注册成功")

    def log_in(self):
        """登录界面"""
        print("————————登录界面————————")
        try:
            customer_name = input("请输入用户名")
            customer_password = int(input("请输入密码"))
        except Exception as rat:
            return print("输入有误，请重新输入")
        sql = "select name,password,id from customers where name=('%s')" % (customer_name)
        self.cursor.execute(sql)
        find_content = self.cursor.fetchone()
        print(find_content)
        self.customer_id = int(find_content[2])
        user = str(find_content[0])
        password = int(find_content[1])
        while True:
                if customer_name == user:
                    if customer_password == password:
                        # 运行查询程序
                        self.data_menu()
                    else:
                        print("用户名或者密码错误请重新输入")
                        break

    def place_an_order(self):  # ,customer_order_content, customer_order_quantity, order_id
        """下订单程序"""
        print("————————下订单界面————————")
        try:
            self.customer_order_content = input("请输入要购买的物品的名称：")
            self.customer_order_quantity = int(input("请输入要购买的个数："))
        except Exception as rat:
            return print("没有这个商品，请重新输入")
        sql = "select id,name from goods where name=('%s')" % (self.customer_order_content)
        self.cursor.execute(sql)
        order_name = self.cursor.fetchone()
        self.order_id = order_name[0]
        print("下单成功")
        self.order_add()


    def order_details(self):
        """订单详情表"""
        print("————————订单详情————————")
        id_order = self.customer_id
        sql_order = "select id,customer_id from orders where id=('%d')" % id_order
        self.cursor.execute(sql_order)
        order_add_content = self.cursor.fetchone()
        self.order_add_id = int(order_add_content[0])
        id_order_add = self.order_add_id
        print(id_order_add)
        order_quantity = self.customer_order_quantity
        id_order = self.order_id
        sql = "insert into order_detail values('%d','%d','%d','%d')" % (0, id_order_add, id_order, order_quantity)
        self.cursor.execute(sql)
        self.conn.commit()

    def order_add(self):
        """订单表"""
        print("————————订单表————————")
        id_order = self.customer_id
        sql = "insert into orders(id,customer_id) values('%d','%d')" % (0, id_order)
        self.cursor.execute(sql)
        self.conn.commit()
        self.order_details()

    def run(self):
        """运行程序"""
        print("————————欢迎光临————————")
        while True:
            print("【1】 登录 【2】 注册")
            nums = input("请输入要选择的方式：")
            if nums == "1":
                self.log_in()
            elif nums == "2":
                self.sign_in()
            else:
                print("输入错误请重新输入")


def main():
    # 创建一个淘宝类
    tb = TB()
    # 运行
    tb.run()


if __name__ =="__main__":
    main()
