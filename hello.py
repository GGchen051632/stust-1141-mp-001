import platform

def get_sys_info():
    print("System:", platform.system())
    print("Version:", platform.version())
    print("Machine:", platform.machine())

if __name__ == "__main__":
    print("Hello, World! (Python version)")
    get_sys_info()

