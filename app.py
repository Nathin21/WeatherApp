from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "f26d3a0bdbb820ec4c8752c2431070d0"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"].capitalize()
            icon_name = ''
            
            if description == 'Mist':
                icon_name = "mist.png"
            if description == 'Rain':
                icon_name = "rain.png"
            if description =='Overcast clouds':
                icon_name = "overcast.png"
            if description == 'Thunderstorm':
                icon_name = "storm.png"
            if description == 'Snow':
                icon_name = "snow.png"
            if description == 'Clear sky':
                icon_name = "sunny.png"
            if description == 'Clouds':
                icon_name = "s-clouds.png"
            if description == 'Broken clouds':
                icon_name = "broken.png"
            if description == 'Drizzle':
                icon_name = "ss.png"
            if description == 'Haze':
                icon_name = "haze.png"
            if description == 'Scattered clouds':
                icon_name = "sca.png"
            
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": description,
                "humidity": data["main"]["humidity"],
                "latitude": data["coord"]["lat"],
                "longitude": data["coord"]["lon"],
                "wind_speed": data["wind"]["speed"],
                "icon_url": f"/static/img/{icon_name}"

            }
        else:
            error = "City not found. Please enter a valid city."

    return render_template("index2.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
