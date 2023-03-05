"""To save the APIs header format."""

from src.config import RAPID_API_KEY

joke_api = {
    "url": "https://dad-jokes.p.rapidapi.com/random/joke",
    "headers": {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
    },
}
quote_api = {
    "url": "https://quotes15.p.rapidapi.com/quotes/random/",
    "headers": {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
    },
}
