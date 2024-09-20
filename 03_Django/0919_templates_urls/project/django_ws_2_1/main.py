import requests

API_URL = None
API_KEY = None
params = {
    'ttbkey': API_KEY,
}
response = requests.get(API_URL).json()
result = []
for item in response['item']:
    book = {
        '저자': item['author'],
        '제목' : item['title'],
    }
    result.append(book)

print(result)
