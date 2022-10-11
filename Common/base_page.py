# —— coding :utf-8 ——
# @time:    2020/10/7 20:58
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    base_page.py
from selenium.webdriver import Chrome

from Common.my_log import MyLog

logging = MyLog()
import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Common.file_path import screenshots_path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# import win32gui
# import win32con
# pip install pywin32

class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    # 1. 等待元素可见
    def wait_eleVisible(self, locator, timeout=20, poll_frequency=0.5, doc=""):
        """
        :param locator: 元素定位，元组形式。 (元素类型,元素定位方式)
        :param timeout:
        :param poll_frequency:
        :param doc: 模块名称_页面名称_操作名称
        :return:
        """
        logging.info('等待元素可见：{}可见'.format(locator))
        try:
            # 开始等待时间
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.datetime.now()
            # 等待时长，转换为s
            wait_times = (end_time - start_time).seconds
            logging.info(
                "{0}:元素:{1}已可见，等待起始时间：{2}，等待结束时间：{3}，等待时间：{4}".format(doc, locator, start_time, end_time, wait_times))
        except:
            # 铺获异常到日志中
            # 截图--保存到指定目录
            logging.error('等待元素可见失败！')
            self.save_screenshot(doc)
            raise

    # 2. 判断元素是否存在
    def ele_isExist(self, locator, timeout=10, doc=""):
        logging.info("{}中是否存在元素：{}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            logging.info("{0}秒内页面{1}中存在元素：{2}".format(timeout, doc, locator))
            return True
        except:
            logging.error("{0}秒内页面{1}中不存在元素：{2}".format(timeout, doc, locator))
            return False

    def wait_element_clickable(self, locator, timeout=10, doc=""):
        """等待元素可以被点击"""
        logging.info("{}中元素是否可点击：{}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            logging.info("{0}秒内页面{1}中元素可点击：{2}".format(timeout, doc, locator))
            return True
        except:
            logging.error("{0}秒内页面{1}中元素不可点击：{2}".format(timeout, doc, locator))
            return False

    # 3. 查找元素
    def find_element(self, locator, doc=""):
        logging.info('{0}查找元素：{1}'.format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.error('查找元素失败')
            self.save_screenshot(doc)
            raise
            # 3. 判断元素是否存在

    # 4. 点击操作
    def click_element(self, locator, doc="", force=False):
        ele = self.find_element(locator, doc)
        logging.info('{0}点击元素：{1}'.format(doc, locator))
        try:
            if force:
                # 强制点击
                action = ActionChains(self.driver)
                logging.info('{0}点击元素：{1}成功'.format(doc, locator))
                action.click(ele).perform()
            else:
                # 不强制点击
                self.wait_element_clickable(locator)
                logging.info('{0}点击元素：{1}成功'.format(doc, locator))
                ele.click()
        except:
            logging.error('元素点击操作失败！')
            self.save_screenshot(doc)
            raise

    # 5. 输入操作
    def input_text(self, content, locator, doc=""):
        ele = self.find_element(locator, doc)
        logging.info('{0}元素：{1}输入文本'.format(doc, locator))
        try:
            logging.info('{0}元素：{1}，输入内容为：{2}'.format(doc, locator, content))
            ele.send_keys(content)
        except:
            logging.error('{0}元素：{1}输入失败'.format(doc, locator))
            self.save_screenshot(doc)
            raise

    # def input_text(self, content, locator=None, doc=""):
    #     """输入内容
    #     当 locator 为 None : 直接输入
    #     如果locator 传入元素定位表达式，   ("id", "kw")
    #     """
    #     try:
    #         if locator is None:
    #             action = ActionChains(self.driver)
    #             logging.info('{0}输入内容为：{1}'.format(doc, content))
    #             action.send_keys(content).perform()
    #         else:
    #             el = self.driver.find_element(locator)
    #             print(el)
    #             logging.info('{0}元素：{1}，输入内容为：{2}'.format(doc, locator, content))
    #             action = ActionChains(self.driver)
    #             action.send_keys_to_element(el, content).perform()
    #     except:
    #         logging.error('{0}元素：{1}输入失败'.format(doc, locator))
    #         self.save_screenshot(doc)
    #         raise

    # 6. 获取元素文本
    def get_element_text(self, locator, doc=""):
        ele = self.find_element(locator, doc)
        logging.info('{0}获取元素：{1}的文本内容'.format(doc, locator))
        try:
            text = ele.text
            logging.info('{0}获取元素：{1}的文本内容为：{2}'.format(doc, locator, text))
            return text
        except:
            logging.error('获取元素：{}文本内容失败'.format(locator))
            self.save_screenshot(doc)
            raise

    # 7. 获取元素属性
    def get_element_attribute(self, locator, attr, doc=""):
        ele = self.find_element(locator, doc)
        logging.info('{0}获取元素：{1}的属性：{2}'.format(doc, locator, attr))
        try:
            ele_attr = ele.get_attribute(attr)
            logging.info('{0}元素：{1}的属性：{2}值为：{3}'.format(doc, locator, attr, ele_attr))
            return ele_attr
        except:
            logging.error('{}获取元素：{}的属性失败'.format(doc, locator))
            self.save_screenshot(doc)
            raise

    def assert_text_equal(self, locator, expected):
        el = self.driver.find_element(locator)
        assert el.text == expected

    # 8. alert处理
    def switch_to_alert(self, timeout=30, poll_frequency=0.5, action='accept', doc=""):
        logging.info('{0}_切换alert弹框'.format(doc))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            value = alert.text
            logging.info('{0}当前弹框内容为:{1}'.format(doc, value))
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            return value
        except:
            logging.error('{}弹框操作失败！'.format(doc))
            self.save_screenshot(doc)
            raise

    # 9. 保存截图
    # def save_screenshot(self, doc):
    #     # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
    #     # filePath = "截图路径" + "{0}".format(time.strftime("%Y%m%d%H%M%S"))
    #     filePath = screenshots_path + "{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #     try:
    #         self.driver.save_screenshot(filePath)
    #         logging.info("截取网页成功，文件路径为：{}".format(filePath))
    #     except:
    #         logging.error('保存网页失败!')
    #         raise

    def save_screenshot(self, doc=''):
        """截图到 allure报告"""
        f = self.driver.get_screenshot_as_png()
        allure.attach(f, name=doc, attachment_type=allure.attachment_type.PNG)

    # 10. 滚动条处理
    def scrollbal_handle(self, url, mode='foot', doc=""):
        global js
        logging.info('{}进行滚动条操作'.format(doc))
        try:
            self.driver.get(url)
            if mode == 'top':
                # 滚动到顶部
                js = "window.scrollTo(0,0)"
                self.driver.execute_script(js)
            else:
                # 滚动到底部
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.driver.execute_script(js)
            logging.info('{}滚动成功'.format(doc))
        except:
            logging.error('{}滚动操作失败'.format(doc))
            self.save_screenshot(doc)
            raise

    # 11. 上传操作
    # def upload_file(self, UpfilePath, doc=""):
    #     logging.info('{}进行文件上传'.format(doc))
    #     try:
    #         dialog = win32gui.FindWindow('#32770', '打开')  # 一级
    #         # 二级窗口
    #         ComBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComBoxEx32', None)
    #         # 三级窗口
    #         ComboBox = win32gui.FindWindowEx(ComBoxEx32, 0, 'ComboBox', None)
    #         # 四级窗口
    #         edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #         button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&0)")
    #
    #         # 操作
    #         # 输入文件地址
    #         win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, UpfilePath)  # 发送文件路径
    #         # 打开文件按钮
    #         win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
    #         logging.info('{}文件上传成功'.format(doc))
    #     except:
    #         logging.error('{}文件上传操作失败'.format(doc))
    #         self.save_screenshot(doc)
    #         raise

    # 12. iframe切换
    def switch_to_frame(self, locator, doc=""):
        ele = self.find_element(locator)
        logging.info('{}表单切换'.format(doc))
        try:
            self.driver.switch_to.frame(ele)
            logging.info('{}切换表单成功'.format(doc))
        except:
            logging.error('{}切换表单失败！'.format(doc))
            self.save_screenshot(doc)
            raise

    # 13. 窗口切换
    def switch_to_window(self, window_reference, timeout=30, poll_frequency=0.5, window_handles=None, doc=""):
        logging.info("{0}_切换窗口".format(doc))
        try:
            if window_reference == "new":
                if window_handles:
                    WebDriverWait(timeout, poll_frequency).until(EC.new_window_is_opened(window_handles))
                    current_window_handles = self.driver.window_handles
                    self.driver.switch_to.window(current_window_handles[-1])
                else:
                    logging.error("打开新窗口时，请传入window_handles参数")
                    raise ("打开新窗口时，请传入window_handles参数")
            elif window_reference == "default":
                self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.window(window_reference)
            logging.info("{0}_切换窗口成功".format(doc))
        except:
            logging.error("{0}_切换窗口失败".format(doc))
            self.save_screenshot(doc)
            raise

    # 14. 执行js
    def execute_script(self, js_str, element_info=None, doc=""):
        logging.info('{}执行js'.format(doc))
        try:
            if element_info:
                self.driver.execute_script(js_str)
            else:
                self.driver.execute_script(js_str, None)
            logging.info('{}执行js成功'.format(doc))
        except:
            logging.error('{}执行js操作失败'.format(doc))
            self.save_screenshot(doc)
            raise

    # 15. 鼠标事件
    # 元素鼠标操作：右击-测试OK
    def context_click(self, locator):
        mouse = ActionChains(self.driver)
        ele = self.find_element(self, locator)
        logging.info('{}元素进行右击操作'.format(locator))
        mouse.context_click(ele).perform()

    # 元素鼠标操作：移动到该元素上--测试OK
    def move_to_element_by_mouse(self, locator):
        ele = self.find_element(locator)
        mouse = ActionChains(self.driver)
        logging.info('将鼠标移动到{}元素上'.format(locator))
        mouse.move_to_element(ele).perform()

    # 长按元素
    def long_press_element(self, locator, seconds):
        ele = self.find_element(locator)
        mouse = ActionChains(self.driver)
        logging.info('将鼠标长按到{}元素上后松开'.format(locator))
        mouse.click_and_hold(ele).pause(seconds).release(ele)

    def scrollIntoView(self, locator):
        ele = self.find_element(locator)
        logging.info('将滚动条滚动至{}元素可见'.format(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', ele)
        time.sleep(1)

    def double_click(self, locator):
        """双击"""
        el = self.driver.find_element(*locator)
        mouse = ActionChains(self.driver)
        logging.info('双击{}元素'.format(locator))
        mouse.double_click(el).perform()

    def move_to(self, locator, xoffset=0, yoffset=0):
        """悬停"""
        el = self.driver.find_element(locator)
        mouse = ActionChains(self.driver)
        logging.info('鼠标悬停到{}元素上'.format(locator))
        mouse.move_to_element_with_offset(el, xoffset=xoffset, yoffset=yoffset)

    def move_by(self, xoffset, yoffset):
        """移动多少个像素点"""
        mouse = ActionChains(self.driver)
        mouse.move_by_offset(xoffset, yoffset).perform()

    # 16. 键盘事件
    # 删除内容-测试OK
    def back_space(self, locator):
        ele = self.find_element(locator)
        logging.info('{0}元素操作back_space'.format(locator))
        ele.send_keys(Keys.BACK_SPACE)

    # 清空内容--测试OK
    def clear_input(self, locator):
        ele = self.find_element(locator)
        logging.info('{}元素输入框操作清空'.format(locator))
        ele.clear()

    # 按回车--测试OK
    def enter(self, locator):
        ele = self.find_element(locator)
        logging.info('{}元素进行回车键操作'.format(logging))
        ele.send_keys(Keys.ENTER)

    # 全选  Ctrl+a--测试OK
    def ctrl_a(self, locator):
        ele = self.find_element(locator)
        logging.info('{}元素输入框内容进行全选操作'.format(locator))
        ele.send_keys(Keys.CONTROL, 'a')

    # 粘贴 Ctrl +x--测试OK
    # def ctrl_x(self, locator):
    #     ele = self.find_element(locator)
    #     logging.info('{}元素输入框内容进行剪切操作'.format(locator))
    #     ele.send_keys(Keys.CONTROL, 'x')
    #
    # # 粘贴 Ctrl +v--测试OK
    # def ctrl_v(self, locator):
    #     ele = self.find_element(locator)
    #     logging.info('{}元素输入框内容进行粘贴操作'.format(locator))
    #     ele.send_keys(Keys.CONTROL, 'v')

    def copy(self, content=None, all=None):
        """复制
        # TODO: pyclipper
        """
        action = ActionChains(self.driver)
        if (content is None) and (all is None):
            # 直接按ctrl + C
            action.key_down(Keys.CONTROL)
            action.send_keys('c')
            return action.key_up(Keys.CONTROL).perform()

        if all:
            action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            action.key_down(Keys.CONTROL)
            action.send_keys('c')
            return action.key_up(Keys.CONTROL).perform()

    def paste(self):
        """粘贴"""
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys('v').key_down(Keys.CONTROL)
        return action.perform()

    # 17. 等待操作
    def implicitly_wait(self, seconds=15):
        self.driver.implicitly_wait(seconds)

    def wait(self, seconds=5):
        time.sleep(seconds)

    # 18.浏览器操作
    def open_url(self, url):
        self.driver.get(url)
        logging.info('打开URL地址%s;' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logging.info("设置浏览器的最大化")

    def close_tab(self):
        self.driver.close()
        logging.info('关闭当前的tab页签')

    def set_browser_min(self):
        self.driver.minimize_window()
        logging.info("设置浏览器的最小化")

    def browser_refresh(self):
        self.driver.refresh()
        logging.info("浏览器的刷新操作")

    def get_title(self):
        value = self.driver.title
        logging.info("获取网页的标题为：%s" % value)
        return value

    def quit_browser(self):
        '''退出浏览器'''
        self.driver.quit()
        logging.info("关闭浏览器")
