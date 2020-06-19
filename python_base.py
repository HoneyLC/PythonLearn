# 注释
"""
多行注释
"""
# helloworld
import random

print("helloworld");

# 算数运算符 :   +加法   -减法   *乘(字符串也可以使用乘法)  /除  //取整  %取余  **幂运算
print("顶顶顶顶" * 10);

# 变量的定义
number1 = 10;
number = "10000";

"""
数据类型:
    1.数字型: int long(python3中没有此类型)  float bool  complex(复数型)
    2.非数字型: 字符串 列表 元组 字典 
"""
demo = 10 ** 10;
# print(2 ** 1000000) # type函数 ,查看变量的类型
# money = input("请输入")  # input控制台输入的函数
# money = float(input("请输入"))  # float函数  把数字变成浮点数1
name = "name";
## 格式化字符:    %s 字符串  %d 整数  %06d表示显示的位数   %f浮点数 %.02f 表示小数点后两位  %% 输出%
print("你好 %s%%" % name)  # 格式化输出

"""
流程控制
"""
# if   逻辑运算符  and  or  not
if_num = 2;
if (if_num == 1):
    print("true")  # 缩进的为同一代码块
elif (if_num == 2):
    print("无效")
else:
    print("false")
print("外围")
print(random.randint(10, 20))
# 循环
# 赋值运算符   += =  -= *=   /=  //=  %=  **=

i = 1;
while i < 10:
    i = i + 1;
    if i == 8:
        continue;
    print(i);

"""
定义函数
"""


def function(num1, num2):
    """测试函数 (ctrl + q 查看方法注释)"""
    return num1 + num2;


print(function(10, 10))
"""
列表
"""

list = [1, 2, 3, 3];
list2 = [4]
list.append(10);
list.insert(1, 5)
list.extend(list2)
list.pop()
list.remove(2)

print(list.index(1))
print(list)
print(len(list))
print(list.count(""))
list.reverse()
list.sort()  # 升序
list.sort(reverse=True)  # 降序
print(list)
name = "小明";
del name;

# 遍历
lis = [];
for li in lis:
    print(li)

"""
元组(定义后不可修改)
应用场景:格式字符串;保证列表不被修改;函数的参数和返回值
"""
list3 = [];
tuple1 = (1, 2, 3, 4, 5, 6);
print(tuple1.count(1))
print(len(tuple1))
print(tuple1.index(1))
tuple(list3)

"""
字典(无序的对象集合)(key:value)
"""
people = {"name": "小明", "age": 18}
people1 = {"gender": "男"}
people["school"] = "北大"  # 增
people.pop("age")  # 删
people["school"] = "清华"  # 改
print(people["name"])  # 查
print(len(people))  # 长度
people.update(people1)  # 合并字典 重复的key会被覆盖
print(people)

# 遍历
for key in people.keys():
    print(people[key])
for k in people:
    print(people[k])

"""
字符串
"""
str1 = "helloed 'xiaom'";

for str in str1:
    print(str)

print(len(str1))
print(str1.count("h"))

print(str1[0:5])  # 字符串截取
print(str1[0:])
print(str1[-3:])
print(str1[::2])  # 步长
print(str1[-1::-1])  # 逆序
print(str1[::-1])  # 可以省略其实索引

## 公共方法
listnum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(listnum))
print(max(listnum))
print(min(listnum))

print(id(listnum))
# 完整的for 变量 in 集合 :代码 else[循环结束后执行,使用break不执行] 代码

a = 10;
print(id(a))
a = "hello"
print(id(a))
a = [1, 2, 3]
print(id(a))
a = [2, 2, 2]
print(id(a))

print(hash("hello"))

x = 0.0;

for i in range(10):
    x += 0.1;
    print(x)

# 在python中是无法直接修改全局变量的,需要使用global关键字
num = 100;


def update():
    global num;
    num = 200;
    print(num);


def update1():
    print(num);


update();
update1();


# 定义多个变量来接收返回的元组数据
def rt():
    return (1, 2);


num1, num2 = rt();
print(num1)
print(num2)

# 交换两个变量的值
a = 10;
b = 20;
# 方法1
c = a;
a = b;
b = c;
# 方法2
a = a + b;
b = a - b;
a = a - b;
#方法3
a,b = (b,a);
print(a, b)

## 定义缺省方法

def moren(num,age = True,gender=True):
    print(num)
    print(age)
    print(gender)
moren(10,gender=10);

# 接收多值元素  *args表示元组参数,**kwargs表示字典
def manyparam(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)
manyparam(1 ,name ="小明")

# 元组和字典的拆包   传参时元组前加*  字典前加**
# 递归
def number_sum(num):
    if num ==1:
        return 1 ;
    temp = number_sum(num - 1)
    return num +temp;

print(number_sum(10))




#dir内置函数
def demo():
    """内置参数"""
    print("hellowrold")

demo();
print(dir(demo))
print(demo.__doc__)


#身份运算符 is 和is not 类似于id(a)==id(b)和!=,如果对none进行比较  使用is
#比较  == 比较的是内容  is 比较的是内存地址
