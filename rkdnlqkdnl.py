import random

def rps_game():
    options = ["가위", "바위", "보"]
    print("--------------------------------")
    print("✨ 가위바위보 게임에 오신 것을 환영합니다! ✨")
    print("--------------------------------")

    while True:
        user_choice = input("가위, 바위, 보 중 하나를 입력하세요 (종료하려면 '그만'): ")
        
        if user_choice == "그만":
            print("게임을 종료합니다. 다음에 또 봐요! 👋")
            break
            
        if user_choice not in options:
            print("⚠️ '가위', '바위', '보' 중에서만 입력해주세요!")
            continue

        # 컴퓨터의 랜덤 선택
        computer_choice = random.choice(options)
        print(f"나: {user_choice} vs 컴퓨터: {computer_choice}")

        # 승패 판정 로직
        if user_choice == computer_choice:
            print("🤝 비겼습니다!")
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            print("🎉 이겼습니다! 축하드려요!")
        else:
            print("💀 졌습니다... 다시 도전해보세요!")
        print("-" * 30)

if __name__ == "__main__":
    rps_game()
