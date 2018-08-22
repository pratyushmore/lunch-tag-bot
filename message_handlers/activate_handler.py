sys.path.append("../")

import constants, settings

def activate(messaging_adaptor, user, channel, to_ignore):
	button_commands = [constants.LOCATION_TOKEN] * len(settings.LOCATIONS)
	button_labels = settings.LOCATIONS
	message = "Please choose the location you want to be active in:"
	messaging_adaptor.send_message_with_buttons(channel, message, button_commands, button_labels, button_labels)
