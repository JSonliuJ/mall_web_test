## webTest(关键字+数据驱动) 
### 01 依赖安装和项目启动

#### 1.1 安装项目依赖

pip install -r requirement.txt

#### 1.2 项目启动方式

- 终端运行：
  - `pytest -v -s 文件名.py::测试类名::测试函数名`
- 参数和终端方式一样
- pycharm命令行参数运行   
  -  `pytest.main()` 运行所有用例  
  - `pytest.main("-v -s 模块名::类名") `
  - `pytest.main(["-v", "模块名", "类名","函数名"]) `  运行指定用例
  - `pytest.main(["-v", "-m", "标签名1","标签名n"]) `# 运行打上标签的用例

### 02 框架模块
- common：公共层

- OutPuts：输出层——日志、html/allure报告、错误截图
    - base_page:基础页面封装—— 鼠标事件、键盘事件、弹窗处理、窗口切换、滚动条处理、js文件执行、元素查找、元素点击、文本获取等方法封装
    - file_path:路径处理
    - my_log:自定义logging模块
    - mysql_handle:数据库处理模块--mysql的增删改查操作
    
- PageLocators：元素定位数据

- PageObjects：对每个功能页面进行二次封装

- TestCases：测试用例
    - conftest：全局资源共享配置文件：
    - setup:每个用例执行前执行一次
    - teardown：每个用例执行后执行一次
    - SetupClass：每个测试类执行前执行一遍
    - TearDown：每个测试类执行前执行一次
    
- TestDatas：测试数据
    - common_datas：主要存放url、数据库连接信息
    - logins_datas等：每个页面用到的信息，如用户名、密码、手机号、预期结果等
    
- conftest：全局资源共享文件
    - 定义前后置：实例化driver、打开浏览器(并最大化)、关闭浏览器、刷新浏览器、打开浏览器并登陆等方法
    - 调用夹具：
      - 方式1：# @pytest.mark.usefixtures("夹具名")
      - 方式2：test_xxxx(夹具名)
    
- pytest.ini：
    - 定义执行的用例路径、用例匹配模式、测试用例标签注册、定义allure报告输出路径、失败执行次数设置等功能
    - 打标签：需要注册标签并在需要运行的行数上打上对应标签名
    
- requirement.txt：项目环境依赖

- run.py:项目执行入口文件

- pytest

    - 在对应测试类名、函数名上打 `pytest.mark.标记`

    - pytest.mark.skip 用例跳过执行

    - pytest-order

        - 安装：pip install pytest-order
        - 使用：@pytest.mark.run(order=数值) order值安装assic码顺序执行 

    - @pytest.fixure(scope，params，autouse,name)

        - scope：调用范围(有模块级别module、类级别class、函数级别function、会话session级别)
        - params：参数
        - autouse：自动调用
        - name：夹具别名

    - @pytest.mark.xfail(condition, reason="xxx") 

        - condition：预期失败的条件，必传参数

        - reason：失败的原因

### 03 项目主要功能模块

1. 注册：手机号
2. 登陆：手机、用户名
3. 商品搜索：页头、页主体、悬浮框
4. 商城收藏和取消收藏
5. 加入购物车和购物车删除
6. 商品查看：侧边栏、导航栏、商品详情
7. 商品购买：立即购买、加入购物车后购买、先收藏后购买
8. 商品下单：使用积分抵扣、不使用积分抵扣
9. 订单付款：支付宝、微信、银行卡
10. 个人中心查询：订单列表、订单状态、订单管理、账号管理、客户服务、中心首页（订单状态、订单列表）
11. 我的订单：订单查询、订单管理（支付、订单详情、添加收藏）
### 04 jenkins持续集成和报告输出

#### 1. 构建工程

![1665646602106](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665646602106.png)

![1665646628630](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665646628630.png)

![1665646665768](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665646665768.png)

![1665646708252](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665646708252.png)

![1665646749558](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665646749558.png)

#### 2. 启动任务

![1665647151700](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665647151700.png)

#### 3. 报告查看

![1665647405947](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665647405947.png)

![1665647435119](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665647435119.png)

![1665647532668](C:\Users\jieliu666\AppData\Roaming\Typora\typora-user-images\1665647532668.png)

### 05 后续持续优化

1. 步骤和关键字驱动
2. la