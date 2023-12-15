import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("말해보세요...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"인식된 명령: {command}")
        process_command(command)
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition API 오류: {e}")

def process_command(command):
    if "안녕" in command:
        print("안녕하세요!")
    elif "날씨" in command:
        print("날씨를 가져오는 중...")

recognize_speech()
