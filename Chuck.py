import json
import requests
from Modules import html_decode
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route('/', methods=['POST'])
#@app.route('/')

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


    # e adesso inviala a slack via slash command
    usr = "WitzBOT"
    icon = ":hugging_face:"
    msg = "La sai l'ultima?"
    text_a = witz
    text_b = ""
    channel = "vacanze"


    payload = {'user' : usr,
               'icon_emoji': icon,
               'text':      msg,
               'attachments': [
                                {   "color": "#36a64f",
                                    'text': text_a,
                                    'pretext': text_b,
                                    'author_name': "Chuck Norris",
                                    'author_link': "http://www.icndb.com/"
                                }
                              ]
               }

#   restituisce il messaggio di ritorno
#    return('messaggio di ritorno')
#    return text_a
    return payload
    print (payload)
