from twilio_net_neutrality import app
from twilio_net_neutrality.controller import index


app.add_url_rule('/', 'index', index)
