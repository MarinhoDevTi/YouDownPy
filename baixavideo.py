#Biblioteca do pytube
from pytube import YouTube

#função para download 
def Donwload(link):
    baixarVideo = YouTube(link)
    baixarVideo = baixarVideo.streams.get_lowest_resolution()
    #exceções 
    try:
        baixarVideo.download()
    except:
        print("Um erro impediu o exito de seu download !!")
    print("Download completo com sucesso !")
#leitura de dados     
link = input("Cole o endereço do link: ")
Donwload(link)