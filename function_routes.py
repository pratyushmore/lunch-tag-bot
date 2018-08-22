from message_handlers.activate_handler import activate
from message_handlers.deactivate_handler import deactivate
from message_handlers.complete_handler import complete
from message_handlers.match_handler import match
from message_handlers.location_handler import location

import settings, constants

message_to_function = {
	settings.ACTIVATE_TOKEN : activate,
	settings.DEACTIVATE_TOKEN : deactivate,
	settings.COMPLETE_TOKEN : complete,
	settings.MATCH_TOKEN: match,
	constants.LOCATION_TOKEN: location
}
