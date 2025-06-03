import re
import requests
import datetime
from bs4 import BeautifulSoup
from hijri_converter import Hijri

RSS_URL = "https://moe.gov.sa/ar/education/generaleducation/Pages/rss.aspx"

def get_next_event_days(rss_url=RSS_URL):
    """
    1. Download the HTML page.
    2. Find all <li> elements under the first <ul> (each <li> contains an event title and a Hijri date).
    3. Extract the Hijri date (DD/MM/YYYY) and the title.
    4. Convert Hijri → Gregorian, then compute days until that Gregorian date.
    5. Return the title and diff(days) of the upcoming event.
    """
    resp = requests.get(rss_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, "html.parser")

    ul = soup.find("ul")
    if not ul:
        return None

    today = datetime.date.today()
    next_title = None
    next_diff = None

    for li in ul.find_all("li"):
        text = li.get_text(separator=" ").strip()
        m = re.search(r"(\d{2}/\d{2}/\d{4})", text)
        if not m:
            continue

        hijri_str = m.group(1)
        title = text.replace(hijri_str, "").strip()

        d_h, m_h, y_h = map(int, hijri_str.split("/"))
        g = Hijri(y_h, m_h, d_h).to_gregorian()
        event_date = datetime.date(g.year, g.month, g.day)

        diff = (event_date - today).days
        if diff >= 0 and (next_diff is None or diff < next_diff):
            next_diff = diff
            next_title = title

    if next_title is None:
        return None

    return next_title, next_diff