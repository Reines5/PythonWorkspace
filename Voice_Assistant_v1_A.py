import speech_recognition as sr
from datetime import datetime
import webbrowser

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:

        if ask:
            print(ask)

        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language='tr-TR && en-EN, en-EN')

        except sr.UnknownValueError:
            if voice(language = 'tr_TR'):
                print('Anlayamadım lütfen tekrar deneyiniz...')

            if voice(language = 'en_EN'):
                print("What you are trying to say ...")
    
        except sr.RequestError:
            if voice(language = 'tr_TR'):
                print('!!Sistem Çalışmadı!!')

            if voice(language = 'en_EN'):
                print('!!System Error!!')

        return(voice)

def response(voice):

    if 'saat kaç' in voice:
        print(datetime.now().strftime('%H:%M'))

    if 'What time is it' in voice:
        print(datetime.now().strftime('%H:%M'))

    if 'arama yap' in voice:
        search = record('Ne Aramak İstiyorsunuz?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print(search + (' İçin Bulduklarım'))

    if 'search' in voice:
        search_en = record('How can I help?')
        url_en = 'https://google.com/search?q=' + search_en
        webbrowser.get().open(url_en)
        print(search_en + ' I found the response')
    

print('Nasıl Yardımcı Olabilirim?')
voice = record()
print(voice)
response(voice)