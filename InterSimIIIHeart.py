# -*- coding: utf-8 -*-
import sys
import time
import keyboard
from PyQt5.QtCore import QTranslator
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from pywinauto import mouse
from pywinauto.application import Application
import Icd_UI
from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor
from PyQt5.QtWidgets import QDialog, QApplication, QComboBox, QMessageBox, QFileDialog, \
    QTableWidget, QTableWidgetItem, QLineEdit, QHeaderView, QSplashScreen, QLabel, QVBoxLayout, QCheckBox, \
    QMenu, QAction
import psutil
import subprocess
from datetime import datetime
import os
# import Displaytkintesr
import re



Userfiles_PATH = "D:/Users/wangchengcheng/Documents/IBLang/InterSimIII/Userfiles/"
DefiEvent_DATA = time.strftime('%Y%m%d%H%M%S')
DefiEvent_PATH = r"D:\Users\wangchengcheng\Documents\IBLang\InterSimIII\Userfiles\DefiLog.iuf"
TEST_PATH = "D:/Users/wangchengcheng/Documents/IBLang/InterSimIII/Userfiles/"

PACEEvent_PATH = r"D:\Users\wangchengcheng\Documents\IBLang\InterSimIII\Userfiles\PaceLog.iuf"
SENSEvent_PATH = r"D:\Users\wangchengcheng\Documents\IBLang\InterSimIII\Userfiles\SenseLog.iuf"



class MainDialog(QMainWindow, Icd_UI.Ui_MainWindow):
    _filePath = None

    # 程序初始化
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)

        try:
           app = Application(backend="uia").start("D:\Program Files (x86)\IBLang\InterSimIII\InterSimIII.Desktop.exe")
           # app = Application().connect(path="D:\Program Files (x86)\IBLang\InterSimIII\InterSimIII.Desktop.exe")
           dlg = app.TMainForm
        except:
               QMessageBox.critical(self, self.tr('Error'),
                                 self.tr('InterSimIII software not found!'),
                                 QMessageBox.Ok, QMessageBox.Ok)
        # dlg = app.window(class_name="TMainForm")
        self.setWindowIcon(QIcon(r'res\Icon.ico'))
        self.trans = QTranslator()
        language_file = r'zh_CN.qm'
        self.trans.load(language_file)
        _app = QApplication.instance()
        _app.installTranslator(self.trans)
        self.retranslateUi(self)


        self.pushButton_Reset.clicked.connect(self.set_rest)
        self.pushButton_VentricularFibrillationCoarse.clicked.connect(self.set_ventricularfibrillationcoarse)
        self.pushButton_RVSlow.clicked.connect(self.set_rvslow)
        self.pushButton_RVMedium.clicked.connect(self.set_rvmedium)
        self.pushButton_RVFast.clicked.connect(self.set_rvfast)
        self.pushButton_Ventricle.clicked.connect(self.set_ventricle)
        self.comboBox_Tip_Condition.activated.connect(self.set_tip_condition)
        self.comboBox_Threshold.activated.connect(self.set_threshold)
        self.pushButton_set_time.clicked.connect(self.set_time)
        self.pushButton_Buzzer.clicked.connect(self.set_time)
        self.pushButton_Electrophysiological_fibrillation.clicked.connect(self.set_electrophysiological_fibrillation)
        self.pushButton_magnet_VF.clicked.connect(self.set_time)
        self.pushButton_magnet_vt.clicked.connect(self.set_magnet_reaction)

        self.pushButton_Emergency_defibrillation.clicked.connect(self.set_emergency_defibrillation)
        self.pushButton_Emergency_pacing.clicked.connect(self.set_emergency_pacing)
        self.pushButton_shutdown.clicked.connect(self.set_emergency_pacing)
        self.pushButton_Ventricular_Vf.clicked.connect(self.set_time)
        self.pushButton_rate.clicked.connect(self.set_rate)

        self.pushButton_Svt_vt.clicked.connect(self.set_magnet_reaction)
        self.pushButton_Svt_AF.clicked.connect(self.set_svt_atrialFibrillation)
        self.pushButton_Svt_Sinus_velocity.clicked.connect(self.set_svt_sinus)

        self.pushButton_Detection_mode_vf.clicked.connect(self.set_time)
        self.pushButton_Detection_mode_vt.clicked.connect(self.set_magnet_reaction)
        self.pushButton_Detection_mode_fvt.clicked.connect(self.set_detection_mode_fvt)

        self.pushButton_shock_pacing.clicked.connect(self.set_shock_pacing)

        self.pushButton__Frequency_lag_1.clicked.connect(self.set_frequency_lag_1)
        self.pushButton_Frequency_lag_2.clicked.connect(self.set_frequency_lag_2)
        self.pushButton_Frequency_lag_3.clicked.connect(self.set_frequency_lag_3)

        self.pushButton_Asynchronous_shock.clicked.connect(self.set_magnet_reaction)
        self.pushButton_ATP_therapy.clicked.connect(self.set_magnet_reaction)
        self.pushButton_VT_Shock_One.clicked.connect(self.set_magnet_reaction)

        self.pushButton_VT_Shock_Two.clicked.connect(self.set_vt_shock_two)
        self.pushButton_VT_Shock_Five.clicked.connect(self.set_vt_shock_five)
        self.pushButton_VT_Shock_Six.clicked.connect(self.set_vt_shock_five)

        self.pushButton_VF_Shock_One.clicked.connect(self.set_time)
        self.pushButton_VF_Shock_Two.clicked.connect(self.set_vf_shock_two)
        self.pushButton_VF_Shock_Six.clicked.connect(self.set_vf_shock_six)

        self.pushButton_VT_FVT_VF.clicked.connect(self.set_vt_fvt_vf)
        self.pushButton_VF_FVT_VT.clicked.connect(self.set_vf_fvt_vt)
        self.pushButton_VT_VF.clicked.connect(self.set_vt_vf)
        self.pushButton_VF_VT.clicked.connect(self.set_vf_vt)
        self.pushButton_VT_FVT.clicked.connect(self.set_vt_fvt)
        self.pushButton_FVT_VT.clicked.connect(self.set_fvt_vt)
        self.pushButton_VT_ATP_FVT.clicked.connect(self.set_vt_atp_fvt)
        self.pushButton_FVT_ATP_VT.clicked.connect(self.set_fvt_atp_vt)

        self.pushButton_OS_STB_phase.clicked.connect(self.set_os_stb_phase)
        self.pushButton_Template_phase.clicked.connect(self.set_os_stb_phase)
        self.pushButton_Algorithmless_phase.clicked.connect(self.set_algorithmless_phase)

        self.pushButton_No_persistent_even.clicked.connect(self.set_no_persistent_even)
        self.pushButton_AF_even.clicked.connect(self.set_af_even)
        self.pushButton_frequencylag_data.clicked.connect(self.set_frequencylag_even)

        self.pushButton_vt_detection_1.clicked.connect(self.set_vt_detection_1)
        self.pushButton_vt_detection_2.clicked.connect(self.set_vt_detection_2)
        self.pushButton_vt_detection_3.clicked.connect(self.set_vt_detection_3)
        self.pushButton_vt_detection_4.clicked.connect(self.set_vt_detection_4)




    #重名名文件名称
    def add_timestamp_to_filename(self,filename):
        # 获取当前时间
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)

        # 添加时间戳并组合为新的文件名
        new_filename = f"{name}_{timestamp}{ext}"
        return new_filename

    def rename_file_with_timestamp(self,file_path):
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"文件不存在：{file_path}")
            return

        # 获取文件所在的目录和文件名
        directory = os.path.dirname(file_path)
        basename = os.path.basename(file_path)

        # 添加时间戳到文件名
        new_basename = self.add_timestamp_to_filename(basename)

        # 构建新的路径
        new_file_path = os.path.join(directory, new_basename)

        # 重命名文件
        os.rename(file_path, new_file_path)

    #判断日志中电击的值
    def compare_text_file_numbers_shock(self,filename, expected_ranges):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            numbers = set()  # 使用集合存储去重后的小数值
            for i, line in enumerate(lines, 1):
                number = re.search(r'\d+\.\d+', line)

                # 使用正则表达式匹配当前行中的所有数字
                if number is not None:
                    value = float(number.group())  # 将匹配到的小数转换为浮点数
                    numbers.add(value)  # 将小数值添加到集合中
            numbers_list = sorted(list(numbers))  #
            # print(numbers_list)
            # 检查每个数字是否在期望的范围内
            for i, number in enumerate(numbers_list, 1):
                if i in expected_ranges:
                    expected_range = expected_ranges[i]
                    if number < expected_range[0] or number > expected_range[1]:
                        # print(f"第 {i} 行的小数不在期望的范围内")
                        return False

            return True

        except FileNotFoundError:
            return False

    # 判断日志中起搏信息的值是否在范围之内
    # 起搏信息正则表达
    def pace_test_standard(self,filename, expected_pattern, voltage_range, time_range):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            for line in lines:
                match = re.search(expected_pattern, line)
                if not match:
                    return False

                voltage = float(match.group(1))  # values = match.group().split('--')
                time = float(match.group(2))  # voltage = float(re.findall(r'\d+\.\d+', values[0])[0])
                # timetime = float(re.findall(r'\d+\.\d+', values[1])[0])
                if not (voltage_range[0] <= voltage <= voltage_range[1] and
                        time_range[0] <= time <= time_range[1]):
                    return False

            return True

        except FileNotFoundError:
            return False

     #测试完成后读取文件
    def set_read_file(self, filename):
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                lines = file.read()
            return lines
        except :
            QMessageBox.critical(self, self.tr('Error'),
                               self.tr('DefiEvent file not found!'),
                                        QMessageBox.Ok, QMessageBox.Ok)
    #读取文件时去重处理
    def set_show_unique_content(self,content):
         lines = content.split('\n')
         unique_lines = set(lines)
         unique_content = '\n'.join(unique_lines)
         return unique_content

    # ICD时间同步
    def set_time(self):
        self.rename_file_with_timestamp(DefiEvent_PATH)
        self.rename_file_with_timestamp(PACEEvent_PATH)
        self.rename_file_with_timestamp(SENSEvent_PATH)
        self.set_run()
        name_time = "TM-01-10260"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
        time.sleep(30)
        file_content = self.set_read_file(DefiEvent_PATH)
        file_unique_content = self.set_show_unique_content(file_content)
        self.textEdit_read.setPlainText(file_unique_content)
        expected_ranges = {
            1: (3.0, 5.0),
            2: (12.0, 20.0)
        }
        result = self.compare_text_file_numbers_shock(DefiEvent_PATH, expected_ranges)
        self.textEdit_read_shock_result.setPlainText(str(result))


        file_content_pace = self.set_read_file(PACEEvent_PATH)
        file_unique_content_pace = self.set_show_unique_content(file_content_pace)
        self.textEdit_read_2.setPlainText(file_unique_content_pace)
        #程控仪起搏参数设置
        expected_pattern = r'RVTip--RVRing\*\*\*\*(\d+\.\d+)V\*\*\*\*(\d+\.\d+)ms'
        voltage_range = (5.7, 6.3)
        time_range = (1.2, 1.8)
        #测试结果判断
        result = self.pace_test_standard(PACEEvent_PATH, expected_pattern, voltage_range, time_range)
        self.textEdit_read_pace_result.setPlainText(str(result))




    # 电生理诱颤
    def set_electrophysiological_fibrillation(self):
        self.set_run()
        name_time = "TM-01-10264"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # 磁铁反应
    def set_magnet_reaction(self):
        self.set_run()
        name_time = "TM-01-10261"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    #紧急除颤
    def set_emergency_defibrillation(self):
        self.set_run()
        name_time = "TM-01-10265"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    #紧急治疗
    def set_emergency_pacing(self):
        self.set_run()
        name_time = "TM-01-10265-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # 设置除颤阈值

    def set_rate(self):
        time.sleep(1)
        mouse.click(button="left", coords=(103, 36))
        time.sleep(0.5)
        mouse.click(button="left", coords=(114, 133))
        time.sleep(0.5)
        mouse.click(button="left", coords=(1041, 47))
        time.sleep(0.5)
        keyboard.send('ctrl+a+del')
        time.sleep(1)
        rate_number = self.lineEdit_set_rate.text().strip()
        time.sleep(1)
        keyboard.write(rate_number)
        time.sleep(1)
        mouse.click(button="left", coords=(951, 651))


    # svt房颤
    def set_svt_atrialFibrillation(self):
        self.set_run()
        name_time = "TM-01-10307-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # svt窦速
    def set_svt_sinus(self):
        self.set_run()
        name_time = "TM-01-10307-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # 心动过速检测模式fvt
    def set_detection_mode_fvt(self):
        self.set_run()
        name_time = "TM-01-10270"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # 电击后起搏
    def set_shock_pacing(self):
        self.set_run()
        name_time = "TM-01-10269"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # 频率滞后
    def set_frequency_lag_1(self):
        self.set_run()
        name_time = "TM-01-10267-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    # 频率滞后
    def set_frequency_lag_2(self):
        self.set_run()
        name_time = "TM-01-10267-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    # 频率滞后
    def set_frequency_lag_3(self):
        self.set_run()
        name_time = "TM-01-10267-03"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    #VT电击次数2次
    def set_vt_shock_two(self):
        self.set_run()
        name_time = "TM-01-10330-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # VT电击次数2次以上
    def set_vt_shock_five(self):
        self.set_run()
        name_time = "TM-01-10330-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # VF电击次数2次
    def set_vf_shock_two(self):
        self.set_run()
        name_time = "TM-01-10271-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

     # VF电击次数2次以上
    def set_vf_shock_six(self):
        self.set_run()
        name_time = "TM-01-10271-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

     # 跨区治疗
    def set_vt_fvt_vf(self):
        self.set_run()
        name_time = "TM-01-10411-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vf_fvt_vt(self):
        self.set_run()
        name_time = "TM-01-10411-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_vf(self):
        self.set_run()
        name_time = "TM-01-10411-03"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vf_vt(self):
        self.set_run()
        name_time = "TM-01-10411-04"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_fvt(self):
        self.set_run()
        name_time = "TM-01-10411-05"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_atp_fvt(self):
        self.set_run()
        name_time = "TM-01-10411-06"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_fvt_vt(self):
        self.set_run()
        name_time = "TM-01-10411-07"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_fvt_atp_vt(self):
        self.set_run()
        name_time = "TM-01-10411-08"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    # SVT鉴别可用阶段
    def set_os_stb_phase(self):
        self.set_run()
        name_time = "TM-01-10343-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    def set_algorithmless_phase(self):
        self.set_run()
        name_time = "TM-01-10343-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')

    #临床数据存储
    def set_no_persistent_even(self):
        # self.set_subprocess()
        self.set_run()
        name_time = "TM-01-10346-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_af_even(self):
        self.set_run()
        name_time = "TM-01-10346-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_frequencylag_even(self):
        self.set_run()
        name_time = "TM-01-10346-03"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    # VT检测
    def set_vt_detection_1(self):
        self.set_run()
        name_time = "TM-01-10322-01"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_detection_2(self):
        self.set_run()
        name_time = "TM-01-10322-02"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_detection_3(self):
        self.set_run()
        name_time = "TM-01-10322-03"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    def set_vt_detection_4(self):
        self.set_run()
        name_time = "TM-01-10322-04"
        keyboard.write(name_time)
        time.sleep(0.5)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.send('ctrl+m')
    # 程控定位到路径
    def set_run(self):
        time.sleep(0.5)
        mouse.click(button="left", coords=(389, 40))
        mouse.click(button="left", coords=(447, 98))
        time.sleep(1)

     # 心律重置
    def set_rest(self):
        time.sleep(1)
        mouse.click(button="left", coords=(103, 36))
        time.sleep(1)
        mouse.click(button="left", coords=(95, 70))

    # 设置室颤
    def set_ventricularfibrillationcoarse(self):
        time.sleep(1)
        mouse.click(button="left", coords=(172, 36))
        time.sleep(0.5)
        mouse.click(button="left", coords=(377, 531))
        time.sleep(0.5)
        mouse.click(button="left", coords=(684, 541))

    # 设置心动过速slow
    def set_rvslow(self):
        time.sleep(1)
        mouse.click(button="left", coords=(172, 36))
        time.sleep(0.5)
        mouse.click(button="left", coords=(281, 419))
        time.sleep(0.5)
        mouse.click(button="left", coords=(676, 416))

    # 设置心动过速Medium
    def set_rvmedium(self):
        time.sleep(1)
        mouse.click(button="left", coords=(172, 36))
        time.sleep(0.5)
        mouse.click(button="left", coords=(281, 419))
        time.sleep(0.5)
        mouse.click(button="left", coords=(659, 450))

    # 设置心动过速Fast
    def set_rvfast(self):
        time.sleep(1)
        mouse.click(button="left", coords=(172, 36))
        time.sleep(0.5)
        mouse.click(button="left", coords=(281, 419))
        time.sleep(0.5)
        mouse.click(button="left", coords=(690, 449))

    # 设置除颤阈值
    def set_ventricle(self):
        time.sleep(1)
        mouse.click(button="left", coords=(329, 39))
        time.sleep(0.5)
        mouse.click(button="left", coords=(361, 120))
        time.sleep(0.5)
        mouse.click(button="left", coords=(1081, 408))
        time.sleep(0.5)
        keyboard.send('ctrl+a+del')
        ventricle_number = self.lineEdit.text().strip()
        keyboard.write(ventricle_number)
        time.sleep(0.5)
        mouse.click(button="left", coords=(1137, 694))
        time.sleep(0.5)
        mouse.click(button="left", coords=(1235, 682))

    # 设置起搏阻抗
    def set_tip_condition(self):
        time.sleep(1)
        mouse.click(button="left", coords=(329, 39))
        time.sleep(0.5)
        mouse.click(button="left", coords=(386, 67))
        time.sleep(0.5)
        mouse.click(button="left", coords=(964, 571))
        time.sleep(2)
        current_text = self.comboBox_Tip_Condition.currentIndex()
        # print(current_text)
        if current_text == 1:
            mouse.click(button="left", coords=(965, 610))
        # else:
        #     print(current_text + 1)
        if current_text == 2:
            mouse.click(button="left", coords=(973, 628))
        # else:
        #     print(current_text + 2)
        if current_text == 3:
            mouse.click(button="left", coords=(951, 641))
        # else:
        #     print(current_text + 3)
        if current_text == 0:
            mouse.click(button="left", coords=(953, 591))
        # else:
        #     print(current_text + 4)
        mouse.click(button="left", coords=(973, 628))
        time.sleep(2)
        mouse.click(button="left", coords=(1240, 792))
        time.sleep(0.5)
        mouse.click(button="left", coords=(1336, 791))

    # 设置起搏阈值
    def set_threshold(self):
        time.sleep(3)
        mouse.click(button="left", coords=(329, 39))
        time.sleep(0.5)
        mouse.click(button="left", coords=(386, 67))
        time.sleep(0.5)
        mouse.click(button="left", coords=(723, 651))
        time.sleep(0.5)
        current_text = self.comboBox_Threshold.currentIndex()
        print(current_text)
        if current_text == 0:
            mouse.scroll(coords=(760, 714), wheel_dist=3)
            time.sleep(1)
            mouse.click(button="left", coords=(700, 671))
        else:
            print(current_text)
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainDialog()
    win.show()
    sys.exit(app.exec_())
    # os.system("pause")
    # 语言翻译 pylupdate5 Icd_UI.py -ts en.ts

    # pyinstaller -w --clean -i res\Icon.ico --noconfirm --distpath E:\PackPython -D InterSimIIIHeart.py --name " InterSimn Tool" -p D:\PycharmProjects\pythonProject  --add-data=".\*qm;."



