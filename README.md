pyelevate
=========

Executes a shell command with an elevated rights on Windows Vista, Windows 7.
It requires win32com and win32con modules.

Examples
---------

This example give an exception to Windows Firewall on Port 6701:

Windows 7:

    python elevate.py netsh advfirewall firewall add rule name="My_Exception_6701" dir=in action=allow protocol=TCP localport=6701

Windows XP:

    python elevate.py netsh firewall add portopening 6701 My_Exception_port_6701

It can also be imported in other python program, of course:

    import elevate
    
    elevate("netsh", "advfirewall firewall delete rule name="My_Exception_6701" protocol=TCP localport=6701")
    # elevate("netsh", "firewall delete portopening 6701") for Windows XP
