import allure
import pytest
import yaml
from HomeWork_calculator1.pythoncode.calculator import Calculator
from HomeWork_calculator1.pythontest.base import Base


def get_data(level):
    # 使用with 读取yaml 文件,完成后会自动关闭连接
    with open("datas/data.yml", encoding='utf-8') as f:
        #安全下载数据文件，放到datas里
        datas = yaml.safe_load(f)
        #get()方法获取值，参数为add，获取add下的值
        add_datas = datas.get("add")
        # get()方法获取值，参数为div，获取div下的值
        div_datas = datas.get("div")
        print(div_datas)

        #返回值：接受传入的参数level,并获取该参数对应的datas,ids作为返回值
        #return (add_datas.get(level).get("datas"),add_datas.get(level).get("ids"),div_datas.get(level).get("datas"),div_datas.get(level).get("datas"))
        return (add_datas.get(level),div_datas.get(level))

class TestCalculator(Base):
    #获取加法测试数据，赋值给变量
    add_P0_datas = get_data("P0")[0].get("datas")
    add_P0_ids = get_data("P0")[0].get("ids")
    add_P11_datas= get_data("P1_1")[0].get("datas")
    add_P11_ids = get_data("P1_1")[0].get("ids")
    add_P12_datas = get_data("P1_2")[0].get("datas")
    add_P12_ids = get_data("P1_2")[0].get("ids")
    add_P2_datas = get_data("P2")[0].get("datas")
    add_P2_ids = get_data("P2")[0].get("ids")

    #获取乘法测试数据，赋值给变量
    div_P0_datas = get_data("P0")[1].get("datas")
    div_P0_ids = get_data("P0")[1].get("ids")
    div_P11_datas = get_data("P1_1")[1].get("datas")
    div_P11_ids = get_data("P1_1")[1].get("ids")
    div_P12_datas = get_data("P1_2")[1].get("datas")
    div_P12_ids = get_data("P1_2")[1].get("ids")
    div_P13_datas = get_data("P1_3")[1].get("datas")
    div_P13_ids = get_data("P1_3")[1].get("ids")
    div_P2_datas = get_data("P2")[1].get("datas")
    div_P2_ids = get_data("P2")[1].get("ids")

    #实例化Calculator对象
    calc = Calculator()

    #标记这个方法以后可以用标签来对测试用例进行分类，并分类执行
    @pytest.mark.ADD_P0
    #参数化测试数据，@pytest.mark.parametrize("参数名",列表数据)
    #‘a,b,expect’是参数名（这里有三个参数名）， add_P0_datas, ids=add_P0_ids是参数对应的数据，
    # 其中参数a对应add_P0_datas，b对应ids=add_P0_ids
    @pytest.mark.parametrize("a,b,expect", add_P0_datas, ids=add_P0_ids)
    def test_case_add_p0(self, a, b, expect):
        print(a, b, expect)
        assert expect == self.calc.add(a, b)

    @pytest.mark.ADD_P1
    @pytest.mark.parametrize("a,b,expect", add_P11_datas, ids=add_P11_ids)
    def test_case_add_p11(self, a, b, expect):
        print(a, b, expect)
        assert expect == self.calc.add(a, b)

    @pytest.mark.ADD_P1
    @pytest.mark.parametrize("a,b,expect", add_P12_datas, ids=add_P12_ids)
    def test_case_add_p12(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename
        print(f'预期捕获的异常：{expect}')
        print(f'实际捕获的异常：{e.typename}' )

    @pytest.mark.ADD_P2
    @pytest.mark.parametrize("a,b,expect", add_P2_datas, ids=add_P2_ids)
    def test_case_add_p2(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename
        print(f'预期捕获的异常：{expect}')
        print(f'实际捕获的异常：{e.typename}')

    @pytest.mark.DIV_P0
    @pytest.mark.parametrize("a,b,expect", div_P0_datas, ids=div_P0_ids)
    def test_case_div_p0(self, a, b, expect):
        print(a, b, expect)
        assert expect == self.calc.div(a, b)

    @pytest.mark.DIV_P1
    @pytest.mark.parametrize("a,b,expect", div_P11_datas, ids=div_P11_ids)
    def test_case_div_p11(self, a, b, expect):
        print(a, b, expect)
        assert round(expect) == round(self.calc.div(a, b),2)

    @pytest.mark.DIV_P1
    @pytest.mark.parametrize("a,b,expect", div_P12_datas, ids=div_P12_ids)
    def test_case_div_p12(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.div(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename
        print(f'预期捕获的异常：{expect}')
        print(f'实际捕获的异常：{e.typename}')

    @pytest.mark.DIV_P1
    @pytest.mark.parametrize("a,b,expect", div_P13_datas, ids=div_P13_ids)
    def test_case_div_p13(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.div(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename
        print(f'预期捕获的异常：{expect}')
        print(f'实际捕获的异常：{e.typename}')

    @pytest.mark.DIV_P2
    @pytest.mark.parametrize("a,b,expect", div_P2_datas, ids=div_P2_ids)
    def test_case_div_p2(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.div(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename
        print(f'预期捕获的异常：{expect}')
        print(f'实际捕获的异常：{e.typename}')



