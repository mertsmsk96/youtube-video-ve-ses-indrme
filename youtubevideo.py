import os
from pytube import YouTube
import youtube_dl

def muzikIndir(link,directory):
    try:
        yt = YouTube(link)
    except:
        print("Hatalı Link")
        exit()

    mp3 = yt.streams.filter(only_audio=True).first()

    print("İndiriliyor...")
    sonuc = mp3.download(directory)
    base,ext=os.path.splitext(sonuc)

    to_mp3 = base + ".mp3"
    os.rename(sonuc,to_mp3)
    print("Müzik başarılı bir şekilde indirildi!")

ydl_opts = {}
def videoIndir():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

cann = 1
while True:
    print("""
    video indirmek için 1
    Müzik indirmek için 2""")
    secenek = input("İşlem: ")
    if secenek == "1":
        print("video indirme")
        link = input("Link Giriniz: ")
        zxt = link.strip()
        videoIndir()
    elif secenek == "2":
        print("müzik indirme")
        link = input("Link Giriniz: ")
        directory = input("Kaydedilecek Yol: ")
        muzikIndir(link,directory)
    else:
        print("çıkılıyor...")
        break

        