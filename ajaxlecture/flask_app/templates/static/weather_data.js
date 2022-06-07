console.log("running");

async function getWeatherData(){
    
    var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=chicago&appid=ef7a9b1e8ad709fb2994f5e8bb08d51b");
        //We then need to convert the data into JSON formaT
    var weatherData=await response.json();
    
    var mainElement=document.querySelector("weather_cities");
    mainElement.innerHTML = 








}