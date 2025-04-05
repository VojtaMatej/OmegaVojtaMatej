import requests
import json
import time
import re  # Import pro extrakci dispozice z titulu

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

BASE_URL = "https://www.sreality.cz/api/cs/v2/estates"
PARAMS = {
    "category_main_cb": 1,  # Byty
    "category_type_cb": 1,  # Prodej
    "per_page": 20,  # Počet na stránku
    "page": 1
}

collected_data = {}
SAVE_THRESHOLD = 20  # Po kolika inzerátech se uloží do JSON


def extract_dispozice(title):
    """Extrahuje dispozici (např. Mezonet, Jednopodlažní) z titulu."""
    match = re.search(r"(Mezonet|Ateliér|Loft)", title, re.IGNORECASE)
    return match.group(1) if match else "Jednopodlažní"


def fetch_data(url, params, retries=3):
    """Načítá data z API Sreality.cz s opakováním při chybě."""
    for _ in range(retries):
        try:
            response = requests.get(url, params=params, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"❌ Chyba při načítání {url}: {e}, zkouším znovu...")
            time.sleep(2)
    return None


def fetch_sreality_data():
    """Stahuje inzeráty z Sreality.cz."""
    global collected_data
    print("🔄 Stahuji data z Sreality.cz...")

    page = 1
    new_listings = 0

    while True:
        PARAMS["page"] = page
        data = fetch_data(BASE_URL, PARAMS)

        if not data or "_embedded" not in data:
            print("❌ Nepodařilo se načíst data nebo žádné nové inzeráty.")
            break

        for estate in data["_embedded"].get("estates", []):
            url = f"https://www.sreality.cz/detail/{estate.get('hash_id')}"
            title = estate.get("name", "")
            dispozice = extract_dispozice(title)

            if url not in collected_data:
                collected_data[url] = {
                    "title": title,
                    "price": estate.get("price"),
                    "location": estate.get("locality"),
                    "dispozice": dispozice,  # Nový atribut – Mezonet, Jednopodlažní...
                    "url": url
                }
                new_listings += 1

        page += 1

        if new_listings >= SAVE_THRESHOLD:
            save_data()

        time.sleep(1)

    save_data()


def save_data():
    """Uloží data do JSON souboru."""
    with open("fresh_sreality_apartments.json", "w", encoding="utf-8") as f:
        json.dump(list(collected_data.values()), f, ensure_ascii=False, indent=4)
    print(f"💾 Uloženo {len(collected_data)} inzerátů do sreality_apartments.json")


def main():
    """Spouští nekonečný loop pro průběžné získávání dat."""
    while True:
        fetch_sreality_data()
        print("🕒 Čekám 60 sekund...")
        time.sleep(60)  # Aktualizace každou minutu


if __name__ == "__main__":
    main()
