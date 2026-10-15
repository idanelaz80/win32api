import win32gui

"""
עידן אלעז ושני צוקרמן
"""
def win_enum_callback(hwnd, results):
    """
    פעולה שבודקת האם החלון פתוח ויש לו כותרת, ואם כן מכניסה אותו לרשימה resuls
    :param hwnd:
    :param results:
    :return:
    """
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        if title:
            results.append((hwnd, title))
    return True

def get_all_windows():
    """
    פעולה אשר יוצרת רשימה של כל החלונות הפתוחים עם הכותרות
    :return:
    """
    windows_list = []

    win32gui.EnumWindows(win_enum_callback, windows_list)
    return windows_list

#
if __name__ == "__main__":
    all_windows = get_all_windows()
    for hwnd, title in all_windows:
        print(f"Title: {title}")
