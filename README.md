# NiKenguru

**Fullstack dasturchi · AI Engineer**  
Python, JavaScript, REST API, PostgreSQL · Namangan, O‘zbekiston

Savdo dasturlari, veb-ilovalar va mahalliy integratsiyalar. Dastur xavfsizligini tekshirish va muammolarni tuzatish bilan ham shug‘ullanaman.

**Fullstack-разработчик · AI Engineer** · Наманган, Узбекистан  
Разработка веб-приложений, API, интеграции и тестирование безопасности продукта.

## Loyihalar / Проекты

| Loyiha | Nima qiladi / Что показывает |
| --- | --- |
| [Keng POS](https://github.com/NiKenguru/keng-releases) | Windows kassasi / Касса для кафе с заказами, печатью чеков и отчётами. Публичные релизы и руководство. |
| [Valyuta kurslari / Курсы валют](portfolio/server.py) | Интеграция с JSON API Центрального банка Узбекистана, нормализация номинала, представление в UZS. |
| [Bilimlar bazasi / База знаний](portfolio/index.html) | Демонстрационный справочник по Keng POS с поиском ответов на узбекском и русском языках. |

## Ishga tushirish / Запуск

```bash
python -m pip install -r portfolio/requirements.txt
python -m uvicorn server:app --app-dir portfolio --host 127.0.0.1 --port 8000
```

Откройте http://127.0.0.1:8000. Документация REST API доступна на /docs. Поиск работает на встроенных демонстрационных заметках и возвращает идентификаторы источников. Поиск лексический. LLM и векторная база планируются отдельно. Для загрузки курсов нужен доступ к cbu.uz.

- [Документация JSON API ЦБ Узбекистана](https://cbu.uz/en/arkhiv-kursov-valyut/veb-masteram/)
- [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template) — открытый MIT-референс для перехода на React и PostgreSQL. Демонстрации в этой ветке написаны отдельно.
