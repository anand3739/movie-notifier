from flask import Flask, render_template, request
import requests
import os
import schedule
import time
import threading
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

last_checked = {}


def send_telegram_notification(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Telegram credentials are missing; notification skipped.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
    }

    try:
        requests.post(url, data=data, timeout=5)
        print("Telegram message sent.")
    except Exception as e:
        print("Telegram error:", e)


def check_showtimes():
    global last_checked

    for key, data in last_checked.items():
        movie = data["movie"]
        location = data["location"]

        print(f"Checking showtimes for {movie} in {location}...")

        # Here we simulate checking
        # (later we connect real website/API)
        message = f"Showtimes available for {movie} in {location}."
        print(message)

        send_telegram_notification(message)


@app.route("/", methods=["GET", "POST"])
def home():
    movie_data = None
    showtimes = []
    status_message = None
    error_message = None
    search = {"movie": "", "location": ""}

    if request.method == "POST":
        movie = request.form.get("movie", "").strip()
        location = request.form.get("location", "").strip()
        search = {"movie": movie, "location": location}

        if not movie or not location:
            error_message = "Please enter both movie name and location."
            return render_template(
                "index.html",
                movie=movie_data,
                showtimes=showtimes,
                search=search,
                status_message=status_message,
                error_message=error_message,
            )

        user_key = f"{movie}_{location}"
        last_checked[user_key] = {"movie": movie, "location": location}

        # ---- TMDB API CALL ----
        if API_KEY:
            url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
            try:
                response = requests.get(url, timeout=5)
                response_data = response.json()
            except requests.exceptions.RequestException:
                response_data = {}

            if "results" in response_data and response_data["results"]:
                movie_data = response_data["results"][0]
            else:
                status_message = f"No movie details found for '{movie}'."
        else:
            error_message = "TMDB API key is missing. Add API_KEY to your .env file."

        # ---- DEMO SHOWTIME DATA ----
        demo_theatres = {
            "new york": [
                {"theatre": "AMC Empire 25", "times": ["10:00 AM", "1:30 PM", "6:00 PM"]},
                {"theatre": "Regal Times Square", "times": ["11:00 AM", "3:00 PM", "9:00 PM"]},
            ],
            "london": [
                {"theatre": "Odeon Leicester Square", "times": ["12:00 PM", "4:00 PM", "8:00 PM"]},
            ],
            "hyderabad": [
                {"theatre": "AMB Cinemas", "times": ["10:30 AM", "2:00 PM", "7:00 PM"]},
                {"theatre": "PVR Nexus Mall", "times": ["11:15 AM", "3:30 PM", "9:45 PM"]},
            ],
        }

        showtimes = demo_theatres.get(location.lower(), [])

        if showtimes:
            message = f"Showtimes available for {movie} in {location}."
            send_telegram_notification(message)
            status_message = f"Found {len(showtimes)} theatres in {location.title()}."
        elif not status_message:
            status_message = f"No demo showtimes found for {location.title()}."

    return render_template(
        "index.html",
        movie=movie_data,
        showtimes=showtimes,
        search=search,
        status_message=status_message,
        error_message=error_message,
    )


def run_scheduler():
    schedule.every(30).seconds.do(check_showtimes)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    threading.Thread(target=run_scheduler, daemon=True).start()
    app.run(debug=True, use_reloader=False)
