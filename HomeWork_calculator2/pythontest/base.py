from HomeWork_calculator1.pythoncode.calculator import Calculator


class Base():
    def setup_class(self):
        print('class级别setup:开始测试')

    def setup(self):
        print("方法级别setup:开始计算")

    def teardown(self):
        print("方法级别teardown:结束计算")

    def teardown_class(self):
        print('class级别teardown:结束测试')