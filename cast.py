import subprocess

proc = subprocess.Popen("netsh interface ip show address Wi-Fi", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ip = proc.stdout.read().decode().replace(" ", "").split("DefaultGateway:")[1].splitlines()[0]
print(ip)
subprocess.Popen(f"./adb tcpip 5555")
proc = subprocess.Popen(f"./scrcpy --tcpip={ip} --fullscreen --no-mouse-hover --push-target=/sdcard/", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)