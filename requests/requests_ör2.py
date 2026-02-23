import requests
import json

# API bilgilerimiz
api_key = "691b63a6dcd9bda1952408593fd1997f"
base_url = "https://api.themoviedb.org/3"

# Anahtar kelimeye göre film arama
def key_bul(key):
    url = f"{base_url}/search/movie?api_key={api_key}&query={key}&page=1"
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        for film in data.get("results", []):
            print(f"{film.get('title')} ({film.get('release_date')}) - Puan: {film.get('vote_average')}")
    else:
        print("Hata:", result.status_code)

# Popüler filmleri bulma
def populer_film_bul():
    url = f"{base_url}/movie/popular?api_key={api_key}&page=1"
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        for film in data.get("results", []):
            print(f"{film.get('title')} ({film.get('release_date')}) - Puan: {film.get('vote_average')}")
    else:
        print("Hata:", result.status_code)

# Vizyondaki filmleri bulma
def vizyon_film():
    url = f"{base_url}/movie/now_playing?api_key={api_key}&page=1"
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        for film in data.get("results", []):
            print(f"{film.get('title')} ({film.get('release_date')}) - Puan: {film.get('vote_average')}")
    else:
        print("Hata:", result.status_code)

# Ana döngü
while True:
    try:
        secim = int(input("\nNe tür işlem yapmak istersiniz?\n"
                          "1. Anahtar kelimeye göre arama\n"
                          "2. En popüler film listesi\n"
                          "3. Vizyondaki filmler\n"
                          "4. Çıkış\nSeçiminiz: "))
    except ValueError:
        print("Lütfen sayı girin!")
        continue

    if secim == 4:
        print("Çıkış yapıldı.")
        break
    elif secim == 1:
        key = input("Anahtar kelimeniz nedir?: ")
        key_bul(key)
    elif secim == 2:
        populer_film_bul()
    elif secim == 3:
        vizyon_film()
    else:
        print("Yanlış seçim yaptınız.")



"""200 → Her şey yolunda, cevap var.

404 → İstek yapılan kaynak bulunamadı.

401 → Yetkilendirme hatası (API key yanlış olabilir).

500 → Sunucu hatası.
----------------------------
get() → Python sözlüklerinde (dict) kullanılan bir metot.

Görevi: Verilen anahtarın (key) karşılığındaki değeri almak.
"""