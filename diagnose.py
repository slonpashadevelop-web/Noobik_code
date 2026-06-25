import os as a,subprocess as b,winreg as c
print("=== ДИАГНОСТИКА STEAM ДЛЯ CS GO 2 ===\n");d=[r"C:\Program Files\Steam\steam.exe",r"C:\Program Files (x86)\Steam\steam.exe"];print("Проверка стандартных путей:")
for e in d:f=a.path.exists(e);print(f"  {'✓' if f else '✗'} {e}")
print("\nПроверка реестра Windows:")
try:
 with c.OpenKey(c.HKEY_LOCAL_MACHINE,r"SOFTWARE\Wow6432Node\Valve\Steam") as g:h=c.QueryValueEx(g,"InstallPath")[0];i=a.path.join(h,"steam.exe");f=a.path.exists(i);print(f"  {'✓' if f else '✗'} {i}")
except Exception as j:print(f"  ✗ Реестр не доступен: {j}")
print("\nПеременные окружения:");print(f"  ProgramFiles: {a.environ.get('ProgramFiles','не установлена')}");print(f"  ProgramFiles(x86): {a.environ.get('ProgramFiles(x86)','не установлена')}");print("\nПопытка запуска steam://run/730 (CS GO 2)...");print("  (это просто тест, игра НЕ будет запущена)");print("  Если хотите запустить CS GO, используйте main.py и нажмите Del");print("\n=== КОНЕЦ ДИАГНОСТИКИ ===")
