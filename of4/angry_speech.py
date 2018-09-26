
def angry_speech():
    speech = input("Hva vil du si?")
    speech = speech.upper()
    speech = speech + "!"
    return speech


angry = angry_speech()
print(angry)
print(angry_speech())
