
def activate(messaging_adaptor, user, channel, to_ignore):
	# TODO: Add buttons here for location!
	messaging_adaptor.send_message(user, "Please choose the location you want to be active in:", channel)
