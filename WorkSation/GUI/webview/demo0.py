"""
main.py
"""
import webview

window = webview.create_window(
    title='百度一下,全是广告',
    url='http://www.baidu.com',
    width=850,
    height=600,
    resizable=True,    # 固定窗口大小
    text_select=False,   # 禁止选择文字内容
    confirm_close=True   # 关闭时提示
)
webview.start()
