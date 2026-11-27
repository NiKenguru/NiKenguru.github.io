"""Local FastAPI portfolio demos for Uzbekistan."""
import json
import re
import unicodedata
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse

app = FastAPI(title="Uzbekistan Portfolio Demos", version="1.0.0")
ROOT = Path(__file__).resolve().parent
CBU_URL = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"
KB = (
    ("uz", "buyurtma", "Buyurtma ochish", "Stolni tanlang va buyurtmaga taom qo‘shing."),
    ("uz", "hisobot", "Savdo hisoboti", "Hisobotda kunlik savdo va to‘lov turlarini ko‘ring."),
    ("uz", "printer", "Chek printeri", "Chek uchun sozlamalarda kerakli printerni tanlang."),
    ("ru", "buyurtma", "Открытие заказа", "Выберите стол и добавьте блюдо в заказ."),
    ("ru", "hisobot", "Отчёт о продажах", "В отчёте доступны продажи за день и способы оплаты."),
    ("ru", "printer", "Печать чека", "Чтобы напечатать чек, выберите чековый принтер в настройках."),
)


def tokens(text: str) -> set[str]:
    text = unicodedata.normalize("NFKC", text.casefold())
    normalized = re.sub(r"['’ʻʼ‘`]", "", text).replace("ё", "е")
    return set(re.findall(r"[^\W_]+", normalized))


def search(query: str, locale: str) -> list[dict[str, str]]:
    words = tokens(query)
    ranked = []
    for language, key, title, answer in KB:
        if language != locale:
            continue
        score = 2 * len(words & tokens(title)) + len(words & tokens(answer))
        if score:
            ranked.append((score, key, title, answer))
    return [
        {"id": key, "title": title, "answer": answer}
        for _, key, title, answer in sorted(ranked, key=lambda item: (-item[0], item[1]))[:3]
    ]


def read_rates() -> list[dict[str, str]]:
    with urlopen(CBU_URL, timeout=5) as response:
        body = response.read(262145)
    if len(body) > 262144:
        raise ValueError("Rate feed is too large")
    rows = json.loads(body)
    if not isinstance(rows, list):
        raise ValueError("Unexpected rate feed")
    result = []
    for row in rows:
        code = row["Ccy"]
        if code not in {"USD", "EUR", "RUB", "KZT"}:
            continue
        rate = Decimal(str(row["Rate"]))
        nominal = Decimal(str(row["Nominal"]))
        if not rate.is_finite() or not nominal.is_finite() or min(rate, nominal) <= 0:
            raise ValueError("Invalid exchange rate")
        result.append({
            "currency": code,
            "uzs_per_unit": str(rate / nominal),
            "effective_date": datetime.strptime(row["Date"], "%d.%m.%Y").date().isoformat(),
        })
    if not result:
        raise ValueError("Rate feed is empty")
    return sorted(result, key=lambda row: row["currency"])


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(ROOT / "index.html")


@app.get("/api/rates")
def rates():
    try:
        return {"source": CBU_URL, "rates": read_rates()}
    except (OSError, URLError, ValueError, KeyError, TypeError, InvalidOperation) as error:
        raise HTTPException(status_code=502, detail="CBU feed unavailable") from error


@app.get("/api/knowledge")
def knowledge(q: str = Query(min_length=2, max_length=160), lang: str = "uz"):
    if lang not in {"uz", "ru"}:
        raise HTTPException(status_code=422, detail="Unsupported language")
    return {"matches": search(q, lang)}
