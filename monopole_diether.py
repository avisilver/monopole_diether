"""
An Implementation of the Monopoly Deal card game
"""

# import os
# from collections import defaultdict
# import itertools
import pprint

from lib.number_cards import *
from lib.action_cards import *
from lib.game_area import GameArea
from lib.game import Game

def main():
    print(OneCard())
    print(TwoCard())


    game = Game(num_players=2)
    print(game)
    
    game_area = GameArea()
    print(game_area)
    print(game_area.main_deck)
    pprint.pprint(game_area.play_pile)


if __name__ == "__main__":
    main()

#     english_words = load_words()

# MAIN_WORDS_FILE = "words_alpha.txt"
# FOUR_LETTERS_AND_UP_FILE = "four_letters_and_up.txt"

# def load_word_file(filename):
#     with open(filename, 'rt') as word_file:
#         valid_words = sorted(set(word_file.read().split()))
#     print(f"Loaded {len(valid_words)} words from {filename}")
#     return valid_words


# def load_words():
#     """Get a list of English words that are four letters long or longer, caching them in a file"""
#     if os.path.exists(FOUR_LETTERS_AND_UP_FILE):
#         return load_word_file(FOUR_LETTERS_AND_UP_FILE)
#     else:
#         all_words = load_word_file(MAIN_WORDS_FILE)
#         four_letter_words = [word for word in all_words if len(word) >= 4]
#         print(len(four_letter_words))
#         with open(FOUR_LETTERS_AND_UP_FILE, 'wt') as word_file:
#             word_file.write("\n".join(four_letter_words))
#         return load_word_file(FOUR_LETTERS_AND_UP_FILE)


# def score(word: str, is_pangram: bool=False) -> int:
#     """
#     4-letter words are worth 1 point each.
#     Longer words earn 1 point per letter.
#     Each puzzle includes at least one "pangram" which uses every letter. These are worth 7 extra points!
#     """
#     return len(word) - 3 + (7 if is_pangram else 0)

# _line = ("-" * 80) + "\n"

# def spelling_bee(central_letter, other_letters, english_words):

#     puzzle_set = set(list(central_letter) + list(other_letters))
#     print(puzzle_set)
#     assert len(puzzle_set) == 7

#     print("Pangrams first:\n", _line)
#     pangrams = set()
#     for word in english_words:
#         if central_letter in word and set(word) == puzzle_set:
#             pangrams.add(word)

#     print("\n".join(f"{word}, {score(word, True)}" for word in sorted(pangrams)))

#     print("Nonpangrams:\n", _line)
#     other_words = set()
#     words_by_score = defaultdict(set)
#     for word in english_words:
#         if len(word) > 3 and word not in pangrams and central_letter in word and set(word).issubset(puzzle_set):
#             other_words.add(word)
#             words_by_score[score(word)].add(word)
#     #print("\n".join(f"{word}, {score(word)}" for word in sorted(other_words)))
#     for wordscore in sorted(words_by_score):
#         words = sorted(words_by_score[wordscore])
#         # len(words) * wordscore
#         # print (f"\n\tWords with score = {wordscore}:\n\t{words}")
#         print (f"\n\tWords with score = {wordscore}:")
#         padding = max(2, 7 - wordscore)
#         col_width = max(len(word) for word in words) + padding
#         num_columns = 5
#         for row in itertools.batched(words, num_columns):
#             print ("\t", "".join(word.ljust(col_width) for word in row))

#         # col_width = max(len(word) for row in data for word in row) + 2  # padding

#     # five_letter_words = sorted(word for word in english_words if len(word) == 5)
#     # print(len(five_letter_words))
#     # # for word in five_letter_words:
#     #     # print(word)

#     # with open('five_letter_words.txt', 'wt') as five_word_file:
#     #     five_word_file.writelines("\n".join(five_letter_words))
#     #     # for word in five_letter_words:
#     #     #     five_word_file.write(word)
#     #     #     five_word_file.write('\n')

# if __name__ == '__main__':
#     english_words = load_words()
#     # demo print
#     # print('fate' in english_words)

#     # 19th Aug 2024
#     # spelling_bee(central_letter='h', other_letters="pyotra", english_words=english_words)
#     # 20th Aug 2024
#     # spelling_bee(central_letter='p', other_letters="nixheo", english_words=english_words)
#     # 21st Aug 2024 - I got to Genius, including three pangrams, before running this.
#     # spelling_bee(central_letter='b', other_letters="laming", english_words=english_words)
#     # 25th Aug 2024 - I got to Amzing, and didn't find the pangram.
#     # spelling_bee(central_letter='f', other_letters="teilom", english_words=english_words)
#     # 29th Aug 2024 - I got to Amazing, used anagram solver to get to Genius, then this to get Queen Bee with the last three or four words
#     # spelling_bee(central_letter='w', other_letters="hatorn", english_words=english_words)
#     # 1st Sep 2024 - I got to Great
#     # From me: Abandon Banana Band Bank Baobab Dank Haka Hand Handbook Hank Hookah Kabob
#     # From this program: Bandana Bandanna nana khan adobo babka - Genius at that point
#     # From this program: baboon doodad haboob
#     # Then I thought of one: anon
#     # From this program: ankh baba boba koan nada nabob
#     # i found naan from a hint for queen bee
#     # spelling_bee(central_letter='a', other_letters="nobdhk", english_words=english_words)

#     # 2nd Sep 2024 - I got to Great
#     # From me: cede code codeine coin coincide conincided coined cone conic conjoin conjoined (pangram) decide decided deco decode deicide dice diced ecocide encode iced nice nonce once
#     # From this program: coincidence innocence incidence ionic condone condoned conceded concede cocoon cocooned (got to Amazing in the last two or three words)
#     # From this program: encoded (got to Genius)
#     # From this program: decoded icon iconic deiced conned niece deice cooed coned condo codon coded cocci ceded coed
#     # From clue "new conservative" - neocon
#     # spelling_bee(central_letter='c', other_letters="inojed", english_words=english_words)

#     # CONCLUSION:
#     #  need an updated list of words, and one with upper case characters so that I can optionally exclude proper nouns


#     # 6nd Sep 2024 - I got to Nice
#     # From me: Devil, deviled, dive, divide, divided,dived, dove, evil, five, levee, live, lived, livid, love, loved, video, videoed, vile, vilified, viol, voile, vole
#     # From this program: void, veil, vied, delve (great), delved, olive ovoid vivid devoid (amazing) evolve
#     # Me: levied
#     # From this program: veiled fivefold voodoo (genius) voided level leveled
#     #
#     # spelling_bee(central_letter='v', other_letters="floeid", english_words=english_words)


#     # 2nd Sep 2024 - I got to Great
#     # From me: city clkod clot cloy codicil coil cold coldly colloid colt cool colly coot coyly illicit licit
#     # From this program: icily licitly loco loci cocci colic idyllic idiotic (genius)
#     # From this program: illicitly cyclic docility (pangram)
#     # From this program: idiocy (queen bee)
#     # 28 words 126 points
#     spelling_bee(central_letter='c', other_letters="toylid", english_words=english_words)
