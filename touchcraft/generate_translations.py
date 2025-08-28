import polib
from pathlib import Path
from bs4 import BeautifulSoup
import re

BASE_DIR = Path(__file__).resolve().parent
LOCALE_DIR = BASE_DIR / "locale"
LANGUAGES = ["ru", "uk", "en", "es"]  # языки проекта

# Поиск строк в шаблонах
def extract_from_html(file_path):
    text_set = set()
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    # Ищем {% trans "..." %}
    matches = re.findall(r'{%\s*trans\s+"([^"]+)"\s*%}', content)
    text_set.update(matches)
    return text_set

# Поиск строк в Python
def extract_from_python(file_path):
    text_set = set()
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r'_\("([^"]+)"\)', content)
    text_set.update(matches)
    return text_set

# Сбор всех строк
all_strings = set()
for path in BASE_DIR.rglob("*.html"):
    all_strings.update(extract_from_html(path))
for path in BASE_DIR.rglob("*.py"):
    all_strings.update(extract_from_python(path))

print(f"🔍 Найдено {len(all_strings)} строк для перевода.")

# Создание .po файлов
for lang in LANGUAGES:
    po_path = LOCALE_DIR / lang / "LC_MESSAGES" / "django.po"
    po_path.parent.mkdir(parents=True, exist_ok=True)

    if po_path.exists():
        po = polib.pofile(str(po_path))
    else:
        po = polib.POFile()
        po.metadata = {
            "Content-Type": "text/plain; charset=UTF-8",
            "Language": lang,
        }

    for text in sorted(all_strings):
        if not po.find(text):
            po.append(polib.POEntry(msgid=text, msgstr=text if lang == "ru" else ""))

    po.save(str(po_path))
    po.save_as_mofile(str(po_path.with_suffix(".mo")))

print("✅ Переводы созданы и скомпилированы!")
