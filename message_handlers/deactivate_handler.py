
def deactivate(messaging_adaptor, user, channel, to_ignore):
	messaging_adaptor.send_message(user, "You are no longer being matched for Lunch Tag :( Come back soon!", channel)
