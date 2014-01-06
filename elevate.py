import sys

from win32com.shell import shell
from win32con import SW_HIDE

def elevate(command, param=""):
    """
    Execut a she shell command with elevated rights when the current
    user can have the privilge.

    Deisgned to be used with Windows Vista, 7 and 8.
    It also works on Windows XP although it is not necessary on many
    occasions.

    It may pops User Access Control dialog to confirm the elevation.
    """
    ret = shell.ShellExecuteEx(
        hwnd=None,
        lpVerb="runas",
        lpFile=command,
        lpParameters=param,
        lpDirectory=""
    )
    return ret

if __name__ == "__main__":
    argv = sys.argv
    command = argv[1]
    param = " ".join(argv[2:]) if len(argv) > 1 else None
    elevate(command, param)
