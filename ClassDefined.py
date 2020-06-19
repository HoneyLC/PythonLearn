## 定义类
class classdefined:
    """方法1"""

    def method1(self):
        pass

    def method2(self):
        pass


"""创建对象"""
classdemo = classdefined();


class cat:
    def __init__(self, new_name):
        self.__name = new_name
        print("初始化方法")

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


tom = cat("JACK");
tom.name = "jary"
tom.drink()
tom.eat()
print(tom._cat__name)


# 私有变量或者私有方法,前面加上__,例子:self.__name
# 强制访问私有变量 (不推荐使用)   对象名._类名_变量名

# 继承: class 子类(父类):
# 方法重写,直接重新写 就好了
# super().方法() 调用父类的方法

# 多继承  class 子类 (父类1,父类2)
# 注意: 当有重复的父类方法,调用第一个父类的方法
# python的MRO(方法搜索顺序)

# 多态:
# 实例方法: 方法内部需要访问实例属性,
# 类方法:  类方法内部可以直接访问类属性和类方法
# 静态方法: 不需要访问类属性和类方法
class ClassMethod():
    count = 1;

    @classmethod
    def show_count(cls):
        print(cls.count)

    def __init__(self):
        print("初始化方法")
        ClassMethod.count += 1;


class1 = ClassMethod();
class2 = ClassMethod();
ClassMethod.show_count()

print("_" * 20)

"""
单例
"""


class singleDemo(object):
    instance = None;
    init_flag = False;

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls);
        print("分配空间")
        return cls.instance

    def __init__(self):
        if singleDemo.init_flag:
            return

        print("初始化")
        singleDemo.init_flag = True

    @classmethod
    def method(self):
        print("方法调用")
        print(self)


s = singleDemo()
print(s)
s.method()

"""
异常处理:
    异常的传递:异常出现.会把异常传递给调用方,若果没有处理异常,程序会停止
"""


class exception():
    @classmethod
    def ex(self):
        try:
            print(1 / 1);
        except Exception as result:
            print(result)
        except ZeroDivisionError:
            print("非零异常")
        except ValueError:
            print("数值错误")
        else:
            print("没有异常,执行的代码")
        finally:
            print("无论是否出现异常,执行的代码")


exception.ex()


class defindException():
    @staticmethod
    def input_pssword():
        pwd = "10";
        if len(pwd) <= 8:
            exception = Exception("密码长度不够")
            raise exception;
        return pwd;


try:
    print(defindException.input_pssword());
except Exception as result:
    print(result)


# 编写测试代码
def main():
    print("测试代码")


if __name__ == "__main__":
    main()

# 包(package):  每个包下有一个__init__.py文件,  包名的命名格式: 小写字母+_报名
# __init__.py 导入每个模块
"""发布模块"""
"""
1)创建setup.py的文件:
    from distutils.core import setup
    setup(
        name="包名",
        version="版本号",
        description="描述信息",
        long_description="完整描述信息",
        author="作者",
        author_email = "邮箱",
        url="主页",
        py_module=[各个模块名]
        )
2)构建模块: python3 setup.py build
3)生成发布的压缩包: python3 setup.py sdist
"""

"""
文件处理:
"""

print("-" * 20)
file = open("README", encoding='utf8')  # 参数:r(只读) w(只写,文件存在覆盖,不存在创建) a(追加) "参数"+(读写)
# 写
# write = file.write("world")
# 读
# read = file.read()
while True:
    readline = file.readline()
    if not readline:
        break;
    print(readline)

# print(read)
# 关闭
file.close();

"""
    eval函数:  把字符串当成python代码执行
    注意: 不要直接转换input的结果
    __import__('os').system('ll')
    __import__('os').system('rm delete')
"""
input = input("请输入命令:")
eval = eval(input)
print(eval)