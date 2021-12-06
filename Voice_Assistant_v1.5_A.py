import speech_recognition as sr
from datetime import datetime
import webbrowser
from GoogleNews import GoogleNews



def record(ask = False):
    with sr.Microphone() as source:

        if ask:
            print(ask)

        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language='tr-TR, en-EN')

        except sr.UnknownValueError:
            if voice(language = 'tr_TR'):
                print('Anlayamadım lütfen tekrar deneyiniz...')

            if voice(language = 'en_EN'):
                print("What you are trying to say...")
    
        except sr.RequestError:
            if voice(language = 'tr_TR'):
                print('!!Sistem Çalışmadı!!')

            if voice(language = 'en_EN'):
                print('!!System Error!!')

        return(voice)

def record_en(ask = False):
    with sr.Microphone() as source:

        if ask:
            print(ask)

        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language='en-EN && tr-TR')

        except sr.UnknownValueError:
            if voice(language = 'en_EN'):
                print("What you are trying to say...")
    
        except sr.RequestError:
            if voice(language = 'en_EN'):
                print('!!System Error!!')

        return(voice)

def record_tr(ask = False):
    with sr.Microphone() as source:

        if ask:
            print(ask)

        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language='tr-TR && en-EN')

        except sr.UnknownValueError:
            if voice(language = 'tr-TR && en-EN'):
                print("Dediğini anlayamadım...")
    
        except sr.RequestError:
            if voice(language = 'tr-TR && en-EN'):
                print('!!Sistem Hatası!!')

        return(voice)

def response_tr(voice):
    if 'saat kaç' in voice:
        print(datetime.now().strftime('%H:%M'))

    if 'arama yap' in voice:
        search = record('Ne Aramak İstiyorsunuz?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print(search + (' İçin Bulduklarım'))

    if 'haberler' in voice:
        googleNews = GoogleNews()
        googleNews = GoogleNews('tr', 'd')
        googleNews.search('Turkey')
        googleNews.getpage(1)
        googleNews.result()
        googleNews.gettext()

def response_en(voice):
    if 'what time is it' in voice:
        print(datetime.now().strftime('%H:%M'))

    if 'search' in voice:
        search_en = record('what do you want to call?')
        url_en = 'https://google.com/search?q=' + search_en
        webbrowser.get().open(url_en)
        print(search_en + ' I found the response')

    if 'news' in voice:
        googleNews = GoogleNews()
        googleNews = GoogleNews('en', 'd')
        googleNews.search('USA')
        googleNews.getpage(1)
        googleNews.result()
        googleNews.gettext()



r = sr.Recognizer()

print('******* Choice Language *******\n** 1)Türkçe ****** 2)English **')
voice = record()
print(voice)

if 'Türkçe' in voice:
    print('Nasıl Yardımcı Olabilirim?')
    voice = record_tr()
    print(voice)
    response_tr(voice)

elif 'English' in voice:
    print('How can I help?')
    voice = record_en()
    print(voice)
    response_en(voice)

else:
    print('!!System Error!!')