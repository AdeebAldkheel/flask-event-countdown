# 📆 Hijri Event Countdown App

This is a simple Flask web app that displays the next upcoming educational event (based on the [Saudi Ministry of Education RSS feed](https://moe.gov.sa/ar/education/generaleducation/Pages/rss.aspx)). It parses Hijri dates, converts them to Gregorian, and calculates how many days remain until the next event.

## 🚀 Features

* Fetches event titles and Hijri dates from the official RSS feed.
* Converts Hijri to Gregorian dates.
* Displays how many days remain until the next event.
* Arabic support in output.
* Lightweight and minimal Flask app.

## 📦 Requirements

* Python 3.8+
* Required packages:

  ```bash
  pip install flask beautifulsoup4 requests hijri-converter
  ```

## 🛠️ File Structure

```
.
├── app.py               # Flask web server
├── events.py            # Contains logic to fetch and process event dates
├── templates/
│   └── index.html       # HTML template to render the result
└── README.md
```

## 🏁 How to Run

```bash
python app.py
```

Then open your browser at: [http://localhost:5000](http://localhost:5000)

## 🌍 Deployment

To run on all interfaces (e.g. inside Docker or on a server):

```bash
python app.py
# or ensure: app.run(host="0.0.0.0", port=5000)
```

## 📝 Notes

* If no valid event is found or parsing fails, a fallback message will be shown.
* RSS feed format is subject to change by the Ministry, which may break parsing.