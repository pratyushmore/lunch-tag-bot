
def match(messaging_adaptor, user, channel, to_ignore):
	matched_user = "TODO"
	name = "lt-{}-{}".format(user.lower()[:4], matched_user.lower()[:4])
	message = "Hello <@{}> and <@{}>. You've been matched for lunch tag! {}".format(
		user,
		matched_user,
		"Please schedule lunch, and once you've met, message me on the app saying `complete`.")
	messaging_adaptor.create_private_group_with_message([user, matched_user], name, message)
