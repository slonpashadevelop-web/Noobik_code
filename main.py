import keyboard
import subprocess
import os
import sys
import winreg
import time
import pyautogui
import psutil
class GameLauncher:
    def __init__(self):
        self.csgo_process = None
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
        except Exception as e:
            pass
        
        for path in steam_paths:
            if os.path.exists(path):
                return path
        
        return None
    
    def launch_dota2(self):
        """Запустить Dota 2"""
        try:
            print("[*] Запуск Dota 2...")
            
            dota2_app_id = "570"
            steam_url = f"steam://run/{dota2_app_id}"
            
            # Метод 1: Попробуем через os.startfile (работает на Windows)
            try:
                os.startfile(steam_url)
                print("[+] Запущено через os.startfile")
                return True
            except Exception as e1:
                print(f"[-] os.startfile не сработал: {e1}")
            
            # Метод 2: Попробуем через cmd start
            try:
                subprocess.Popen(f'cmd /c start {steam_url}', shell=True)
                print("[+] Запущено через cmd start")
                return True
            except Exception as e2:
                print(f"[-] cmd start не сработал: {e2}")
            
            # Метод 3: Если Steam найден, запустим его напрямую
            steam_path = self.find_steam_path()
            if steam_path:
                try:
                    subprocess.Popen([steam_path, f"-applaunch {dota2_app_id}"])
                    print("[+] Запущено через прямой вызов steam.exe")
                    return True
                except Exception as e3:
                    print(f"[-] Прямой запуск не сработал: {e3}")
            
            print("[-] Все методы запуска не сработали")
            return False
        except Exception as e:
            print(f"[-] Ошибка при запуске Dota 2: {e}")
            return False
    
    def is_process_running(self, process_name):
        """Проверить, работает ли процесс"""
        try:
            for proc in psutil.process_iter(['name']):
                if process_name.lower() in proc.name().lower():
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False
    
    def wait_for_dota_load(self, timeout=30):
        """Ждать загрузки Dota 2"""
        print("[*] Ожидание загрузки Dota 2...")
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_process_running("dota2.exe"):
                print("[+] Dota 2 загружена")
                return True
            time.sleep(1)
        return False
    
    def accept_game(self):
        """Нажать кнопку Accept когда найдется игра"""
        print("[*] Ожидание поиска игры... (это может занять до 10 минут)")
        print("[*] Скрипт будет нажимать Accept когда найдется игра...")
        print("[*] Убедитесь, что окно Dota 2 активно\n")
        
        # Ждем до 10 минут поиска
        search_timeout = 600  # 10 минут
        start_time = time.time()
        check_interval = 3  # Проверяем каждые 3 секунды
        
        while time.time() - start_time < search_timeout:
            try:
                # Нажимаем Enter для подтверждения Accept
                pyautogui.press('enter')
                elapsed = int(time.time() - start_time)
                print(f"[*] Попытка подтвердить Accept (прошло {elapsed}сек)")
            except:
                pass
            
            time.sleep(check_interval)
        
        print("[-] Игра не найдена за 10 минут")
        return False
    
    def close_dota2(self):
        """Закрыть Dota 2"""
        try:
            print("[*] Закрытие Dota 2...")
            os.system('taskkill /F /IM dota2.exe')
            time.sleep(2)
            print("[+] Dota 2 закрыта")
            return True
        except Exception as e:
            print(f"[-] Ошибка при закрытии Dota 2: {e}")
            return False
    
    def launch_csgo(self):
        """Запустить CS GO 2"""
        try:
            print("[*] Запуск CS GO 2...")
            
            csgo_app_id = "730"
            steam_url = f"steam://run/{csgo_app_id}"
            
            # Метод 1: Попробуем через os.startfile (работает на Windows)
            try:
                os.startfile(steam_url)
                print("[+] Запущено через os.startfile")
                return True
            except Exception as e1:
                print(f"[-] os.startfile не сработал: {e1}")
            
            # Метод 2: Попробуем через cmd start
            try:
                subprocess.Popen(f'cmd /c start {steam_url}', shell=True)
                print("[+] Запущено через cmd start")
                return True
            except Exception as e2:
                print(f"[-] cmd start не сработал: {e2}")
            
            # Метод 3: Если Steam найден, запустим его напрямую
            steam_path = self.find_steam_path()
            if steam_path:
                try:
                    subprocess.Popen([steam_path, f"-applaunch {csgo_app_id}"])
                    print("[+] Запущено через прямой вызов steam.exe")
                    return True
                except Exception as e3:
                    print(f"[-] Прямой запуск не сработал: {e3}")
            
            print("[-] Все методы запуска не сработали")
            return False
        except Exception as e:
            print(f"[-] Ошибка при запуске CS GO 2: {e}")
            return False
    
    def change_steam_name(self):
        """Изменить имя профиля в Steam на 'Слон Паша'"""
        try:
            print("[*] Открытие страницы редактирования профиля в Steam клиенте...")
            
            # Открываем страницу редактирования в Steam клиенте
            edit_url = "steam://openurl/https://steamcommunity.com/id/Ya_Slon/edit"
            os.startfile(edit_url)
            
            print("[*] Ожидание загрузки страницы в Steam (10 сек)...")
            time.sleep(10)
            
            # Убеждаемся, что фокус на окне Steam
            pyautogui.click(700, 400)
            time.sleep(1)
            
            # Кликаем на поле "ИМЯ ПРОФИЛЯ"
            print("[*] Кликаю на поле 'ИМЯ ПРОФИЛЯ'...")
            pyautogui.click(640, 305)
            time.sleep(0.5)
            
            # Очищаем текущее имя
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.3)
            
            # Вводим новое имя "Слон Паша"
            print("[*] Ввожу 'Слон Паша'...")
            new_name = "Слон Паша"
            subprocess.run(['powershell', '-Command', f'Set-Clipboard -Value "{new_name}"'], 
                         capture_output=True)
            time.sleep(0.3)
            
            # Вставляем из буфера обмена
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            
            # Ищем и кликаем на кнопку "Сохранить" - она синяя и находится внизу
            print("[*] Нажимаю кнопку 'Сохранить'...")
            # Кнопка обычно находится внизу справа на странице редактированияs
            pyautogui.click(945, 543)  # Координаты кнопки "Сохранить"
            time.sleep(2)
            
            print("[+] Имя профиля изменено на 'Слон Паша'!")
            return True
            
        except Exception as e:
            print(f"[-] Ошибка при смене имени: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def on_s_pressed(self):
        """Обработчик нажатия S/ы"""
        print("\n[!] Клавиша S/ы нажата!")
        print("[*] Запускаю смену имени в Steam...\n")
        
        if self.change_steam_name():
            print("[+] Имя в Steam успешно изменено!")
        else:
            print("[-] Не удалось изменить имя в Steam")
    
    def on_backslash_pressed(self):
        """Обработчик нажатия \\"""
        print("\n[!] Клавиша \\ нажата!")
        print("[*] Запускаю Dota 2 с автопоиском игры...\n")
        
        if self.launch_dota2():
            if self.wait_for_dota_load():
                if self.accept_game():
                    print("[+] Игра найдена и принята!")
                    time.sleep(5)  # Ждем перехода в выбор героев
                    self.close_dota2()
                    print("[+] Dota 2 закрыта после выбора героев")
                else:
                    print("[-] Не удалось найти игру")
                    self.close_dota2()
            else:
                print("[-] Dota 2 не загрузилась")
        else:
            print("[-] Не удалось запустить Dota 2")
    
    def on_delete_pressed(self):
        """Обработчик нажатия Del"""
        print("\n[!] Клавиша Del нажата!")
        print("[*] Запускаю CS GO 2...\n")
        
        if self.launch_csgo():
            print("[+] CS GO 2 успешно запущена!")
        else:
            print("[-] Не удалось запустить игру")
    
    def start_listener(self):
        """Начать прослушивание горячих клавиш"""
        print("[*] Программа запущена")
        print("[*] Горячие клавиши:")
        print("     Del - Запустить CS GO 2")
        print("     \\  - Запустить Dota 2 с автопоиском")
        print("     S/ы - Изменить имя в Steam на 'слон паша'")
        print("[*] Для выхода нажмите Esc\n")
        
        # Регистрируем функции на нажатие клавиш
        keyboard.add_hotkey('del', self.on_delete_pressed)
        keyboard.add_hotkey('\\', self.on_backslash_pressed)
        keyboard.add_hotkey('s', self.on_s_pressed)
        
        # Слушаем Esc для выхода
        keyboard.wait('esc')
        print("\n[*] Программа завершена")

def main():
    # Проверяем установку необходимых библиотек
    try:
        import keyboard
        import pyautogui
        import psutil
    except ImportError:
        print("[!] Требуются библиотеки. Установка...")
        os.system('pip install keyboard pyautogui psutil')
    
    launcher = GameLauncher()
    launcher.start_listener()

if __name__ == "__main__":
    main()