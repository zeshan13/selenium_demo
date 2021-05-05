### 时序图

在线生成时序图
https://plantuml.ceshiren.com/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

```
@startuml
企业微信主页面 -> 通讯录页面 : 点击通讯录tab
企业微信主页面 -> 导入通讯录页面 : 点击导入通讯录
企业微信主页面 -> 添加成员页面 : 点击添加成员
通讯录页面 -> 企业微信主页面 : 点击首页tab
通讯录页面 -> 添加成员页面 : 点击添加成员
通讯录页面 -> 导入通讯录页面 : 1.点击批量导入/导出；\n2.点击文件导入
通讯录页面 -> 添加部门页面 : 1.点击“+”号按钮；\n2.点击添加部门
添加成员页面 -> 通讯录页面 : 点击保存/取消
添加成员页面 -> 添加成员页面 : 点击保存并继续添加
添加部门页面 -> 通讯录页面 : 点击保存/取消/关闭弹窗
导入通讯录页面 -> 通讯录页面 : 导入完成/返回
@enduml
```



### PageOject

![1620012825631](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1620012825631.png)

马丁福勒博客：

https://martinfowler.com/bliki/PageObject.html

六大原则：

 ![image](https://ceshiren.com/uploads/default/original/2X/e/ef29c9aed7911696a26b245017b4716811cd0319.jpeg) 



### 原则解读

- 方法意义 
  - 用公共方法代表UI所提供的功能
  - 方法应该返回其他的PageObject或者返回用于断言的数据
  - 同样的行为不同的结果可以建模为不同的方法
  - 不要在方法内加断言
- 字段意义 
  - 不要暴露页面内部的元素给外部
  - 不需要建模UI内的所有元素

