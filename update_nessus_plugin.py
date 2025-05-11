from os import system
import platform

def update_nessus_plugins(os):
    if(os == 1):
        system("/opt/nessus/sbin/nessuscli update --plugins-only")
        print("Nessus Updated Successfully")
    elif(os ==2):
        system('"C:\\Program Files\\Tenable\\Nessus\\nessuscli.exe" update --plugins-only')
        print("Nessus Updated Successfully")
def detect_os():
    system = platform.system().lower()
    if system == 'linux':
        return 1
    elif system == 'windows':
        return 2
    else:
        print(f"Unsupported operating system: {system}")
        exit(1)

def main():
    os = detect_os()
    update_nessus_plugins(os)

if __name__ == "__main__":
    main()