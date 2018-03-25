import argparse
import sys
from sound import *
from generator import *

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--location", help="Lokalizacja dla pliku wyjsciowego")
parser.add_argument("-t", "--tempo", help="Preferowane tempo melodii (1 - 500)", type=int, choices=range(20, 501))
parser.add_argument("-d", "--duration", help="Dlugosc melodii w sekundach (1 - 300)", type=int, choices=range(1, 301))
parser.add_argument("-m", "--mode", help="Tryb generowania melodii: 0/1/2", type=int, choices=[0, 1, 2]) # 0 - tryb losowy, 1 - tryb mieszany (0 + 2), 2 - tryb z uzyciem gotowych wzorcow
parser.add_argument("-s", "--start", help="Poczatek zakresu dzwiekow")
parser.add_argument("-e", "--end", help="Koniec zakresu dzwiekow")
parser.add_argument("-ml", "--maxlength", help="Maksymalna dlugosc dzwieku (1-5)", type=int, choices=range(1, 5))
args = parser.parse_args()

if args.start:
    sound_start = Sound(args.start)
    if (not sound_start.check_sound()):
        print ("Nieprawidlowy format poczatku zakresu dzwiekow")
        sys.exit(0)
if args.end:
    sound_end = Sound(args.end)
    if (not sound_end.check_sound()):
        print ("Nieprawidlowy format konca zakresu dzwiekow")
        sys.exit(0)
if args.start and args.end:
    if sound_start.to_number() > sound_end.to_number():
        print ("Koniec zakresu dzwiekow musi byc za poczatkiem zakresu")
        exit(0)

gen = Generator(args.location, args.tempo, args.duration, args.mode, args.start, args.end, args.maxlength)
gen.generate()


