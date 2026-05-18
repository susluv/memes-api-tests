import random


def fake_token():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    token = "".join([random.choice(chars) for n in range(15)])
    return token
