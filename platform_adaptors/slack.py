import sys
sys.path.append("../")

from slackclient import SlackClient
import settings

BUTTON_CLICK_IDENTIFIER = "interactive_message"

class SlackAdaptor(object):
	def __init__(self):
		self.sc = SlackClient(settings.SLACK_API_TOKEN)

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

	def send_message(self, user, message, channel):
		sc.api_call(
			"chat.postMessage",
			channel=channel,
			text=message
		)
		print message

	def send_message_with_buttons(self, user, message, button_use, labels, values):
		actions = []
		for label, value in zip(labels, values):
			action = {
				"name": button_use,
				"text": label,
				"type": "button",
				"value": value
			}
			actions.append(action)
		attachments =[
			{
				"fallback": "You were unable to choose a location."
				"callback_id": "random-unused",
				"actions": actions
			}
		]
		sc.api_call(
			"chat.postMessage",
			channel=channel,
			text=message,
			attachments=attachments
		)
		print message, attachments

	def remove_botname_from_message(self, full_message):
		message_parts = full_message.split()
		if len(message_parts) == 1:
			return full_message
		elif '@' in message_parts[0]:
			return ' '.join(message_parts[1:])
