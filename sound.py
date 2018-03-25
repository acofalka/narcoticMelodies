class Sound(object):
    def __init__(self, string_sound):
        self.string_sound = string_sound

    def check_sound(self):
        if len(self.string_sound) != 2:
            return False
        lower = self.string_sound.lower()
        if lower[0] not in "cdefgah":
            return False
        n = self.string_sound[1]
        if not n.isdigit() or int(n) not in range(2, 9):
            return False
        else:
            return True

    def to_number(self):
        if not self.check_sound():
            exit(0)
        number = 12 * int(self.string_sound[1])
        lower = self.string_sound.lower()
        letters = 'c d ef g a h'
        number += letters.index(lower[0])
        return number