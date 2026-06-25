import keyboard
import subprocess
import time
import pyautogui
import os
import sys
import winreg

class DotaAutoPicker:
    def __init__(self):
        self.dota_process = None
        self.is_running = False
        
    def find_steam_path(self):
        """Найти путь к Steam"""
        steam_paths = [
            r"C:\Program Files\Steam\steam.exe",
            r"C:\Program Files (x86)\Steam\steam.exe",
            os.path.expandvars(r"%ProgramFiles%\Steam\steam.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Steam\steam.exe"),
        ]
        
        # Проверяем реестр Windows
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Valve\Steam") as key:
                steam_path = winreg.QueryValueEx(key, "InstallPath")[0]
                steam_exe = os.path.join(steam_path, "steam.exe")
                steam_paths.insert(0, steam_exe)
                print(f"[*] Из реестра найдено: {steam_exe}")
        except Exception as e:
            print(f"[*] Реестр не доступен: {e}")
        
        print("[*] Проверяемые пути:")
        for path in steam_paths:
            exists = "✓" if os.path.exists(path) else "✗"
            print(f"  {exists} {path}")
        
        for path in steam_paths:
            if os.path.exists(path):
                print(f"[+] Найден Steam: {path}")
                return path
        
        print("[-] Steam не найден ни по одному пути")
        return None
    
    def launch_dota2(self):
        """Запустить Dota 2"""
        try:
            print("[*] Запуск Dota 2...")
            print("[*] Диагностика Steam...")
            
            # Проверяем наличие Steam
            steam_path = self.find_steam_path()
            print(f"[*] Найденный путь Steam: {steam_path}")
            
            dota2_app_id = "570"
            steam_url = f"steam://run/{dota2_app_id}"
            
            print(f"[*] URL для запуска: {steam_url}")
            
            # Метод 1: Попробуем через os.startfile (работает на Windows)
            print("[*] Попытка 1: os.startfile()...")
            try:
                os.startfile(steam_url)
                print("[+] Запущено через os.startfile")
                time.sleep(20)
                print("[+] Dota 2 запущена")
                return True
            except Exception as e1:
                print(f"[-] os.startfile не сработал: {e1}")
            
            # Метод 2: Попробуем через cmd start
            print("[*] Попытка 2: cmd start...")
            try:
                subprocess.Popen(f'cmd /c start {steam_url}', shell=True)
                print("[+] Запущено через cmd start")
                time.sleep(20)
                print("[+] Dota 2 запущена")
                return True
            except Exception as e2:
                print(f"[-] cmd start не сработал: {e2}")
            
            # Метод 3: Если Steam найден, запустим его напрямую
            if steam_path:
                print(f"[*] Попытка 3: Прямой запуск {steam_path} с параметрами...")
                try:
                    subprocess.Popen([steam_path, f"-applaunch {dota2_app_id}"])
                    print("[+] Запущено через прямой вызов steam.exe")
                    time.sleep(20)
                    print("[+] Dota 2 запущена")
                    return True
                except Exception as e3:
                    print(f"[-] Прямой запуск не сработал: {e3}")
            
            print("[-] Все методы запуска не сработали")
            return False
        except Exception as e:
            print(f"[-] Ошибка при запуске Dota 2: {e}")
            import traceback
            traceback.print_exc()
            return False
    def pick_lina(self):
        """Автоматический пик Лины"""
        try:
            print("[*] Ожидание загрузки интерфейса выбора героя...")
            time.sleep(10)
            
            print("[*] Поиск Лины в списке героев...")
            
            # Пытаемся нажать Tab для открытия поиска
            pyautogui.press('tab')
            time.sleep(1)
            
            # Вводим название героя
            pyautogui.typewrite('lina', interval=0.1)
            time.sleep(1)
            
            print("[*] Выбираем Лину...")
            # Нажимаем Enter для выбора первого результата
            pyautogui.press('enter')
            time.sleep(1)
            
            # Подтверждаем выбор
            pyautogui.press('enter')
            time.sleep(1)
            
            print("[+] Лина выбрана!")
            return True
            
        except Exception as e:
            print(f"[-] Ошибка при выборе героя: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def on_delete_pressed(self):
        """Обработчик нажатия Del"""
        print("\n[!] Клавиша Del нажата!")
        print("[*] Запускаю последовательность...")
        
        if self.launch_dota2():
            self.pick_lina()
        else:
            print("[-] Не удалось запустить игру")
    
    def start_listener(self):
        """Начать прослушивание клавиши Del"""
        print("[*] Программа запущена")
        print("[*] Ожидание нажатия клавиши 'Del'...")
        print("[*] Для выхода нажмите Esc\n")
        
        # Регистрируем функцию на нажатие Del
        keyboard.add_hotkey('del', self.on_delete_pressed)
        
        # Слушаем Esc для выхода
        keyboard.wait('esc')
        print("\n[*] Программа завершена")

def main():
    # Проверяем установку необходимых библиотек
    try:
        import pyautogui
        import keyboard
    except ImportError:
        print("[!] Требуются библиотеки. Установка...")
        os.system('pip install pyautogui keyboard')
    
    picker = DotaAutoPicker()
    picker.start_listener()

if __name__ == "__main__":
    main()
