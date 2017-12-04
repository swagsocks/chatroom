from channels import include

# This function will display all messages received in the console
def message_handler(message):
    print(message['text'])


channel_routing = [
    # Include sub-routing from an app.
    include("chat.routing.websocket_routing", path=r"^/chat/stream"),

    # Custom handler for message sending (see Room.send_message).
    # Can't go in the include above as it's not got a 'path' attribute to match on.
    include("chat.routing.custom_routing"),

    # A default "http.request" route is always inserted by Django at the end of the routing list
    # that routes all unmatched HTTP requests to the Django view system. If you want lower-level
    # HTTP handling - e.g. long-polling - you can do it here and route by path, and let the rest
    # fall through to normal views.
]
