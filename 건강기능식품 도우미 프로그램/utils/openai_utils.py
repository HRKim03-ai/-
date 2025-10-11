import openai
import requests
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# Mistral API 설정
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def get_llm_response(prompt):
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요.")
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-medium",  # 또는 mistral-small, mistral-large 등
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"API 요청 중 오류가 발생했습니다: {e}")
    except KeyError as e:
        raise Exception(f"API 응답 형식이 예상과 다릅니다: {e}")