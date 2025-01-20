import pywhatkit as kit
import pyautogui

def mesaj_gonder(isim, mesaj):
    try:
        numara = get_numara(isim)
        
        if numara:
            # WhatsApp Web üzerinden mesaj göndermeyi başlatıyoruz
            kit.sendwhatmsg_instantly(
                phone_no="+90" + numara,
                message=mesaj,
                wait_time=5  # Açılma ve mesaj gönderim süresi 5 saniyeye düşürüldü
            )
            
            pyautogui.sleep(5)  # Mesajın gönderilmesini beklemek için süre
            pyautogui.press('enter')  # Mesajı göndermek için Enter'a basıyoruz
            print(f"Mesaj gönderildi: {isim} ({numara}) -> {mesaj}")
        else:
            print(f"Kişi bulunamadı: {isim}")
    except Exception as e:
        print(f"Hata: {e}")
        import traceback
        traceback.print_exc()

def get_numara(isim):
    telefon_rehberi = {
        "yalçın durmuş": "5324045750",
        "beyza": "5537744761",
        "selma": "5434463773",
        "şimal": "5550373353"
    }

    isim = isim.lower()  # İsim küçük harfe çevriliyor
    return telefon_rehberi.get(isim, None)
