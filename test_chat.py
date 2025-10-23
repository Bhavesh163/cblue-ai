#!/usr/bin/env python3
import requests
import time

API_URL = 'http://localhost:8000'

def test_chat():
    print("Testing chat endpoint...")
    
    response = requests.post(
        f'{API_URL}/chat',
        json={'message': 'Hello, what services do you provide?'}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        data = response.json()
        if 'message' in data and data['message']:
            print("✅ Chat working!")
            print(f"Bot response: {data['message']}")
        else:
            print("❌ Empty response")
    else:
        print(f"❌ Error: {response.status_code}")

def test_health():
    print("\nTesting health endpoint...")
    response = requests.get(f'{API_URL}/health')
    print(f"Health: {response.json()}")

if __name__ == '__main__':
    test_health()
    time.sleep(1)
    test_chat()
