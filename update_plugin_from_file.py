from os import system
import platform
import glob
import os
from pathlib import Path

def find_plugin_files(os_type):
    if(os_type == 1):  # Linux
        downloads_path = str(Path.home() / "Downloads")
    elif(os_type == 2):  # Windows
        downloads_path = str(Path.home() / "Downloads")
    
    pattern = os.path.join(downloads_path, "all-*.tar")
    return glob.glob(pattern)

def update_nessus_plugins_from_file(os_type, plugin_files):
    if(os_type == 1):  # Linux
        for plugin_file in plugin_files:
            system(f"/opt/nessus/sbin/nessuscli update {plugin_file}")
        print("Nessus Plugins Updated Successfully")
    elif(os_type == 2):  # Windows
        for plugin_file in plugin_files:
            system(f'"C:\\Program Files\\Tenable\\Nessus\\nessuscli.exe" update "{plugin_file}"')
        print("Nessus Plugins Updated Successfully")

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
    os_type = detect_os()
    plugin_files = find_plugin_files(os_type)
    print(plugin_files)
    update_nessus_plugins_from_file(os_type, plugin_files)

if __name__ == "__main__":
    main()