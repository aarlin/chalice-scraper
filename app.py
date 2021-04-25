from chalice import Chalice, Rate
import requests

app = Chalice(app_name='twilio_to_discord')

@app.route('/sms', methods=['POST'])
def periodic_task():
    print(app.current_request.json_body)
    body = request.values.get('Body', None)
    number = request.form['From']
    message_body = request.form['Body']

    url = "<DISCORD_WEBHOOK_URL>"

    data["content"] = message_body
    data["username"] = number

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

    return "200"
    
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