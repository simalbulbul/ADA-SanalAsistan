import random
import pandas as pd
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import warnings
import webbrowser
import multiprocessing
import whatsapp

df = None  # Başlangıçta df'yi tanımlıyoruz
warnings.simplefilter(action='ignore', category=FutureWarning)

try:
    df = pd.read_csv("dataset.csv", delimiter=";")  
    print("CSV dosyası başarıyla yüklendi!")
except Exception as e:
    print(f"Hata: {e}")

asistan = "Ada: "

r = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)
        try:
            girdi = r.recognize_google(audio, language="tr-TR")
            print(f"Girdi: {girdi}")
            return girdi
        except sr.UnknownValueError:
            print(asistan + "Anlayamadım, lütfen tekrar eder misiniz?")
            return ""
        except sr.RequestError:
            print(asistan + "Bağlantı hatası, tekrar deneyin.")
            return ""

def temizle_df(df):
    """DataFrame'deki NaN değerlerini temizler."""
    return df.applymap(lambda x: '' if isinstance(x, float) and pd.isna(x) else x)

def cevap(girdi):
    """Kullanıcıdan alınan komuta göre cevap verir."""
    global df  

    if df is None:
        print(asistan + "CSV dosyası yüklenemedi. Lütfen dosyayı kontrol edin.")
        return

    girdi = girdi.lower()

    df_clean = temizle_df(df)

    if "şaka yapar mısın" in girdi or "şaka yap" in girdi:
        if 'şaka yapar mısın' in df_clean['komut'].str.lower().values:
            yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'şaka yapar mısın'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
            print(asistan + str(yanit))
            if yanit:  # Eğer yanıt boş değilse sesli yanıtla
                sesliYanit(str(yanit))

    elif 'nasılsın' in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'nasılsın'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'iyiyim' in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'iyiyim'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'kötüyüm' in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'kötüyüm'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'bilgi' in girdi or "bilgi verir misin" in girdi or "bilgi ver" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'bilgi'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'film' in girdi or "film önerir misin" in girdi or "film öner" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'filmsoru'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'hayır yok' in girdi or "fark etmez" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'filmoneri'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'korku' in girdi or "korku filmi" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'korku'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'komedi' in girdi or "komedi filmi" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'komedi'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif 'bilim kurgu' in girdi or "bilim kurgu filmi" in girdi:
        yanit = random.choice(df_clean[df_clean['komut'].str.lower() == 'bilim kurgu'][['yanit1', 'yanit2', 'yanit3', 'yanit4', 'yanit5']].dropna().values.flatten())
        print(asistan + str(yanit))
        if yanit:
            sesliYanit(str(yanit))

    elif "google da ara" in girdi or "Google'da ara" in girdi:
        print(asistan + "Sizin için ne aramamı istersiniz?")
        sesliYanit("Sizin için ne aramamı istersiniz?")
        search = record()
        if search:  
            url = f"https://www.google.com/search?q={search}"
            webbrowser.open(url)

    elif "makale ara" in girdi:
        print(asistan + "Sizin için ne konuda makale aramamı istersiniz?")
        sesliYanit("Sizin için ne konuda makale aramamı istersiniz?")
        search = record()
        if search:
            url = f"https://scholar.google.com/scholar?hl=tr&as_sdt=0%2C5&q={search}"
            webbrowser.open(url)

    elif "youtube da ara" in girdi or "Youtube'da ara" in girdi or "Youtube da ara" in girdi:
        print(asistan + "Sizin için ne aramamı istersiniz?")
        sesliYanit("Sizin için ne aramamı istersiniz?")
        search = record()
        if search:
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.open(url)

    elif "hava durumu" in girdi:
        print(asistan + "Hava durumu sayfası açılıyor...")
        sesliYanit("Hava durumu sayfası açılıyor...")
        havaDurumu_sayfasiniAc()

    elif "nöbetçi eczane" in girdi:
        print(asistan + "Nöbetçi eczane sayfası açılıyor...")
        sesliYanit("Nöbetçi eczane sayfası açılıyor...")
        nobetciEczane_sayfasiniAc()

    elif "not defteri" in girdi:
        print(asistan + "not defteri açılıyor...")
        sesliYanit("not defteri açılıyor...")
        notDefter_sayfasiniAc()

    if "mesaj at" in girdi:
        print(asistan + "Kime mesaj atmamı istersin?")
        sesliYanit("Kime mesaj atmamı istersin?")
        kisi = record()  
        print(asistan + "Ne mesajı göndermemi istersin?")
        sesliYanit("Ne mesajı göndermemi istersin?")
        mesaj = record()  
        whatsapp.mesaj_gonder(kisi, mesaj)  

   

def havaDurumu_sayfasiniAc():
    havaDurumu_url = "havaDurumu.html"  
    webbrowser.open(havaDurumu_url)

def nobetciEczane_sayfasiniAc():
    nobetciEczane_url = "nobetciEczane.html"  
    webbrowser.open(nobetciEczane_url)

def notDefter_sayfasiniAc():
    notDefter_url = "notDefter.html"  
    webbrowser.open(notDefter_url)

def sesliYanit(string):
    """Metni sesli yanıt olarak çevirir ve çalar."""
    if string: 
        tts = gTTS(text=string, lang="tr", slow=False)
        dosya = "cevap.mp3"
        tts.save(dosya)
        playsound(dosya)
        os.remove(dosya)
    else:
        print(asistan + "Cevap verilemiyor, metin boş.")

if __name__ == "__main__":
    while True:
        kullanici_input = record()
        if kullanici_input:
            cevap(kullanici_input)
