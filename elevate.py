import sys
import win32event

from win32com.shell import shell


def elevate(command, param="", wait=False):
    """
    Execute a shell command with elevated rights when the current
    user can have the privilge.

    Deisgned to be used with Windows Vista, 7 and 8.
    It also works on Windows XP although it is not necessary on many
    occasions.

    It may pops User Access Control dialog to confirm the elevation.
    """
    dict = shell.ShellExecuteEx(
        fMask=256 + 64,  # SEE_MASK_NOASYNC(0x00000100) + SEE_MASK_NOCLOSEPROCESS(0x00000040)
        hwnd=None,
        lpVerb="runas",
        lpFile=command,
        lpParameters=param,
        lpDirectory=""
    )

    if not wait:
        return dict

    hh = dict["hProcess"]
    ret = win32event.WaitForSingleObject(hh, -1)
    return ret


if __name__ == "__main__":
    argv = sys.argv
    command = argv[1]
    param = " ".join(argv[2:]) if len(argv) > 1 else None
    elevate(command, param)
