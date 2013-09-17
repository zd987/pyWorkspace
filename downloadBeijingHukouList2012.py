# -*- coding: utf-8 -*-
import spynner
import pyquery
import time
from PyQt4.QtCore import QTextCodec, QTextStream
browser = spynner.Browser()#debug_level=spynner.INFO)
browser.create_webview()
#browser.show()
browser.load("http://www.chrm.gov.cn/Desktop.aspx?PATH=rsrcw/hdyzl/gs_zgbm/gs_jsdw/gs_cx&queryName=&state=query") 
browser.load_jquery(True)
file = open("e:\\aaaresult.txt", "w");
file.write('%d' % 0)
file.write(browser.webframe.toPlainText())
for i in range(1, 1989):
    #browser.load("E:/aa.html")
    #d = pyquery.PyQuery(browser.html)
    #print d.show()
    #\javascript:__doPostBack('_ctl0$_ctl7$_ctl0$_ctl10','')
    #browser.runjs("__doPostBack('_ctl0$_ctl7$_ctl0$_ctl10','')")
    browser.click("a[href=\"javascript:__doPostBack('_ctl0$_ctl7$_ctl0$_ctl10','')\"]", wait_load=True)
    #print browser.webframe.toHtml().toUtf8()
    #browser.browse()
    #file = open("e:\\aa.html", "w");
    #file.write(browser.html)
    #file.close()
    #time.sleep(5)
    print i
    print browser.webframe.toPlainText()
    file.write('%d' % i)
    file.write(browser.webframe.toPlainText())
#browser.browse()
browser.close()
file.close()
