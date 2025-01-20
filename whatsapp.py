import pywhatkit as kit
import pyautogui

def mesaj_gonder(isim, mesaj):
    try:
        numara = get_numara(isim)
        
        if numara:
            kit.sendwhatmsg_instantly(
                phone_no="+90" + numara,
                message=mesaj,
                wait_time=5  
            )
            
            pyautogui.sleep(5) 
            pyautogui.press('enter') 
            print(f"Mesaj gönderildi: {isim} ({numara}) -> {mesaj}")
        else:
            print(f"Kişi bulunamadı: {isim}")
    except Exception as e:
        print(f"Hata: {e}")
        import traceback
        traceback.print_exc()

def get_numara(isim):
    telefon_rehberi = {
       
    }

    isim = isim.lower()  # İsim küçük harfe çevriliyor
    return telefon_rehberi.get(isim, None)
