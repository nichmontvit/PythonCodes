import winreg

reg_connection = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

reg_key = winreg.OpenKey(reg_connection, r"Software\Microsoft\Windows\CurrentVersion\Explorer\CLSID")

for key in range(3000):
    try:
        print(winreg.EnumKey(reg_key, key))   
    except WindowsError:
        break


winreg.CloseKey(reg_key)
