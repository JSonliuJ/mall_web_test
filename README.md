## webTest(关键字+数据驱动)

### 01 环境安装

1. 安装selenium：

 - `pip install -U selenium`

2. 安装chrome浏览器和chromedriver

 - chromedriver下载地址：`http:npm.taobao.org/mirrors/chromedriver/`
 - *特别提示：* chrome与chromedriver版本要对应

3. chromedriver放在Python安装根目录下面即可

### 02 webdriver通信流程（http请求，json数据）

代码(selenium webdriver) ---http通信--> 驱动程序(chromedriver.exe、ieserverdriver) ---> 浏览器

1. xxxdriver启动。ip+端口号监听中
2. webdriver跟driver建立连接，然后发送*http*请求
3. driver收到指令之后，驱动浏览器执行
4. driver把响应结果返回给python selenium webdriver
5. 继续发下一个http请求
   。。。
6. 断开连接，关闭驱动服务，关闭浏览器
7. 接收和发送数据类型：json

### 03 xpath

![img.png](img.png)

###  04web页面操作（一）：三大等待、四大操作

1. 输入操作 keys()
2. 点击 click()


1. sleep - 强制等待
2. 智能等待：最多等待15s，如果15s内任何一个元素出现了，继续执行下一行代码，超时：报超时异常，TimeoutException、NosuchElementExption
   - 隐性等待：2种场景 1个元素被找到-元素存在/1条命令被执行完成-api的执行，每一个会话当中，只需要调用一次
     会话：从打开浏览器到 quit关闭浏览器整个过程， ---sessionId
   - 显性等待：等待元素可见、等待url变更为xxx、等待新的窗口出现、等待元素可用
     在需要的地方：直接用显性等待。条件+等待
     等待上限：15s 轮询周期：默认0.5s确认一次。webDriverWait类
     条件：有一个专门的条件模块。expected_condition
     WebDriveWait(driver,15,0.5).until/not_until(条件)

### 05web自动化框架

背景：ui非常依赖页面---每一个元素定位的稳定性

 - 历史稳定的功能 - ui自动化 - 解放手工点点点 
 - 重复、繁琐、人工遗漏
 - 新功能 - 人工测试
 - 旧功能 - 新功能的修改引起的历史bug
   回归：
   - 接口自动化(尽可能覆盖异常) +ui自动化(正向场景+部分逆向场景)
     长期运行自动化脚本：可扩展性/可维护性/可回溯性

为什么pytest不用ddt

1. 没有固定相同步骤，不适合ddt

#### 5.1po模式

1. 只改一处，然后所有用例通通都改了
2. 核心思想：测试对象(页面)、测试用例(页面操作+测试数据) 彻底分离
   实现方式：
   1. 一个页面，对应一个类，page类。这个页面的元素定位、元素操作
   2. 用例当中，直接调用页面当中的页面操作 
      1）功能模块里：涉及哪些页面、页面哪些操作
      登录页面 - 登录操作，获取提示信息行为
      首页 - 页面是否包含了某个元素/某个元素是否可见
3. 页面封装：页面操作/元素的文本/元素属性的获取

#### 5.2 二次细分

元素定位和页面操作分离
PageLocators + pageObjects

#### 5.3 投资

![img_1.png](img_1.png)

#### 5.4 web自动化框架

1. basepage:日志输出/失败截图/异常处理，封装网页操作简化代码/路径配置

   - 等待元素可见
   - 元素存在
   - 点击
   - 查找元素
   - 输入文本
   - 窗口切换
   - iframe切换
   - 滚动条操作
   - 文件上传

2. 测试数据testDatas

3. 测试用例 testCases

4. 运行用例和生成报告 main.py：

5. 输出层：日志/报告/错误截图

6. pageobject：页面对象层

7. pagelocators：元素定位层

8. 筛选用例/重运行机制
   调页面对象行为 + 测试数据
         ||
       页面对象
         ||
   selenium webdriver api(日志/失败截图)
         ||

     1. 等待可见 wait_ele_visible
     2. 查找元素 find_element
     3. 点击--必然前提：等待、查找 click_element 
     4. 输入--必然前提：等待、查找 input_text
     5. 获取属性--必然前提：等待、查找 get_element_attribute
     6. 获取文本--必然前提：等待、查找 get_element_text
        每一个函数：提供一个功能，公共的功能
         关键字：已经实现的功能。只需要负责调用

   basepage):
    1)创建-个basepage.py实现BasePage类.
    1oc代表元素定位，img. name代表业务操作
    6大方法是什么？
    如何实现日志/异常截图?
    2)测试basepage类。
    3)测试通过之后，更新PageObjects目录下的页面对象行为。--- 先修改登陆用例涉及到的页面。
    4)运行登陆用例，确保运行成功。
    5)看看日志生成了吗。截图生成了吗

### 06 pytest

#### 6.1pytest与unittest区别

```
pytest:基于unittest之上的单元测试框架。
1、自动发现测试模块和测试方法; 
2、断言使用assert +表达式即可;
3、可以设置测试会话级、模块级、类级、函数级的fixtures用例的前置和后置
unitest:setup、teardown. setupClass、 teardownClass
共享前置后置-- conftest.py
4、有丰富的插件库，目前在600个以上。= = allure
```

1. 表达用例：

   - unittest:定义一个类，继承unittest.TestCase
   - pytest:类/函数

2. 断言的表达

   - unittest:self.assertxxx()
   - pytest：assert 表达式(结果为true-断言成功，否则-断言失败)  逻辑/成员/比较/函数返回值

3. 收集用例

   - unittest: TestLoader类+TestSuite类,discover收集用例
   - pytest：自动收集用例

4. fixture： 前后置   

   - unittest：setup&teardown setupClass&teardownClass ---固定名称

   - pytest:function(用例) -> class(测试类） -> module(.py) -> session(会话) ---不固定名字(函数)/ 前后置放在一个函数里/ 不与测试类放在一起(独立）测试函数/测试类/模块/会话

   - 定义: 

     - 1、怎么知道函数它是一个前置后置?
       在函数前面：@pytest.fixture

      ```
      @pytest.fixture
           def init():
              pass
      ```

     - 2、怎么区分前置和后置? yeild --前后置隔分

      ```
      @pytest.fixture
      def init():
          driver = webdirver.Chrome()
          driver.get('http://www.baidu.com')
          yeild
          driver.close()
          driver.quit()
      ```

     - 3、作用域是什么?测试函数/类/模块/会话? @pytest.fixture(scope=?)
       - function：默认值 unittest当中setup和teardown
       - class：测试类 unittest当中setupClass和teardownClass，
       - module：模块 整个py文件
       - session：会话 收集到的所有测试用例
         接口：前置-连接数据库 后置-关闭连接
     - 4、如何返回数据

   - 共享：conftest.py 名称固定

     - 1）专门用来存放fixture
     - 2）作用域(哪些范围内的用例可以使用)：conftest.py所在文件内的用例都可以使用 
     - 3）用例文件当中不需要引入，直接调用fixture名称就可以  

   - 调用:

     - 5、 测试用例当中，如何调用这个前置后置?
       在测试用例/类前面：
       `@pytest.mark.usefixture("定义的fixture名称")`
     - 6、接收返回值的方式：

      ```
      将fixture的函数名称，作为用例的参数
      用例的参数 = 返回值
      测试用例参数：1. 数据驱动、2. fixture返回值
      如果需要使用fixture返回值，一定要传参，可以不用`@pytetst.mark.usefixture`
      如果fixture没有返回值，测试要使用，必须申明：`@pytest.mark.usefixtures`
      ```

   - 总结：

     - 定义：申明pytest.fixture/yield区分前后置/作用域scope
       - 1）测试用例文件当中定义
       - 2）conftest.py当中定义 -- 共享
         - 2.1) conftest.py定义的fixture,哪些范围内的用例可以调用我:conftest.py所在的包下，所有的用例均可以。
         - 2.2）在不同的包下，可以创建自己的conftest.py
     - 调用：测试用例/测试类
       - 1）用例不需要使用fixture返回值：`@pytest.mark.usefixtures("")`
       - 2)用例要使用fixture返回值：
         - 方式1：@pytest.mark.usefixtures("").fixture函数名称作为用例参数
         - 方式2：fixture函数名称作为用例参数
         - 用例的参数有两种：1）数据驱动 2）fixture
       - 3）需要的时候才调用
       - 4）如果测试类下面，所有的测试用例都使用同一个函数级别的前后置
         那么直接在类名上，申明调用：`@pytest.mark.usefixtures("函数级别的fixture")`

5. 插件

   - unittest：无
   - pytest：700+ html、allure、重运行  
     - 安装方式：pip install ...

- 区别总结：
  - 1.自动收集/断言/写用例/插件/前后置
  - 2.筛选用例：1）注册标签名 2）打标记 `@pytest.mark.标签名` 3)运行过滤：`pytest.mark(['-m','标签名'])`

#### 6.2.pytest之mark功能

- 筛选用例：

  - 1.注册标签名
    注册方式：创建pytest.ini文件，在文件中按如下形式添加标签名：

    ```
    [pytest]
    markers= 
        slow:marks tests as slow(deselect with '-m "not slow"'
        serial
    ```

  - 2.在测试用例/测试类上面加：`@pytest.mark.已注册的标记名`

    - 更多标签方法：

      - 打标记范围:测试用例、测试类、模块文件
      - 在测试类里，使用以下申明(测试类下,所有用例都被打上该标签):

      ```
      class TestClass(object):
          pytestmark = pytest.mark.已注册标签名
          pytestmark = [pytest.mark.标签1, pytest.mark.标签2] # 多标签模式
      ```

      - 在模块文件里，同理(py文件下，所有测试函数和测试类里的测试函数，都有该标签):

      ```
      import pytest
      pytestmark = pytest.mark.webtest
      pytestmark = lpytest.mark.标签1, pytest.mark.标签2] # 多标签模式
      ```

  - 3.运行时，只运行标记了的用例
    pytest.mark(['-m','标签名','-s','-v'])
     unittest.main()

#### 6.3.pytest之命令行运行用例

- 收集的机制：
  - 1.从哪个目录开始收集
    pytest命令在哪个目录下执行，就默认从哪个目录下开始搜索用例
  - 2.文件：目录下所有的文件都需要去看是否有用例吗？
    不需要
     目录下，有文件/子目录
      - 符合以下标准的文件，才会去文件中确认是否有用例
        - 1）.py 
        - 2)文件名以test_开头，或以_test结尾  
  - 3.用例名称：以test_开头的函数。或者以Test开头的类(不含__init__)名下，以test_开头的方法
- 执行顺序
      1）文件名称顺序 - ascii排序
      0-9 a-z A-Z

#### 6.4.pytest之fixture功能

- 范围：
  - 一个fixture，可以使用比它高的/与它同级的fixture作为它的参数
  - function可以调用class，function，module，session
  - fuction是最小单位。最后执行，其它的级别一定比它先执行

#### 6.5.pytest之参数化

- pytest参数化

  - 在测试用例的前面加上：
    `pytest.mark.parametrize("参数名",列表数据)`
    参数名:用来接收每一项数据，并作为测试用例的参数。
    列表数据:一组测试数据。
    `pytest.mark.parametrize("参数1,参数2",[(数据1，数据2).(数据1，数据2)])`
    示例:

    ```
    pytest.mark.parametrize("a,b,c".[(1,3,4),(10,35,45),(22.22,22.22,44.44)])
    def test_add(a,b,c):
        res = a + b
        assert res == c
    ```

  - 组合参数化:多组参数，依次组合。
    使用多个@pytest.mark.parametrize
    示例:用例有4个: 0,2/0,3/1,2/1,3 迪卡尔积

  ```
  @pytest.mark.parametrize("x", [0, 1])
  @pytest.mark.parametrize("y", [2, 3])
  def test_ foo(x, y):
      pass
  ```

#### 6.6.pytest之重运行

- 重运行机制：针对失败用例(提高用例稳定性/通过率的手段之一)
  - test提供了失败重试机制:
    - 插件名称: `rerunfailures`
    - 安装方法: `pip install pytest-rerunfailures`
  - 使用方式:
    - 命令行参数形式:
      - 命令:`ytest --reruns 重试次数`
        - 比如: `pytest --reruns 2` 表示:运行失败的用例可以重新运行2次。
      - 命令: `pytest --reruns 重试次数 --reruns-delay 次数之间的延时设置(单位:秒)`
        - `Pytest --reruns 2 --reruns-delay 5` 表示失败的用例可以重新运行2次。第一次和第二次的间隔时间为5秒钟。

#### 6.7.pytest之html报告

pytest可以生成多种样式的结果:

1. 生成JunitXML格式的测试报告:命令: `-junitxml= path`
2. 生成result log格式的测试报告:命令: `--resultlog= report\log.txt`
3. 生成Html格式的测试报告:命令: `--html=report\test_ one. _func .html(相对路径)
   pip install pytest-html

#### 6.8.pytest之allure测试报告

命令行工具，独立于各种测试工具之外

1. allure安装链接：
   https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
2. 与pytest集成：需要pytest执行用例后，生成allure能够解析的测试结果文件

 - 安装： `pip install allure-pytest`

3. 使用：

 - `pytest --alluredir=/tmp/my_allure_results`
 - 使用allure命令，生成html样式的报告 `allure serve alluredir的路径`

#### 6.9.pytest之Jenkins集成

