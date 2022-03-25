ScriptName = "The Summit"
Website = "https://"
Description = "Minigame about climbing the stairs"
Creator = "Avantgardian"
Version = "0.1"

def Init():
    return


def Execute(data):
    if data.GetParam(0) != "!pyramid":
        return
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
