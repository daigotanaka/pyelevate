pyelevate
=========

Executes a shell command with an elevated rights on Windows Vista, Windows 7

Examples
---------

This example give an exception to Windows Firewall on Port 6701:

    python elevate.py netsh firewall add portopening 6701 Exception_port_6701
    
It can also be imported in other python program, of course:

    import elevate
    
    elevate("netsh", "firewall delete portopening 6701")
