
def deactivate(messaging_adaptor, user, channel, to_ignore):
	messaging_adaptor.send_message(channel, "You are no longer being matched for Lunch Tag :( Come back soon!")
