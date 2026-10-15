import win32clipboard
import time


"""
עידן אלעז ושני צוקרמן
"""
last_num = win32clipboard.GetClipboardSequenceNumber()

while True:
    win32clipboard.OpenClipboard()
    current_num = win32clipboard.GetClipboardSequenceNumber()

    if current_num != last_num:
        last_num = current_num
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
            data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
            print(data)
    win32clipboard.CloseClipboard()
    time.sleep(0.1)



