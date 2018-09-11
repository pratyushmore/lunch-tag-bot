import sys
sys.path.append("../")

from slackclient import SlackClient
import settings
from urlparse import parse_qs
import json

BUTTON_CLICK_IDENTIFIER = "interactive_message"

class SlackAdaptor(object):
	def __init__(self):
		self.sc = SlackClient(settings.SLACK_API_TOKEN)

	def to_dict(self, req_body_string):
		try:
			return json.loads(req_body_string)
		except ValueError:
			return json.loads(parse_qs(req_body_string)['payload'][0])

	def should_respond(self, request):
		if request['type'] == BUTTON_CLICK_IDENTIFIER:
			return True
		if "bot_id" in request['event']:
			return False
		return True

	def parse_request(self, request):
		if request['type'] == BUTTON_CLICK_IDENTIFIER:
			user = request['user']['id']
			command = request['actions'][0]['name']
			other_text = request['actions'][0]['value']
			channel = request['channel']['id']
		else:
			message_event = request['event']
			user, full_message = message_event['user'], message_event['text']
			other_text, channel = "", message_event['channel']
			command = self.remove_botname_from_message(full_message)
		return user, command, other_text, channel

	def send_message(self, channel, message):
		self.sc.api_call(
			"chat.postMessage",
			channel=channel,
			text=message
		)

	def send_message_with_buttons(self, channel, message, fail_message, commands, labels, values):
		actions = []
		for command, label, value in zip(commands, labels, values):
			action = {
				"name": command,
				"text": label,
				"type": "button",
				"value": value
			}
			actions.append(action)
		attachments =[
			{
				"fallback": fail_message,
				"callback_id": "random-unused",
				"actions": actions
			}
		]
		self.sc.api_call(
			"chat.postMessage",
			channel=channel,
			text=message,
			attachments=attachments
		)

	def create_private_group_with_message(self, users, name, message):
		resp = self.sc.api_call(
			"conversations.create",
			name=name,
			is_private=True,
			user_ids=",".join(users)
		)
		if "ok" in resp and resp["ok"]:
			self.send_message(resp["channel"]["id"], message)

	# This does not need to be implemented by another adaptor. It is a helper function
	def remove_botname_from_message(self, full_message):
		message_parts = full_message.split()
		if len(message_parts) == 1:
			return full_message
		elif '@' in message_parts[0]:
			return ' '.join(message_parts[1:])
		else:
			 return full_message
