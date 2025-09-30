
def rule_base(user_message: str) -> str : 


    if "hi" in user_message.lower():
        bot_response = "Hello"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye"
    else:
        bot_response = "I do not understand "

    return     bot_response
