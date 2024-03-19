import speech_recognition as sr 

def capturar_fala():
    capturada, texto = False, None

    reconhecedor = sr.Recognizer()

    try:
        with sr.Microphone() as fonte_de_audio:
            reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

            print("Fale alguma coisa... 🎙️🦻🏼")
            fala = reconhecedor.listen(fonte_de_audio, timeout=4,phrase_time_limit=4)
            texto = reconhecedor.recognize_google(fala,language="pt-br") 
            capturada = True

    except Exception as e:
        print(f"Erro capturando fala: {str(e)}")
    
    return capturada, texto 

def imprimir_texto(texto):
    print(f"Texto capturado: {texto}")

if __name__ == "__main__":
    capturada, texto = capturar_fala()
    if capturada:
        imprimir_texto(texto)