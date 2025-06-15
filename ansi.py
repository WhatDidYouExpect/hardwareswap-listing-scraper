import os
import sys
import ctypes
import platform

# Thanks to ChatGPT for this lmao

def enable_ansi_windows():
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        new_mode = mode.value | 0x0004
        return kernel32.SetConsoleMode(handle, new_mode) != 0
    except Exception:
        return False

def supports_ansi(vt_enabled):
    if os.name != 'nt':
        return sys.stdout.isatty()
    
    if vt_enabled:
        return True

    return (
        sys.stdout.isatty() and (
            'ANSICON' in os.environ or
            'WT_SESSION' in os.environ or
            os.environ.get('TERM_PROGRAM') == 'vscode' or
            'TERM' in os.environ and 'xterm' in os.environ['TERM']
        )
    )

def ansi_supported():
    vt_enabled = False
    if os.name == 'nt':
        vt_enabled = enable_ansi_windows()
    
    ansi_ok = supports_ansi(vt_enabled)

    if ansi_ok:
        return True
    else:
        return False
