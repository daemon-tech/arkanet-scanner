try:
    import os
except ModuleNotFoundError:
    print("PYTHON: Module error: OS")

try:
    import nmap3
except ModuleNotFoundError:
    if os.name == "nt":
        os.system("pip install nmap3")
    else:
        try:
            os.system("python3 -m pip install python3-nmap")
        except:
            close()
try:
    import termcolor
except ModuleNotFoundError:
    if os.name == "nt":
        os.system("pip install termcolor")
    else:
        os.system("python3 -m pip install termcolor")
    
os.system("python3 lib/main.py")