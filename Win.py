# -*- coding: utf-8 -*-
import os
import re
import time
import requests
from head import headers
from threading import Thread
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def __init__(self, parent=None):
        self.keywd = "王心怡"  # 搜索关键词
        self.host = "https://www.xiuren02.cc"  # 主机域名
        self.save_pt = "./Downloads"  # 下载保存路径
        self.search_url = self.host + "/plus/search/index.asp"  # 搜索url
        self.obj_str()
        self.obj_img()
        self.obj_bar()

    def gone(self):
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)

    def obj_bar(self):
        self.obj_prBar = QtCore.QObject()
        def refresh_bar(ls):
            ls = eval(ls)
            num = ls[0]
            schedule = ls[1]
            if num == 1:
                self.progressBar.setValue(schedule)
            elif num == 2:
                self.progressBar_2.setValue(schedule)
            else:
                self.progressBar_3.setValue(schedule)
            return None
        self.obj_prBar.objectNameChanged.connect(refresh_bar)

    def obj_img(self):
        self.obj_image = QtCore.QObject()
        def change_img(img):
            self.label_8.setPixmap(QtGui.QPixmap(img))
        self.obj_image.objectNameChanged.connect(change_img)

    def obj_str(self):
        self.obj_string = QtCore.QObject()
        def output(string):
            self.textEdit.append(string)
        self.obj_string.objectNameChanged.connect(output)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/图.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(521, 501, 72, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(521, 471, 72, 16))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(600, 501, 116, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(600, 471, 116, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(521, 441, 72, 16))
        self.label_3.setObjectName("label_3")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(600, 441, 116, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 400, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(490, 0, 20, 551))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(510, 10, 281, 391))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 271, 391))
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("graphicsView")
        self.label_8.setScaledContents(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 197, 401))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 18, 181, 371))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(70, 470, 351, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setEnabled(True)
        self.menu_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.menu_2.setSeparatorsCollapsible(False)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.label_4.setBuddy(self.lineEdit)
        self.label_5.setBuddy(self.lineEdit_2)
        self.label_6.setBuddy(self.lineEdit_3)
        self.label_7.setBuddy(self.lineEdit_4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 页面标题
        MainWindow.setWindowTitle(_translate("MainWindow", "秀人"))
        # 进度条文本
        self.label.setText(_translate("MainWindow", "下载进度："))
        self.label_2.setText(_translate("MainWindow", "获取进度："))
        self.label_3.setText(_translate("MainWindow", "总进度："))
        # 设置选项
        self.groupBox.setTitle(_translate("MainWindow", "参数"))
        self.label_4.setText(_translate("MainWindow", "Host:"))
        self.label_5.setText(_translate("MainWindow", "Search_url:"))
        self.label_6.setText(_translate("MainWindow", "Keywd:"))
        self.label_7.setText(_translate("MainWindow", "Path:"))
        # 按钮文本
        self.pushButton_3.setText(_translate("MainWindow", "恢复"))
        self.pushButton_4.setText(_translate("MainWindow", "修改"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        # 文本框默认值
        self.lineEdit.setText(self.host)
        self.lineEdit_2.setText(self.search_url)
        self.lineEdit_3.setText(self.keywd)
        self.lineEdit_4.setText(self.save_pt)
        # 按钮功能
        self.pushButton_4.clicked.connect(self.XiuGai)
        self.pushButton_3.clicked.connect(self.HuiFu)
        self.pushButton.clicked.connect(self.Start)
        self.pushButton.clicked.connect(self.gone)
        self.pushButton_2.clicked.connect(self.TingZhi)

    def HuiFu(self):
        """文本框恢复默认值"""
        self.lineEdit.setText(self.host)
        self.lineEdit_2.setText(self.search_url)
        self.lineEdit_3.setText('王心怡')
        self.lineEdit_4.setText(self.save_pt)

    def XiuGai(self):
        """确认更改文本框内容"""
        self.host = self.lineEdit.text()
        self.search_url = self.lineEdit_2.text()
        self.keywd = self.lineEdit_3.text()
        self.save_pt = self.lineEdit_4.text()

    def iprocessing(self, num, l, ls):
        item_num = len(ls) / 100
        schedule = int((ls.index(l) + 1) / item_num)
        role = [num, schedule]
        self.obj_prBar.setObjectName(str(role))

    def TingZhi(self):
        """退出程序"""
        app = QtWidgets.QApplication.instance()
        app.quit()

    def Start(self):
        thread = Thread(target=self.main)
        thread.setDaemon(True)
        thread.start()

    def main(self):
        # self.textEdit.append(f"开始搜索: {self.keywd}...")
        self.obj_string.setObjectName(f"开始搜索: {self.keywd}...")
        soup = self.get_soup(url=self.search_url, params={"keyword": self.keywd})
        works = self.get_all_works(soup=soup)
        self.progressBar_3.setValue(0)
        for work in works:
            self.iprocessing(num=3, l=work, ls=works)
            result = self.get_work_dict(url=work)
            self.downloads(work=result)

    def get_soup(self, url, headers=headers(), params={}):
        """获取网页美丽汤"""
        while True:
            try:
                resp = requests.get(url=url, headers=headers, params=params, timeout=30)
                resp.encoding = resp.apparent_encoding
                soup = BeautifulSoup(resp.text, "lxml")
                # time.sleep(2)
                break
            except:
                continue
        return soup

    def get_content(self, url):
        """获取网络文件byte数据"""
        while True:
            try:
                resp = requests.get(url=url, headers=headers(), timeout=30)
                content = resp.content
                time.sleep(2)
                break
            except:
                continue
        return content

    def get_works(self, soup):
        """获取单页上的所有搜索结果"""
        result = []
        works = soup.select(".sousuo")
        for work in works:
            res = work.a.attrs["href"]
            result.append(res)
        return result

    def get_all_works(self, soup):
        """获取所有搜索结果"""
        result = []
        page_num = len(soup.select(".page")[0].find_all(name="a")) - 1
        # self.textEdit.append(f"搜索结果共计{page_num}页...")
        self.obj_string.setObjectName(f"搜索结果共计{page_num}页...")
        ls = [i for i in range(1, page_num + 1)]
        for l in ls:
            # self.textEdit.append(f"正在获取第{l}页结果...")
            self.obj_string.setObjectName(f"正在获取第{l}页结果...")
            params = {"keyword": self.keywd, "p": l}
            soup = self.get_soup(url=self.search_url, params=params)
            result += self.get_works(soup)
        # self.textEdit.append(f"搜索结果获取完成, 共计结果{len(result)}条...")
        self.obj_string.setObjectName(f"搜索结果获取完成, 共计结果{len(result)}条...")
        return result

    def get_path(self, path):
        """创建文件夹并返回路径"""
        for i in path.split("/"):
            try:
                if not os.path.exists(path=path):
                    os.mkdir(path)
                    break
            except:
                pt = "/".join(path.split("/")[:-1])
                self.get_path(path=pt)
                continue
        return path

    def get_work_dict(self, url):
        """获取所有搜索结果相关信息组成字典"""
        soup = self.get_soup(url=self.host + url)
        title = soup.h1.get_text()
        intro = soup.select(".jianjie")[0].get_text()
        try:
            date = re.search("\d{4}\.\d{1,2}\.\d{1,2}", intro).group()
        except:
            date = None
        page_num = len(soup.select(".page")[0].find_all("a")) - 2
        # self.textEdit.append(f"共计{page_num}页...")
        # self.obj_string.setObjectName(f"共计{page_num}页...")
        pics = self.get_pics(url=url, page_num=page_num)
        return {"title": title, "date": date, "pics": pics}

    def get_pics(self, url, page_num):
        """获取单一作品的所有图片url"""
        result = []
        urls = [url] + [f"{url[:-5]}_{num}.html" for num in range(1, page_num)]
        self.progressBar_2.setValue(0)
        for u in urls:
            print(f"获取第{urls.index(u)+1}页图片...")
            soup = self.get_soup(url=self.host + u)
            imgs = soup.select(".content")[1].find_all("img")
            for img in imgs:
                result.append(img.attrs["src"])
            self.iprocessing(num=2, l=u, ls=urls)
        return result

    def downloads(self, work):
        """通过结果字典, 下载图片"""
        title = work["title"]
        # self.textEdit.append(f'开始下载"{title}"...')
        self.obj_string.setObjectName(f'开始下载"{title}"...')
        pics = work["pics"]
        pt = self.get_path(path=f"{self.save_pt}/{self.keywd}/{title}")
        self.progressBar.setValue(0)
        for pic in pics:
            print(f"下载进度: {pics.index(pic)}/{len(pics)}...")
            content = self.get_content(url=self.host + pic)
            pic_name = "%s/%04d.jpg" % (pt, pics.index(pic) + 1)
            with open(pic_name, "wb") as f:
                f.write(content)
            if pics.index(pic) == 0:
                # self.label_8.setPixmap(QtGui.QPixmap(pic_name))
                self.obj_image.setObjectName(pic_name)
            self.iprocessing(num=1, l=pic, ls=pics)
        return None
