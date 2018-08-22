def location(messaging_adaptor, user, channel, location):
	message = "Your location has been set to `{}`. You are ready to be matched for Lunch Tag :)".format(location)
	messaging_adaptor.send_message(channel, message)
