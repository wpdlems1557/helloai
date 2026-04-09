import requests
import openai

# 🔑 API 키 입력
YOUTUBE_API_KEY = "AIzaSyB9bL72R-vhmJ7kNJnxkjscHXdtfz8JFXE"
openai.api_key = "sk-proj-v-Z2st4BkVHW6ujoFTnull-gkwq1cQZEvo-Zu8PLLxQwpQQXg31oZyYdmf7G8vZJaW4vsETVZJT3BlbkFJ0YC6bYGyBgfXto2R0PvWw1JBula7R7yKyEdg4Odbm7EU4yOXIq3H1891mWDbOtq-4ZIkAzbvQAY"

# 인기 영상 가져오기
def get_trending_videos():
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=5&regionCode=KR&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()

    videos = []
    for item in data['items']:
        title = item['snippet']['title']
        videos.append(title)

    return videos

# AI 요약 생성
def ai_summary(title):
    prompt = f"""
    다음 유튜브 영상 제목을 보고 내용을 추측해서 요약하고,
    왜 사람들이 좋아할지 설명해줘.

    제목: {title}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# 실행
videos = get_trending_videos()

for i, v in enumerate(videos):
    print(f"{i+1}. {v}")

choice = int(input("번호 선택: "))
selected = videos[choice - 1]

print("\n🤖 AI 분석 결과\n")
print(ai_summary(selected))
