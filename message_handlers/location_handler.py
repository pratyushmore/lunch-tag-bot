def location(messaging_adaptor, user, channel, location):
	messaging_adaptor.send_message(user, "Your location has been set to " + location + ". You are ready to be matched for Lunch Tag :)", channel)
