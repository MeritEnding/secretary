from datetime import datetime

# 현재 시간을 얻어오기
current_time = datetime.now()

# 시간을 포맷팅하여 출력
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"현재 시간: {formatted_time}")
