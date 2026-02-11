# Movie Showtime Notifier

A full-stack web application that allows users to search for a movie and location, view showtime availability, and receive **instant Telegram notifications** 
when showtimes are found.

🔗 Live Demo: https://movie-notifier-j5c5.onrender.com  


## 🚀 Features
-  Search movies by **name and location**
-  Fetch real movie data using **TMDB API**
-  Display **theatre showtimes** based on location (demo data)
-  Send **instant Telegram notification** when showtimes are available
-  Fully **deployed on Render cloud**
-  Secure handling of **API keys using environment variables**


## 🛠️ Tech Stack
Frontend
- HTML
- Jinja Templates (Flask)

Backend
- Python
- Flask

APIs & Integrations
- TMDB Movie API
- Telegram Bot API

Deployment & Tools
- Git & GitHub
- Render (Cloud Deployment)
- Gunicorn (Production server)


## 📂 Project Structure
movie-notifier/
│
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│ └── index.html
└── README.md

1️⃣ Clone the repository
  -in bash
    -git clone https://github.com/YOUR_USERNAME/movie-notifier.git
    -cd movie-notifier

2️⃣ Create virtual environment
  -python -m venv venv
  -venv\Scripts\activate   # Windows

3️⃣ Install dependencies
  -pip install -r requirements.txt

4️⃣ Create .env file with this values
  -API_KEY=your_tmdb_api_key
  -TELEGRAM_TOKEN=your_bot_token
  -TELEGRAM_CHAT_ID=your_chat_id

5️⃣ Run the app, click and open the ip address

☁️ Deployment

- This project is deployed on Render using:
- requirements.txt for dependencies
- Procfile with Gunicorn
- Environment variables for secrets

🎯 Learning Outcomes
- Built a full-stack Flask application
- Integrated third-party APIs
- Implemented real-time Telegram notifications
- Managed secure environment variables
- Deployed a production-ready cloud application

👨‍💻 Author
Anand Bandela
Project: Movie Showtime Notifier

⭐ Future Improvements
- Real theatre data scraping (BookMyShow, District, etc.)
- User accounts & database storage
- AI-based movie recommendations
- Modern responsive UI design
