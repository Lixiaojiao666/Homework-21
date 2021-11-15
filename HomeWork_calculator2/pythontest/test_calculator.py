import allure
import pytest
import yaml
from HomeWork_calculator1.pythoncode.calculator import Calculator
from HomeWork_calculator1.pythontest.base import Base

#定义一个函数，从yaml文件中获取测试数据
def get_data_from_yaml(name,level='P0'):#需要输入两个参数：加法/除法，级别P0/P1/P2等
    # 使用with 读取yaml 文件,完成后会自动关闭连接
    with open("datas/data.yml", encoding='utf-8') as f:
        #安全下载数据文件，放到data里
        data = yaml.safe_load(f)
        #从加载的yaml数据中根据传入的参数拿取对应的datas
        datas = data[name][level]['datas']
        # 从加载的yaml数据中根据传入的参数拿取对应的ids
        ids = data[name][level]['ids']
        #将拿到的datas和ids作为返回值
        return(datas,ids)

@pytest.fixture(autouse=True)#环境准备函数，自动执行
def get_instance():
   print('这是yield之前的语句：在执行测试用例之前，会执行yield前面的这一部分')
   #实例化Calculator()类
   calc = Calculator()
   #执行到yield,yield相当于return，会把你后面的一些值返回回来，然后yield之后的操作步骤，就会在teardown里面执行
   yield calc
   print('这是yield之后的语句：yield激活teardown的操作，所以这部分在teardown里执行')

#定义一个函数，获取测试数据（需要用函数get_data_from_yaml的返回值），
#该函数用 fixture 实现参数化,@pytest.fixture(params=返回值的第一个值，ids=返回值的第二个值)
#加法：P0
@pytest.fixture(params=get_data_from_yaml('add','P0')[0],ids=get_data_from_yaml('add','P0')[1])
def get_datas_with_feature_add_p0(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    #返回get_data_from_yaml('add','P0')[0]即datas测试数据
    return request.param

#加法：P1_1
@pytest.fixture(params=get_data_from_yaml('add','P1_1')[0],ids=get_data_from_yaml('add','P1_1')[1])
def get_datas_with_feature_add_p11(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#加法：P1_2
@pytest.fixture(params=get_data_from_yaml('add','P1_2')[0],ids=get_data_from_yaml('add','P1_2')[1])
def get_datas_with_feature_add_p12(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#加法：P2
@pytest.fixture(params=get_data_from_yaml('add','P2')[0],ids=get_data_from_yaml('add','P2')[1])
def get_datas_with_feature_add_p2(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#除法：P1
@pytest.fixture(params=get_data_from_yaml('div','P0')[0],ids=get_data_from_yaml('div','P0')[1])
def get_datas_with_feature_div_p0(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#除法：P1_1
@pytest.fixture(params=get_data_from_yaml('div','P1_1')[0],ids=get_data_from_yaml('div','P1_1')[1])
def get_datas_with_feature_div_p11(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#除法：P1_2
@pytest.fixture(params=get_data_from_yaml('div','P1_2')[0],ids=get_data_from_yaml('div','P1_2')[1])
def get_datas_with_feature_div_p12(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#除法：P1_3
@pytest.fixture(params=get_data_from_yaml('div','P1_3')[0],ids=get_data_from_yaml('div','P1_3')[1])
def get_datas_with_feature_div_p13(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param

#除法：P2
@pytest.fixture(params=get_data_from_yaml('div','P2')[0],ids=get_data_from_yaml('div','P2')[1])
def get_datas_with_feature_div_p2(request):#这个函数被加了装饰器，可以直接使用函数名来调用它
    return request.param



@allure.feature('Calculator')
class TestCalculator():

    # 测试用例：加法，P0
    #标记这个方法以后可以用标签来对测试用例进行分类，并分类执行
    @pytest.mark.run(order=6)
    @pytest.mark.ADD_P0
    @allure.story('相加-P0') #allure小标题
    #定义方法：测试加法，P0级别数据。
    def test_add_p0(self, get_instance,get_datas_with_feature_add_p0):
        f = get_datas_with_feature_add_p0
        print(f[0],f[1],f[2])
        #allure报告中添加图片
        allure.attach.file("C:/Users/Administrator/PycharmProjects/HomeWork/HomeWork_calculator2/测试用例执行顺序，除法先执行，加法后执行.png",
                           name="测试用例执行顺序，除法先执行，加法后执行.png",
                           attachment_type=allure.attachment_type.PNG,
                           extension=".png")
        #allure报告中添加日志
        allure.attach("这里可以是日志",attachment_type=allure.attachment_type.TEXT)
        assert f[2] == round(get_instance.add(f[0], f[1]),3)

    # 测试用例：加法，P1_1
    @pytest.mark.run(order=7)
    @pytest.mark.ADD_P1
    @allure.story('相加-P1_1')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", add_P11_datas, ids=add_P11_ids)
    def test_add_p11(self, get_instance,get_datas_with_feature_add_p11):
        f = get_datas_with_feature_add_p11
        print(f[0],f[1],f[2])
        assert f[2] == round(get_instance.add(f[0], f[1]),3)

    # 测试用例：加法，P1_2
    @pytest.mark.run(order=8)
    @pytest.mark.ADD_P1
    @allure.story('相加-P1_2')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", add_P12_datas, ids=add_P12_ids)
    def test_add_p12(self,get_instance,get_datas_with_feature_add_p12):
        f = get_datas_with_feature_add_p12
        with pytest.raises(eval(f[2])) as e:
            result = get_instance.add(f[0],f[1])
        # 期望的异常与实际异常比对
        assert f[2] == e.typename
        print(f'预期捕获的异常：{f[2]}')
        print(f'实际捕获的异常：{e.typename}' )

    # 测试用例：加法，P2
    @pytest.mark.run(order=9)
    @pytest.mark.ADD_P2
    @allure.story('相加-P2')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", add_P2_datas, ids=add_P2_ids)
    def test_add_p2(self,get_instance,get_datas_with_feature_add_p2):
        f = get_datas_with_feature_add_p2
        with pytest.raises(eval(f[2])) as e:
            result = get_instance.add(f[0],f[1])
        # 期望的异常与实际异常比对
        assert f[2] == e.typename
        print(f'预期捕获的异常：{f[2]}')
        print(f'实际捕获的异常：{e.typename}')

    # 测试用例：除法，P0
    @pytest.mark.run(order=1)
    @pytest.mark.DIV_P0
    @allure.story('除法-P0')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", div_P0_datas, ids=div_P0_ids)
    def test_div_p0(self, get_instance,get_datas_with_feature_div_p0):
        f = get_datas_with_feature_div_p0
        assert f[2] == get_instance.div(f[0],f[1])


    # 测试用例：除法，P1_1
    @pytest.mark.run(order=2)
    @pytest.mark.DIV_P1
    @allure.story('除法-P1_1')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", div_P11_datas, ids=div_P11_ids)
    def test_div_p11(self, get_instance,get_datas_with_feature_div_p11):
        f = get_datas_with_feature_div_p11
        assert round(f[2]) == round(get_instance.div(f[0],f[1]),2)


    # 测试用例：除法，P1_2
    @pytest.mark.run(order=3)
    @pytest.mark.DIV_P1
    @allure.story('除法-P1_2')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", div_P12_datas, ids=div_P12_ids)
    def test_div_p12(self, get_instance,get_datas_with_feature_div_p12):
        f = get_datas_with_feature_div_p12
        with pytest.raises(ZeroDivisionError) as e:
        # 期望的异常与实际异常比对
            assert f[2] == get_instance.div(f[0],f[1])
        print(f'预期捕获的异常：{f[2]}')
        print(f'实际捕获的异常：{e.typename}')


    # 测试用例：除法，P1_3
    @pytest.mark.run(order=4)
    @pytest.mark.DIV_P1
    @allure.story('除法-P1_3')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", div_P13_datas, ids=div_P13_ids)
    def test_div_p13(self, get_instance,get_datas_with_feature_div_p13):
        f = get_datas_with_feature_div_p13
        with pytest.raises(eval(f[2])) as e:
            result = get_instance.div(f[0],f[1])
        # 期望的异常与实际异常比对
        assert f[2] == e.typename
        print(f'预期捕获的异常：{f[2]}')
        print(f'实际捕获的异常：{e.typename}')


    # 测试用例：除法，P2
    @pytest.mark.run(order=5)
    @pytest.mark.DIV_P2
    @allure.story('除法-P2')  # allure小标题
    #@pytest.mark.parametrize("a,b,expect", div_P2_datas, ids=div_P2_ids)
    def test_div_p2(self, get_instance,get_datas_with_feature_div_p2):
        f = get_datas_with_feature_div_p2
        with pytest.raises(eval(f[2])) as e:
            result = get_instance.div(f[0],f[1])
        # 期望的异常与实际异常比对
        assert f[2] == e.typename
        print(f'预期捕获的异常：{f[2]}')
        print(f'实际捕获的异常：{e.typename}')




