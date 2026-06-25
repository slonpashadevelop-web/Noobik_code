import os
import subprocess
import winreg

print("=== ДИАГНОСТИКА STEAM ===\n")

# Проверка стандартных путей
paths = [
    r"C:\Program Files\Steam\steam.exe",
    r"C:\Program Files (x86)\Steam\steam.exe",
]

print("Проверка стандартных путей:")
for path in paths:
    exists = os.path.exists(path)
    print(f"  {'✓' if exists else '✗'} {path}")

# Проверка реестра
print("\nПроверка реестра Windows:")
try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Valve\Steam") as key:
        steam_path = winreg.QueryValueEx(key, "InstallPath")[0]
        steam_exe = os.path.join(steam_path, "steam.exe")
        exists = os.path.exists(steam_exe)
        print(f"  {'✓' if exists else '✗'} {steam_exe}")
except Exception as e:
    print(f"  ✗ Реестр не доступен: {e}")

# Проверка переменных окружения
print("\nПеременные окружения:")
print(f"  ProgramFiles: {os.environ.get('ProgramFiles', 'не установлена')}")
print(f"  ProgramFiles(x86): {os.environ.get('ProgramFiles(x86)', 'не установлена')}")

# Попытка запустить через os.startfile
print("\nПопытка запуска steam://run/570 через os.startfile()...")
try:
    os.startfile("steam://run/570")
    print("  ✓ Запущено успешно!")
except Exception as e:
    print(f"  ✗ Ошибка: {e}")

print("\n=== КОНЕЦ ДИАГНОСТИКИ ===")
