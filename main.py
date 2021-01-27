import random
import time

Word_1 = ["A", "The", "One", "Jerry", "Bob", "Ann", "Susan", "An", "Once", "I", "Discovering"]
Word_2 = ["banana", "walked", "once", "I", "the", "ran", "inhalers"]
Word_3 = ["and", "saw", "found", "a", "down", "up", "instigated", "Donald"]
Word_4 = ["Trump", "and", "the", "started", "a", "it", "his", "her", "life"]
Word_5 = ["and", "saw", "math", "Nerf", "Helen", "French", "janitor", "search", "tube"]
Word_6 = ["back", "come", "Gun,", "for", "help", "my", "and", "narcotics"]
Word_7 = ["mother.", "narcotics.", "celebrate.", "died.", "help."]

print("A RANDOM 7-WORD SENTENCE GENERATOR")
print()
time.sleep(1.25)

print("If you manage to find a sentence that makes sense or is just really funny, tell me urgently.")
print()
time.sleep(1.85)

print("Here is your sentence:")
print()
time.sleep(2)

Word_1 = random.choice(Word_1)
Word_2 = random.choice(Word_2)
Word_3 = random.choice(Word_3)
Word_4 = random.choice(Word_4)
Word_5 = random.choice(Word_5)
Word_6 = random.choice(Word_6)
Word_7 = random.choice(Word_7)
print(Word_1, Word_2, Word_3, Word_4, Word_5, Word_6, Word_7)