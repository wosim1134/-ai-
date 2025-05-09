import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

API_KEY = '47359576e0f3bfe8b6c633d12f9071cc'  # OpenWeatherMap API Key

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    res = requests.get(url)
    
    if res.status_code == 200:
        data = res.json()
        temp = round(data['main']['temp'] - 273.15, 1)
        feels = round(data['main']['feels_like'] - 273.15, 1)
        humid = data['main']['humidity']
        wind = data['wind']['speed']
        icon_code = data['weather'][0]['icon']
        city_name = data['name']
        
        # 텍스트 업데이트
        lbl_city.config(text=f"{city_name}")
        lbl_temp.config(text=f"기온 {temp}ºC")
        lbl_feel.config(text=f"체감온도 {feels}ºC")
        lbl_humid.config(text=f"습도 {humid}%")
        lbl_wind.config(text=f"풍속 {wind} m/s")
        
        # 날씨 아이콘 업데이트
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_data = requests.get(icon_url).content
        img = Image.open(BytesIO(icon_data))
        img = img.resize((100, 100), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        lbl_icon.config(image=img_tk)
        lbl_icon.image = img_tk
    else:
        lbl_city.config(text="도시 없음")
        lbl_temp.config(text="기온 -")
        lbl_feel.config(text="체감온도 -")
        lbl_humid.config(text="습도 -")
        lbl_wind.config(text="풍속 -")
        lbl_icon.config(image='')

# GUI 생성
root = tk.Tk()
root.title("날씨 앱 - 지현우")
root.geometry("800x600")
root.configure(bg="#a7d3f4")

# 도시 선택 박스
cities = ['선택', 'seoul', 'busan', 'tokyo', 'osaka', 'kyoto', 'barcelona']
sel_city = ttk.Combobox(root, values=cities, font=("Helvetica", 16), state='readonly')
sel_city.set('선택')
sel_city.pack(pady=20)

def on_city_change(event):
    city = sel_city.get()
    if city != '선택':
        get_weather(city)

sel_city.bind("<<ComboboxSelected>>", on_city_change)

# 출력 라벨들
lbl_city = tk.Label(root, text="도시", font=("Helvetica", 20), bg="#a7d3f4")
lbl_city.pack(pady=10)

lbl_temp = tk.Label(root, text="기온 -", font=("Helvetica", 18), bg="#a7d3f4")
lbl_temp.pack()

lbl_feel = tk.Label(root, text="체감온도 -", font=("Helvetica", 18), bg="#a7d3f4")
lbl_feel.pack()

lbl_humid = tk.Label(root, text="습도 -", font=("Helvetica", 18), bg="#a7d3f4")
lbl_humid.pack()

lbl_wind = tk.Label(root, text="풍속 -", font=("Helvetica", 18), bg="#a7d3f4")
lbl_wind.pack()

# 날씨 아이콘
lbl_icon = tk.Label(root, bg="#a7d3f4")
lbl_icon.pack(pady=20)

root.mainloop()
