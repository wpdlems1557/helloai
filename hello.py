print("안녕하세요! 파이썬 공부를 시작합니다.")

import random

# 1. 변수와 데이터 타입
secret_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))
    attempts += 1

    # 여기서부터 수정된 로직입니다!
    if guess < secret_number:             # 입력값이 정답보다 작으면?
        print("Up! 더 큰 숫자예요. ⬆️")
    elif guess > secret_number:           # 입력값이 정답보다 크면?
        print("Down! 더 작은 숫자예요. ⬇️")
    else:                                 # 둘 다 아니면 (즉, 같으면!)
        print(f"🎉 정답입니다! {attempts}번 만에 맞추셨네요.")
        break
