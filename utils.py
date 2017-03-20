import win32gui

import win32process

from pymixer import AudioUtilities


def get_audio_sessions():
    sessions = {}
    for s in AudioUtilities.GetAllSessions():
        if s.Process:
            sessions[s.ProcessId] = s
    return sessions


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds