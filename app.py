from chalice import Chalice, Rate
from requests_html import HTMLSession
import json

app = Chalice(app_name='scrape')

# Automatically runs every 5 minutes
# @app.schedule(Rate(5, unit=Rate.MINUTES))
@app.route("/local-test")
def periodic_task():
    session = HTMLSession()
    url = 'https://sal.livebytes.co.uk/tc/MonGenApp/gen'
    resp = session.get(url)

    monster_generator_descriptions = resp.html.find(".w3-padding-32")

    descriptions = []

    for description in monster_generator_descriptions:
        descriptions.append(description.text[3:])

    return json.dumps(descriptions)