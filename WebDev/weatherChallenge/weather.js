
const apiKey = '1d7ede5b89ffdb80cd4fb63e20b4615a'; 

const url = `https://api.openweathermap.org/data/2.5/weather?q=Algiers&appid=${apiKey}&units=metric`; // Added `units=metric` for Celsius.

const main = document.getElementById('main');
const description = document.getElementById('description');
const temp = document.getElementById('temp');
const feelsLike = document.getElementById('feelsLike');
const tempMin = document.getElementById('tempMin');
const tempMax = document.getElementById('tempMax');
const humidity = document.getElementById('humidity');
const pressure = document.getElementById('pressure');
const weather = document.getElementById('weather');

axios.get(url)
    .then(response => {
        console.log(response.data);
        const data = response.data;
        weather.style.display='none';
        // Fill in the weather data
        main.innerHTML = data.weather[0].main;
        description.innerHTML = data.weather[0].description;
        temp.innerHTML = `Temperature: ${data.main.temp} °C`;
        feelsLike.innerHTML = `Feels Like: ${data.main.feels_like} °C`;
        tempMin.innerHTML = `Min Temperature: ${data.main.temp_min} °C`;
        tempMax.innerHTML = `Max Temperature: ${data.main.temp_max} °C`;
        humidity.innerHTML = `Humidity: ${data.main.humidity} %`;
        pressure.innerHTML = `Pressure: ${data.main.pressure} hPa`;

        
    })
    .catch(error => {
        console.log(error);
        weather.innerHTML = "Error fetching weather data.";
    });
