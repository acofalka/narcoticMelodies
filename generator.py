import random
import string
from miditime.miditime import MIDITime
from sound import *
from patterns import *

class Generator(object):

    def __init__(self, location, tempo, duration, mode, start, end, maxlength):
        if location:
            if location[len(location) - 1] != '/':
                self.location = location + '/'
            else:
                self.location = location
        else:
            self.location = ''
        if tempo:
            self.tempo = tempo
        else:
            self.tempo = 300
        if duration:
            self.duration = duration
        else:
            self.duration = 120
        if mode != None:
            self.mode = mode
        else:
            self.mode = 1
        if start:
            sound_start = Sound(start)
            self.start = sound_start.to_number()
        else:
            self.start = 24
        if end:
            sound_end = Sound(end)
            self.end = sound_end.to_number()
        else:
            self.end = 108
        if maxlength:
            self.maxlength = maxlength
        else:
            self.maxlength = 2

    def generate_filename(self):
        filename = ""
        for i in range(10):
            random_char = random.choice(string.ascii_uppercase + string.digits)
            filename += random_char
        filename += ".mid"
        return filename

    def generate(self):
        filename = self.generate_filename()
        mymidi = MIDITime(self.tempo, self.location + filename)
        if self.mode == 0:
            midinotes = self.mode0()
        elif self.mode == 1:
            midinotes = self.mode1()
        else:
            midinotes = self.mode2()
        mymidi.add_track(midinotes)
        mymidi.save_midi()

    def mode0(self):
        midinotes = []
        beats = self.duration / 60 * self.tempo
        i = 0
        while i < beats:
            random_sound = random.randint(self.start, self.end)
            random_time = random.randint(1, self.maxlength)
            midinotes.append([i, random_sound, 127, random_time])
            i += random_time
        i = 0
        random_number = random.randint(0, 12)
        i += random_number
        while i < beats:
            random_sound = random.randint(self.start, self.end)
            random_time = random.randint(1, self.maxlength)
            midinotes.append([i, random_sound, 127, random_time])
            random_number = random.randint(0, 12)
            i += random_number
            i += random_time
        return midinotes

    def mode1(self):
        midinotes = []
        beats = self.duration / 60 * self.tempo
        i = 0
        patterns = Patterns()
        while i < beats:
            random_mode = random.randint(0,1)
            if random_mode == 0:
                random_sounds = random.randint(4, 16)
                while random_sounds > 0:
                    random_sound = random.randint(self.start, self.end)
                    random_time = random.randint(1, self.maxlength)
                    midinotes.append([i, random_sound, 127, random_time])
                    i += random_time
                    random_sounds -= 1
                    if i >= beats:
                        break
            else:
                pattern = patterns.random_pattern()
                random_sound = random.randint(self.start, self.end)
                repeat = random.randint(1, 4)
                for j in range(repeat):
                    random_time = random.randint(1, self.maxlength)
                    midinotes.append([i + random_time, random_sound + 6, 127, random_time])
                    for n in range(0, len(pattern)):
                        random_time = random.randint(1, self.maxlength)
                        midinotes.append([i + random_time, random_sound + pattern[n], 127, random_time])
                        i += random_time
                        if i >= beats:
                            break
        return midinotes

    def mode2(self):
        midinotes = []
        beats = self.duration / 60 * self.tempo
        i = 0
        patterns = Patterns()
        while i < beats:
            pattern = patterns.random_pattern()
            random_sound = random.randint(self.start, self.end)
            repeat = random.randint(1, 4)
            for j in range(repeat):
                random_time = random.randint(1, self.maxlength)
                midinotes.append([i + random_time, random_sound + 6, 127, random_time])
                for n in range(0, len(pattern)):
                    random_time = random.randint(1, self.maxlength)
                    midinotes.append([i + random_time, random_sound + pattern[n], 127, random_time])
                    i += random_time
                    if i >= beats:
                        break
        return midinotes