import ctypes
import win32con
from wx.lib.activex import user32

WinEventProcType = ctypes.WINFUNCTYPE(
    None,
    ctypes.wintypes.HANDLE,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.HWND,
    ctypes.wintypes.LONG,
    ctypes.wintypes.LONG,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD
)


def callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
    length = user32.GetWindowTextLengthA(hwnd)
    buff = ctypes.create_string_buffer(length + 1)
    user32.GetWindowTextA(hwnd, buff, length + 1)
    print(buff.value)


class Hook:
    def __init__(self, cb):
        self.cb = cb if cb else callback
        WinEventProc = WinEventProcType(self.cb)
        user32.SetWinEventHook.restype = ctypes.wintypes.HANDLE
        hook = user32.SetWinEventHook(
            win32con.EVENT_OBJECT_FOCUS,
            win32con.EVENT_OBJECT_FOCUS,
            0,
            WinEventProc,
            0,
            0,
            win32con.WINEVENT_OUTOFCONTEXT
        )
        msg = ctypes.wintypes.MSG()
        while user32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
            # user32.TranslateMessageW(msg)
            user32.DispatchMessageW(msg)

        user32.UnhookWinEvent(hook)
        user32.CoUninitialize()

    def on(self, cb):
        self.cb = cb
