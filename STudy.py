

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':#字符串''或""|科学计数法用e代替10|
    #转译字符
    # \t制表符
    # \n换行
    #\\表示\
    #print_hi("PyCharm'\\,\nhellow,")
  print_hi(r'''PyCharm'\,
   hellow,
   aka chip''')#r'''   '''

#布朗值不用设置，3>2自动输出|空值为None|派=PI=3.14159265359
#除法不同，//地板除就是保留整数位|%取余|
def main():
    t = 123
    f = 456.789
    s1 = 'HELLO,AKA'
    s2 = r'HELLO, \' AKA'
    s3 = "HELLO, \\ \n'AKA"
    print("t =", t)
    print("f =", f)
    print("s1 =", s1)
    print("s2 =", s2)
    print("s3 =", repr(s3))
    print('\u4e2d\u6587')#
if __name__ == '__main__':
    main( )
    #Unicode字符集和UTF-8
   # print('包含中文的str')
    #ord()获取字符整数|chr()吧编码转成对应字符
    #可以得到，获取中文
    ord('中')
    #20013
    chr(25991)
   #'文'
   #见36行。warm 网络运输和保存磁盘需要吧str变为bytes
   #x=b'ABC'这个是bytes而x='ABC'是str
   #str可以用encode()编码变为bytes
  # 'ABC'.encode('ascii')#及转为UTF-8再变为ASCII或者ASCII形式
  #反之用decode
  #  b'ABC'.decode('ascii'),如果纯在一小部分无效字节可以使用errors='ignore'
  #用len()函数计算字符数
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
#格式化内容，eg:'HELLO,%s,you have $%d.'%('Michael',1000000)
#print('%2d-%02d' % (3,1))
#print('%.2f % 3.1415926')
#format()  用{0},{1}......占位，后用format函数以此替换
#f-string
#r=2.5
#s=3.14 *r**2
#print(f'这里是字符串{s}和{r}')



#list|有序的集合|可以使用.sort()语句直接排序原表|。sort(reverse=True)降序|或者对key参数进行自定义排序
classmates=['chip','bob','ma']#classmates现在就是一个list|可以使用len函数获取classmates的个数
#classmates[-1]直接获取最后一个
#classmates.append('aka')|classmates.insert(1,'bitch')|删除表尾  classmates.pop()
#classmates.pop(1)|也可以替换classmates[1]='666'
#list里面也可以是另一个list  s = ['python', 'java', ['asp', 'php'], 'scheme']
#p = ['asp', 'php']
#s = ['python', 'java', p, 'scheme']
#tuple|不能修改|元组
#为了消除歧义使用 t=(1,)

  #条件判断 if语句忽略和c差不多多一个elif
  #关于input
#birth = input('birth: ')
#   print('00前')
#else:
#    print('00后')
#输入1982，会报错，input返回的数据类型为str,需要转换为int
#所以添加s=input('birth: ')|birth=int(s)
height=1.75
weight=80.5
bmi=weight/(height*height)
#if bmi<18.5:
#    print('细狗，太轻了')
#elif bmi>18.5 and bmi<25:
#    print('一般')
#elif bmi>25 and bmi<28:
#    print('重了')
#elif bmi>28 and bmi<32:
#    print('肥肥了')
#else:
#    print ('良子')
#针对多个elif且仅仅针对某个变量的判断可以使用match语句进行改良
#match bmi:
#    case x if x<18.5:
 #       print('细狗，太轻了')
        #还可以用case 18.6|18.7|18.8:
#match匹配列表
#用list    args=['gcc','hello.c']存储
#args=['gcc','hello.c','world.c']
#match args:
#    case ['gcc']:
#        print('gcc:missing source files(S).')#只出现gcc，报错
#    case ['gcc',file1,*files]:
#        print('gcc compile:'+file1+','+','.join(files))#*表示至少绑定一个文件
#    case ['clean']:
#        print('clean')
#    case _:
#        print('error')
#循环
#for in   就是把每个元素代入变量
#names = ['Michael', 'Bob', 'Tracy']
#for name in names:
#   print(name)
#range()函数可以生成整数序列
#循环2  while 循环和break结束语句、continue跳过

#dict 字典和set注意均不能放入可变对象
#用list实现同学名字找成绩要两个list表，用dict可以更加简洁
#d={'chip':99,'aka':88,'bob':60}
#d['chip']或者d['chip']=100
#为避免key不存在报错可以使用'chip'in d
#或者使用d.get('chip')也可以使用d.get指定value eg: d.get('chup',1)
#用pop(key)删除key时对应的value也会被删除|dict的key必须是不可变对象不能用list。
#set 是key的合集但是不存储value，并且key不能重复
#用{x,c,v}直接列|用list合集|可以使用add(key)添加元素，remove(key)删除元素|可以做到交集和并集

#--------------------------------------------------------------------------------------
#函数调用
#1.abs()函数求绝对值|
#自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')#参数检查,
    if x>=0:
        return x
    elif x<0:
        return -x
    else:
        pass#空函数pass语句
#print(my_abs(-1221)
#注意如果 将my_abs(）保存为aka.py文件，在同目录下的文件可以使用from aka import my_abs来导入该函数
#多值返回
import math#math数学函数包用import导入|实际上返回的是一个元组tuple

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#函数的参数
#默认参数|及def power( x,n=2)|必须指向不变对象eg:str,none
#可变对象|可以在list或者tuple前面加上*来表示将元素转化为可变参数
#关键参数**|def person(name, age, **kw):|用于自动内部组装一个dict|可以用于选填项
#关键字参数命名
def person(name,age,*,city,job):#|与**kw不同，命名用*，将自动吧后面参数视为命名关键参数
    print(name,age,city,job)
#不同的是命名关键字必须带上参数名，但是如果def时使用默认eg: city='BeiJing'调用时就可以不传city参数
#def f1(a, b, c=0, *args, **kw):
    #print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#def f2(a, b, c=0, *, d, **kw):
  #print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#---------------------------------------------------------------------------------------
#切片|Slice
#取list的前三个元素
#l[0:3]同时如果是从0开始可以省略L[:3]
#L[:10:2]前十个每两个取一个|L[::2]没两个取一个|L[:]复制list|tuple也可以切片eg:(1,2,3,4,5,)[:3]得到(1,2,3)
#字符串也可以看作list使用切片
#迭代|相对于c中更加自由不需要下标
#利用for......in
# d = {'a': 1, 'b': 2, 'c': 3}
#for key in d:
#    print(key)



























