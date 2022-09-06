from pywinauto.application import Application
import pywinauto

#-*-coding:utf-8-*-
# 애플리케이션 모듈 선언
app = pywinauto.application.Application()
app = Application(backend="uia").start('C:\Program Files (x86)\Make\Make.exe')
app.connect(title_re ='Make', class_name='UnityWndClass')
dlg = app['Make']
dlg.set_focus()

# dlg = app.print_control_identifiers()
# windows = app['MakeDialog']
# # window.set_focus()

# 아래 코드는 윈도우 애플리케이션의 상위/하위 정보를 모두 볼 수 있는 코드
app.YourDialog.print_control_identifiers()
