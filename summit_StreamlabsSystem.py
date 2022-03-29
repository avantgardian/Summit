ScriptName = "The Summit"
Website = "https://"
Description = "Minigame about climbing the stairs"
Creator = "Avantgardian"
Version = "0.1"
Command = "!pyramid"

def Init():
    return


def Execute(data):
    log("Entering execution")
    if data.GetParam(0) != Command:
        return
    
    username = data.UserName

    if is_pyramid():
        send_message("Yes, you are a pyramid " + username + "!!!")
    else:
        send_message("Oops " + username + ", seems you are not a pyramid")
    log("Exiting execution")
    return


def Tick():
    return


def is_pyramid():
    pyramid_probability = 10
    random_chance = Parent.GetRandom(0, 100)
    return random_chance <= pyramid_probability


def send_message(message):
    Parent.SendStreamMessage(message)
    return


def log(message):
    Parent.log(Command, message)
    return
