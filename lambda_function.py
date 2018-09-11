import json
import settings
from function_routes import message_to_function
from message_handlers.default_handler import help
from platform_adaptors.factory import get_adaptor

def lambda_handler(event, context):
	print event
	messaging_adaptor = get_adaptor(settings.MESSAGING_PLATFORM)
	req_body = messaging_adaptor.to_dict(event["body"])
	if messaging_adaptor.should_respond(req_body):
		user, command, other_text, channel = messaging_adaptor.parse_request(req_body)
		route_request(messaging_adaptor, user, command, other_text, channel)
	return create_lambda_proxy_response(False, 200, {}, {})

def route_request(messaging_adaptor, user, command, other_text, channel):
	func = message_to_function.get(command.strip().lower(), help)
	func(messaging_adaptor, user, channel, other_text)

def create_lambda_proxy_response(is_base_64_encoded, status_code, headers, payload):
	return {
        "isBase64Encoded": is_base_64_encoded,
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(payload)
    }

req = {
	"body" : json.dumps({
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
	})
}

lambda_handler(req, None)
