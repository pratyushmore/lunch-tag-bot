import json
import settings, utils
from message_handlers.default_handler import help

def lambda_handler(event, context):
	try:
		user, message, other_text, channel = parse_request(event)
		route_request(user, message, other_text, channel)
		return create_lambda_proxy_response(False, 200, {}, {})
	except:
		return create_lambda_proxy_response(False, 500, {}, {})

def parse_request(request):
	if request['type'] == settings.BUTTON_CLICK_IDENTIFIER:
		user = request['user']['id']
		message = request['actions'][0]['name']
		other_text = request['actions'][0]['value']
		channel = request['channel']['id']
	else:
		message_event = request['event']
		user, full_message = message_event['user'], message_event['text']
		other_text, channel = "", message_event['channel']
		message = utils.remove_botname_from_message(full_message)
	return user, message, other_text, channel

def route_request(user, message, other_text, channel):
	func = settings.message_to_function.get(message.strip().lower(), help)
	func(user, channel, other_text)

def create_lambda_proxy_response(is_base_64_encoded, status_code, headers, payload):
	return {
        "isBase64Encoded": is_base_64_encoded,
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(payload)
    }

req = {
    "token": "one-long-verification-token",
    "team_id": "T061EG9R6",
    "api_app_id": "A0PNCHHK2",
    "event": {
        "type": "message",
        "user": "U061F7AUR",
        "text": "Activate",
        "ts": "1525215129.000001",
        "channel": "D0PNCRP9N",
        "event_ts": "1525215129.000001",
        "channel_type": "app_home"
    },
    "type": "event_callback",
    "authed_teams": [
        "T061EG9R6"
    ],
    "event_id": "Ev0PV52K25",
    "event_time": 1525215129
}

lambda_handler(req, None)
