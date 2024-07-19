const baseUrl = 'http://localhost';
console.log(baseUrl);

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

const city = getCookie('city');

const last_city = document.getElementById('last_city');
const previous = document.getElementById('previous');

if (last_city && city){
    previous.style.display = 'flex';
    last_city.innerHTML = `Do you want to see weather in ${capitalizeFirstLetter(city)}`;
    last_city.style.marginRight = '1vw';

    const show_previous = document.getElementById('show_previous');
    const close_previous = document.getElementById('close_previous');
    

    show_previous.addEventListener('click', (event) => {
        event.preventDefault();
        window.location.href = `${baseUrl}/weather/${city}/`;
    });

    close_previous.addEventListener('click', (event) => {
        event.preventDefault();
        previous.style.display = 'none';
    })
}
const search_input = document.getElementById('search_input');
const suggestions = document.getElementById('suggestions');
var wait = false;

search_input.addEventListener('input', async (event) => { 
    if (event.target.value && !wait){
        wait = true;

        url = `/search/${event.target.value}`;
        const response = await fetch(url, {
            method: 'GET'
        });
        
        if (response.ok){
            const data = await response.json();
            suggestions.innerHTML = '';

            var len = 3;
            for (var i = 0; i < len; i++){
                var city = data.matches[i];
                if (!city) break;
                suggestions.innerHTML += `<div class="suggestion">${data.matches[i]}</div>`;
            }

            addListenerSuggestions();
        }

        wait = false;
    };
})

search_input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        window.location.href = `${baseUrl}/weather/${event.target.value}/`;
    }
});

function addListenerSuggestions(){
    const suggestion = document.getElementsByClassName('suggestion');

    var len = suggestion.length;
    for (var i = 0; i < len; i++){
        suggestion[i].addEventListener('click', (event) => {
            var city_slug = event.target.innerHTML.toLowerCase();
            window.location.href = `${baseUrl}/weather/${city_slug}/`
        })
    }
}