import requests
from pprint import pprint
import matplotlib.pyplot as plt

korean = {
    'feels_like': '체감온도',
    'humidity': '습도',
    'pressure': '기압',
    'temp': '온도', 
    'temp_max': '최고온도',
    'temp_min': '최저온도',
    'description': '요약',
    'icon': '아이콘',
    'main': '핵심',
    'id': '식별자',
}

def get_weather(api_key):

    def kelvin_to_celsius(kelvin):
        return round((kelvin - 32) * 5 / 9, 2)
    
    city = "Busan,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url).json()

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    result = {
        '기본': {},
        '날씨': [{}],
    }

    # Mapping English keys to Korean keys in '기본'
    for key_en, key_kr in korean.items():
        if key_en in response['main']:
            result['기본'][key_kr] = response['main'][key_en]

    # Mapping English keys to Korean keys in '날씨'
    for key_en, key_kr in korean.items():
        if key_en in response['weather'][0]:
            if isinstance(response['weather'][0][key_en], list):
                result['날씨'][key_kr] = [response['weather'][0][key_en]]
            else:
                result['날씨'][0][key_kr] = response['weather'][0][key_en]

    # Adding Celsius temperature for '온도' related keys in '기본'
    for key_en in ['feels_like', 'temp_max', 'temp_min', 'temp']:
        if key_en in response['main']:
            temp_value_kelvin = response['main'][key_en]
            temp_value_celsius = kelvin_to_celsius(temp_value_kelvin)
            result['기본'][f"{korean[key_en]} (섭씨)"] = temp_value_celsius

    # Adding Celsius temperature for '온도' related key in '날씨'
    for key_en in ['temp']:
        if key_en in response['weather'][0]:
            temp_value_kelvin = response['weather'][0][key_en]
            temp_value_celsius = kelvin_to_celsius(temp_value_kelvin)
            result['날씨'][0][f"{korean[key_en]} (섭씨)"] = temp_value_celsius

        

    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '4d337bf902cb9a2934a563551f480cf5'

    result = get_weather(api_key)
    pprint(result)


# 온도 데이터 추출
temperatures = [
    result['기본']['온도 (섭씨)'],
    result['기본']['최고온도 (섭씨)'],
    result['기본']['최저온도 (섭씨)'],
    result['기본']['체감온도 (섭씨)'],
]
labels = ['Temperature', 'Max Temperature', 'Min Temperature', 'Feels Like']

# 막대 그래프 그리기
plt.figure(figsize=(10, 6))  # 그래프 사이즈 설정

plt.bar(labels, temperatures, color=['blue', 'green', 'red', 'orange'])  # 막대 그래프 생성

# 그래프 제목과 축 레이블 설정
plt.title('Weather Information in Busan')
plt.xlabel('Weather Parameters')
plt.ylabel('Temperature (Celsius)')

# 그래프 표시
plt.grid(True)  # 그리드 표시 (선택적)
plt.tight_layout()  # 레이아웃 최적화 (선택적)
plt.show()
