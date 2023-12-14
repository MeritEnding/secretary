import speech_recognition as sr

def recognize_speech():
    # 음성 인식기 생성
    recognizer = sr.Recognizer()

    # 마이크에서 음성을 수집
    with sr.Microphone() as source:
        print("말씀해주세요...")
        recognizer.adjust_for_ambient_noise(source)  # 환경 소음에 대한 조절
        audio = recognizer.listen(source, timeout=5)  # 5초 동안 음성 수집

    try:
        print("음성 인식 중...")
        text = recognizer.recognize_google(audio, language="ko-KR")  # Google 음성 인식 사용 (한국어)
        print(f"인식된 텍스트: {text}")
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 인식 서비스에 접근할 수 없습니다; {e}")

if __name__ == "__main__":
    recognize_speech()

# 추가
