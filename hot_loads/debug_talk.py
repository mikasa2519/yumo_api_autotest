import random


class DebugTalk:

    def get_random(self, min, max):
        return random.randint(min, max)


if __name__ == '__main__':
    print(DebugTalk().get_random(10000, 99999))
