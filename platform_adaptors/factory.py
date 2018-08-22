import sys
sys.path.append("../")

import constants
from platform_adaptors.slack import SlackAdaptor

def get_adaptor(messaging_platform):
	if messaging_platform == constants.SLACK_PLATFORM:
		return SlackAdaptor()
	raise Exception
