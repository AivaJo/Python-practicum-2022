# Python Practicum 2022

_w1 You will create a minimal Flask application for this assignment. Your application should_

- have a route for /welcome, which responds with the string "welcome"
- have a route for /welcome/home, which responds with the string "welcome home"
- have a route for /welcome/back, which responds with the string "welcome back"

_w2 Weather report_

- Get a weather report for a city of your liking via API call
>     API doc: https://openweathermap.org/current#name
>     API Key: 60aa068482d6ddc251ae5f53570ac5fb
- Create a route /weather which responds with received data
>     display city name and current temperature in Celsius
>     consider using a template to render and display data
- Optional task – let the user pick a city
