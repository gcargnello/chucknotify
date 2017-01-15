import json
import requests
from Modules import html_decode
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/')

# The parameters included in a slash command request (with example values):
#   token=gIkuvaNzQIHg97ATvDxqgjtO
#   team_id=T0001
#   team_domain=example
#   channel_id=C2147483705
#   channel_name=test
#   user_id=U2147483697
#   user_name=Steve
#   command=/weather
#   text=94070
#   response_url=https://hooks.slack.com/commands/1234/5678



##################################################
# LEGGE UN WITZ CHUCK NORRIS E LO MANDA A SLACK
##################################################
def witz_to_slack():

    # PROCEDURA MAIN recupera un witz a caso
    url = 'http://api.icndb.com/jokes/random'

    r = requests.get(url)

    if r.status_code != 200:
        pass
        witz = 'Non ne ho una da raccontare...'
    else:
        full_json = r.text
        full = json.loads(full_json)
        witz = (full['value']['joke'])

    # togli i cartteri escape
    witz = html_decode(witz)
    print ('W:',witz)


    # e adesso inviala a slack
    url_wh = 'https://hooks.slack.com/services/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'

    usr = "WitzBOT"
    icon = ":hugging_face:"
    msg = "La sai l'ultima?"
    text_a = witz
    text_b = ""
    channel = "vacanze"


    payload = {'user' : usr,
               'icon_emoji': icon,
               'text':      msg,
               'channel':   channel,
               'attachments': [
                                {   "color": "#36a64f",
                                    'text': text_a,
                                    'pretext': text_b,
                                    'author_name': "Chuck Norris",
                                    'author_link': "http://www.icndb.com/"
    #                                'author_icon': "http://flickr.com/icons/bobby.jpg"
                                }
                              ]
               }


    # esegue chiamata
    r = requests.put(url_wh,data = json.dumps(payload),
                     headers={'Content-Type': 'application/json'}
                    )

    # controlla esito
    if (r.status_code != 200):
        print ('Errore di connessione')
        print (r.text)
    else:   
        print (r.text)

    return '<h1>Inviato messaggio</h1>'
