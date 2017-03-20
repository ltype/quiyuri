from concurrent.futures import thread

import wx

import config
import hook
import ui
import utils
from pymixer import IID_Empty


def callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
    items = frame.lst.GetItems()
    for k, v in sessions.items():
        hwnds = utils.get_hwnds_for_pid(k)
        mute = v.Process.name() in items and hwnd not in hwnds
        v.SimpleAudioVolume.SetMute(mute, IID_Empty)
        if frame.cb.GetValue() and not mute and v.Process.name() in items:
            for ck, cv in sessions.items():
                cv.SimpleAudioVolume.SetMute(cv.ProcessId != v.ProcessId, IID_Empty)


sessions = utils.get_audio_sessions()
app = wx.App(redirect=False)
frame = ui.Frame(config.title)
frame.refresh_cb(utils.get_audio_sessions())
frame.Show()
thread.ThreadPoolExecutor().submit(hook.Hook(cb=callback))
app.MainLoop()
