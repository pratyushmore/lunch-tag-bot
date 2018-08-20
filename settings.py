from message_handlers.activate_handler import activate
from message_handlers.deactivate_handler import deactivate
from message_handlers.complete_handler import complete
from message_handlers.match_handler import match
from message_handlers.location_handler import location

ACTIVATE_TOKEN = "activate"
DEACTIVATE_TOKEN = "deactivate"
COMPLETE_TOKEN = "complete"
MATCH_TOKEN = "match"

message_to_function = {
	ACTIVATE_TOKEN : activate,
	DEACTIVATE_TOKEN : deactivate,
	COMPLETE_TOKEN : complete,
	MATCH_TOKEN: match
}

BUTTON_CLICK_IDENTIFIER = "interactive_message"
