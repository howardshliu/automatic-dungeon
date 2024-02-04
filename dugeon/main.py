
# coding: utf-8


from sys import argv, exit
from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication,QDialog, QMessageBox, QWidget, QTextEdit
from PyQt5.QtGui import QTextCursor
from PyQt5.uic import loadUi
import paradise
from time import time, sleep
from logging import Handler, warning, WARNING, Formatter, getLogger

    
class MyNewHandler(Handler):
    write = None
    def __init__(self, write_method):
        Handler.__init__(self)
        self.write = write_method

    def emit(self, record):
        self.write(record.message + "\r\n")
        
#調整視窗
class adjust(QWidget):
    
    def __init__(self):
        super(adjust, self).__init__()
        self.window = loadUi('icon\\adjust.ui',self)
        self.setWindowTitle('調整')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

class Life2Coding(QDialog):
   
    def __init__(self):
        super(Life2Coding, self).__init__()
        self.window = loadUi('icon\\autodugeon.ui',self)
        self.setWindowTitle('自動副本小助手-70級')
        #logging顯示在對話框中
        self.edit = self.window.findChild(QTextEdit, 'out_log')
        self.out = None

        #按鈕signal
        self.testall.clicked.connect(self.testall_clicked)#函數不加on 因會與ui原生c++語言重疊 slot會做兩次動作
        self.initial_prepare.clicked.connect(self.initial_prepare_clicked)
        self.screen_adjust.clicked.connect(self.screen_adjust_clicked)
        
    def write(self, m):  # 添加並寫入資料
        self.edit.moveCursor(QTextCursor.End)
        self.edit.insertPlainText(m)
        if self.out:
            self.out.write(m)
            
    @pyqtSlot()
    def testall_clicked(self):
        warning('開始自動打副本')
        QApplication.processEvents()
        sleep(1)
        self.button_control_off()
        start = time()
        try:
            while True:
                QApplication.processEvents()
                if paradise.standby() == 1:
                    a = paradise.judge()
                    if a == 2:
                        warning('第2個試煉進行中')
                        QApplication.processEvents()
                        paradise.second_test()
                        warning('第2個試煉結束!')
                    elif a == 4:
                        warning('第4個試煉進行中')
                        QApplication.processEvents()
                        paradise.forth_test()
                        warning('第4個試煉結束!')
                    elif a == 5:
                        warning('第5個試煉進行中')
                        QApplication.processEvents()
                        paradise.fifth_test()
                        warning('第5個試煉結束!')
                    elif a == 6:
                        warning('第6個試煉進行中')
                        QApplication.processEvents()
                        paradise.sixth_test()
                        warning('第6個試煉結束!')
                    elif a == 7:
                        warning('第7個試煉進行中')
                        QApplication.processEvents()
                        paradise.seventh_test()
                        warning('第7個試煉結束!')
                    elif a == 8:
                        warning('第8個試煉進行中')
                        QApplication.processEvents()
                        paradise.eigth_test()
                        warning('第8個試煉結束!')
                    elif a == 9:
                        warning('第9個試煉進行中')
                        QApplication.processEvents()
                        paradise.ninth_test()
                        warning('第9個試煉結束!')
                        break
                    else:
                        warning('無法進入地監，請退出地監或在安全區域再執行一次')
                        QApplication.processEvents()
                        break
                else:
                    break
            end =  time()
            warning('結束! 用了%.f分%.f秒' % ((end-start)%3600//60,(end-start)%60))
            self.button_control_on()
                    
        except:
            warning('強制中止程式')
        self.button_control_on()
    
    def initial_prepare_clicked(self):
        if paradise.initial_test() == 1:
            receive = QMessageBox.information(self,' ','OK  可以開始打了唷', QMessageBox.Ok)
            self.button_control_on()
        else:
            receive = QMessageBox.warning(self,' ','***請在安全區域中執行***\n***請在快捷鍵擺順捲(盡量20張以上)***\n不要擋到模擬器以免影響偵測\n若已經都好了還偵測不到請移動一下位置', QMessageBox.Ok)
    
    def screen_adjust_clicked(self):
        adjust().show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '離開', '打爽了嗎？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.closeAllWindows()
        else:
            event.ignore()
            
    def button_control_on(self):
        self.testall.setEnabled(True)
        self.initial_prepare.setEnabled(True)
        self.screen_adjust.setEnabled(True)
        
    def button_control_off(self):
        self.testall.setEnabled(False)
        self.initial_prepare.setEnabled(False)
        self.screen_adjust.setEnabled(False)
        
if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(argv)
    aaa = Life2Coding()
    console = MyNewHandler(aaa.write)# 建立MyNewHandler對象，並把剛剛Life2Coding裡面的write 方法傳入
    console.setLevel(WARNING)# 定義只有 WARNING的訊息會輸出出來
    formatter = Formatter('%(asctime)s.%(msecs)03d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S') 
    console.setFormatter(formatter)
    getLogger('').addHandler(console) # logging加入剛剛我們自定義的 handler\
    #aaa.setWindowFlags(Qt.WindowStaysOnTopHint) #永遠顯示在螢幕最上層
    aaa.show()
    exit(app.exec_())
