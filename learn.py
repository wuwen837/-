#字符串格式化  %d/f/s   % (     )
age = "蔡徐坤"
name = "我是毕业市场两年半的%s" % age
print(name)
i=11
o = 11.345
age = "我今年%.2f岁了，约%2d岁" % (o,i)     #%m.n精度控制
print(age)
#快速字符串格式化 f{   }
name = "老子"
year = "今年"
age = "14.4"
print(f"{name}{year}{age}岁了")
#输入  input(   )
"""print("请告诉我你是谁？")
name = input()
print("你是%s" %name)"""
#就等同于
"""name = input("请告诉我你是谁？")
print("你是%s" %name)"""
#bool类型True  Fasle 属于数字大类
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是:{bool_1},类型是:{type(bool_1)}")
print(f"bool_2变量的内容是:{bool_2},类型是:{type(bool_2)}")
#if_______:
#    结果
if 18>10:
    print(""
          "liantongpi")
#while ________:循环
i = 0
while i<100:
    print("失败\n")


    i+=1
    print(i)
print("成功")
#下面这个代码有问题，实现不了我要的功能
import random
num = random.randint(1,100)
print("茹嘉耶：这里有一束头发，在100跟以内，如果你能在10次内猜数有多少头发，我就答应你")
i = 0
aaaa = 0

while aaaa == 0:
    guess = int(input("你猜"))
    if guess > num:
        print("大了")
    elif guess < num:
        print("小了")
    else:
        aaaa = 1
    i += 1
    if i == 10:
        aaaa=1


if i <=10:
    print("我答应你了")
else:
    print("真可惜")
#多行字符对其\t
print("hello world")
print("i love")
#duibi
print("hello\tworld")
print("i\tlove")
#打印九九乘法表
#用i表示行，j表示列
i = 0
while i <=9:
    i+=1
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j}\t",end='')#end=''表示不换行
        j+=1
    print()    #用于输出一个换行
#for循环   for 变量 in 数据集
#数数有几个a
word = "itheima is a brand of itcast"
i=0
for x in word:
    if x =="a":
        i+=1
print(f"{i}")
#range(a,b)  取从a到b，不含b
#用for循环打九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}\t",end='')
    print()    #对外层循环 换行
#comtinue中止本次循环，直接进行下次循环
#break跳出循环


#函数の初体验
str1 = ("love")
str2 = ("like")
str3 = ("you")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)

#函数   def 函数名（传入参数）:
#          函数体
#          return(返回值)
def say_hi(name):
    print(f"{name},你好")

name1 = "茹嘉耶"
name2 = "张三"
say_hi(name)

def add(x,y):
    """
    add函数用于计算两数之和
    :param x: 一个数字
    :param y: 另一个数字
    :return: 结果
    """
    result = x + y
    print(f"两数之和为{result}")
    return result
#数据容器  list tuple str set dict                     --------------------------------------------------------------
#list
mylist = [1,"name","tom"]
print(mylist[0])
youlist = [[1,2,3],["one","two","three"]]
print(youlist[1][2])
print(mylist.index(1))#查询元素下标
mylist[0]="one"#修改特定元素
mylist.insert(1,"best")#特定位置插入元素
mylist.append("love")#尾部追加元素
mylist2=[4,5,6]
mylist.extend(mylist2)#将另一列表元素追加到此列表
del mylist[2]#删除特定元素
mylist.pop(1)#取出特定元素
mylist=[1,2,2,3,3]
mylist.remove(2)#移除匹配的第一个元素
mylist.clear()#清空列表
mylist.count(2)#统计列表中某元素的数量
mylist=[1,2,2,3,3]
count = len(mylist)#列表中元素总数

#元组tuple    ----不可修改 ----用（）                --------------------------------------------------------------
#其方法只有            .index（）    .count（）  len（）
t = (1,2,3,4,5,6)
t2 = ((1,2,3),(7,8,9))

#字符串 ---不可修改-----------------------------------------------------------------------------------------------
#.replace(a，b)  -----  将原字符串中的a替换为b以生成新字符串
#字符串的切分.split()------将字符串按某种符号分割开并存入列表中
#.strip()------去除首尾（）

#序列的切片   序列[起始下标：结束下表：步长]

ad = "万过薪月，元徐成吗黑，nohtyp学"
name = ad[-9:-14:-1]
print(name)
#集合--------------------------------------------------------------------------------------------------------------
#集合----- 不可重复  {a.b,c,d}     空集合------set()    无序
#           .add()添加元素-------------------------}
#            .remove()  移除元素                   }}}改变原集合
#            .pop()     随机取出元素                }}}
#                 .clear()  清空------------------}
# 集合1.difference.(集合2)   取差集    取出集合1有而集合2没有的   生成新集合
set1 = {1,2,3}
set2 = {1,4,5}
set1.difference(set2)
#消除差集      set1.difference_update(set2)   消除集合1与集合2相同的   改变集合1
#合并集合         set1.union()set2
my_list = [1,2,3,2,1,2,3,1,2]
my_set = set()
for x in my_list:
    print(x)
for x in my_list:
    my_set.add(x)
print(my_set)
#字典                 __-----------------------
#{key1:value1,key2:value2,key3:value3,key4:value4}
#-------------key不可重复
#姓名   语文   数学   英语
#小帅   59    80     90
#小美   66    70     60
#小刚   80    80     80
name_scord = {
    '小帅':{
    '语文':59,
    '数学':80,
    '英语':90
},'小美':{
    '语文':66,
    '数学':70,
    '英语':60
},'小刚':{
    '语文':66,
    '数学':70,
    '英语':60   }}
print(name_scord['小帅']['语文'])
#  字典名[key]=value          更新或添加
# .pop(key)   删除元素
#   .clear()   清空
#   .keys()   得到key
name_scord = {
    '小帅':{
    '语文':59,
    '数学':80,
    '英语':90
},'小美':{
    '语文':66,
    '数学':70,
    '英语':60
},'小刚':{
    '语文':66,
    '数学':70,
    '英语':60   }}

print(name_scord.keys())
#sorted   对数据容器的元素进行排序并塞入列表中
#sorted(列表名)  正序
#sorted(列表名,reverse=True)   倒叙
mylist = [3,7,4,6,2]
print(sorted(mylist))

#-------------------函数参数---------------------
#定义函数是嘴都关键字可以默认变量
def count(name,age,gender="女"):
    print(name,age,gender)

count(name = "小明",age = 8,)
count(name = "小明",age = 8,gender = "男")
#不定长-----位置不定长    传入为元组
def inf(*args):
    print(*args)
inf(1,2,"小明")
#关键字不定长   传入为字典
def inf(**kwargs):
    print(**kwargs)
inf(name = "小明",age =18,gender  = "女" )
#lambda匿名函数    只能使用一次
#lambda 传入参数：函数体
def test(add):
    result = add(1,2)
    print(result)
test(lambda x,y:x + y)
#-----------------------------------------文件------------------------------------------------------
#打开   f = open("name","mode",encoding)  mode为r/w/d
#读取   read（num）读取一定长度的数据
#      f.readlines（）全部读取返回列表
#       f.readline（）   读取一行
#        f.close    关闭文件
#-----———————————with open(name,mode,encoding) as f
#                      相关操作                                  ------————————————————————可以执行操作后自动关闭
#文件写入
f = open("E:\新建文档放这里\\learn.txt","w",encoding="UTF-8")  #注意，打开以存在文件时，接下来写入内容会将原文件覆盖；打开不存在文件时，会自动创建文件
f.write("hello world happiness")   #写入内存某一分区
f.flush()    #刷新，写入硬盘
f.close()    #关闭文件
#文件追加写入      将“mode”改为“a”，其他和写入一样