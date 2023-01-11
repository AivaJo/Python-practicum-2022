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



_w3 Weather history report_
Continue evolving the previously created flask app:
- Get geographic coordinates for a city of your liking via an API call
>     API doc: https://openweathermap.org/api/geocoding-api
- Get historical data from dev.meteostat.net via one of these methods:
>     JSON API
>     Python library
>     Bulk data
- Display one year of temperature history - min., max., average
>     Use the graphical form of representation – matplotlib module
- Create a route /weather_history to display data
>     Show city name and chart with temperature data, including legend (names of axis, description of data)
>     In addition, separately display values for min., max. temperature, the date it was recorded, and the average temperature for the whole range.
>     Provide a download link for an Excel document with temperature data (raw data)
>     Provide a download link for a PDF document with a temperature chart (graphical data)

