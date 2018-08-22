
def match(messaging_adaptor, user, channel, to_ignore):
	matched_user, matched_user_channel = "TODO", "TODO"
	messaging_adaptor.send_message(user, "You have been matched with" + matched_user + " for Lunch Tag. Please schedule lunch with them,"
									+ "and once you have met, message me back saying `complete`!", channel)
	messaging_adaptor.send_message(matched_user, "You have been matched with" + matched_user + " for Lunch Tag. Please schedule lunch with them,"
									+ "and once you have met, message me back saying `complete`!", matched_user_channel)
