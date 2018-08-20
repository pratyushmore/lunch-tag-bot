def remove_botname_from_message(full_message):
	message_parts = full_message.split()
	if len(message_parts) == 1:
		return full_message
	else if '@' in message_parts[0]:
		return ' '.join(message_parts[1:])
