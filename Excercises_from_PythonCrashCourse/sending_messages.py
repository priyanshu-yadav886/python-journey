def send_messages(sh_messages, sent_messages):
    """Print each text message
    and move it to a new list.
    """
    while sh_messages:
        message = sh_messages.pop()
        print(f"Message : {message}")
        sent_messages.append(message)


def show_sent_messages(sent_messages):
    """Show all the messages that were printed"""
    print(f"\nThe following messages were sent: ")
    for messages in sent_messages:
        print(messages)


sh_messages = ['hello', 'hi', 'bye']
sent_messages = []

send_messages(sh_messages[:], sent_messages)
show_sent_messages(sent_messages)

print(sh_messages)