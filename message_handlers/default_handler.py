import sys
sys.path.append("../")

import settings

def help(messaging_adaptor, user, channel, to_ignore):
	button_commands = [settings.ACTIVATE_TOKEN, settings.MATCH_TOKEN, settings.COMPLETE_TOKEN, settings.DEACTIVATE_TOKEN]
	message = "Please choose one of the following actions:"
	fail_message = "You were unable to choose an action. Please try again in some time."
	messaging_adaptor.send_message_with_buttons(channel, message, fail_message, button_commands, button_commands, button_commands)
