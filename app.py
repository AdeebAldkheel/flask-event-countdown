from flask import Flask, render_template
from events import get_next_event_days

app = Flask(__name__)

@app.route("/")
def index():
    result = get_next_event_days()
    if result:
        title, days = result
        ar_suffix = "يوم"
        message = f'الحدث التالي: "{title}", بعد {days} {ar_suffix}.'
    else:
        message = "No upcoming events found."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    # Listen on 0.0.0.0:5000 by default. Adjust host/port as needed.
    app.run(host="0.0.0.0", port=5000, debug=True)