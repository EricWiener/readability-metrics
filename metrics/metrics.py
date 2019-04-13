#!/usr/bin/env python
# modified from https://github.com/mmautner/readability
import math

from metrics.utils import *


class Readability:
    def __init__(self):
        self.char_count = 0
        self.word_count = 0
        self.sentence_count = 0
        self.syllable_count = 0
        self.complex_word_count = 0
        self.long_word_count = 0
        self.avg_words_p_sentence = 0

    def analyze_text(self, text):
        words = get_words(text)
        self.char_count += get_char_count(words)
        self.word_count += len(words)
        self.sentence_count += len(get_sentences(text))
        self.syllable_count += count_syllables(words)
        self.complex_word_count += count_complex_words(text)
        self.long_word_count += count_long_words(words)

    def get_results(self):
        self.avg_words_p_sentence = self.word_count / self.sentence_count

        results_dic = {
            "ARI": self.ARI(),
            "FleschReadingEase": self.FleschReadingEase(),
            "FleschKincaidGradeLevel": self.FleschKincaidGradeLevel(),
            "GunningFogIndex": self.GunningFogIndex(),
            "SMOGIndex": self.SMOGIndex(),
            "ColemanLiauIndex": self.ColemanLiauIndex(),
            "LIX": self.LIX(),
            "RIX": self.RIX(),
        }

        return results_dic

    def clear(self):
        self.char_count = 0
        self.word_count = 0
        self.sentence_count = 0
        self.syllable_count = 0
        self.complex_word_count = 0
        self.long_word_count = 0
        self.avg_words_p_sentence = 0

    def ARI(self):
        score = 0.0
        if self.word_count > 0.0:
            score = 4.71 * (self.char_count / self.word_count) + \
                0.5 * (self.word_count / self.sentence_count) - 21.43
        return score

    def FleschReadingEase(self):
        score = 0.0
        if self.word_count > 0.0:
            score = 206.835 - (1.015 * (self.avg_words_p_sentence)) - \
                (84.6 * (self.syllable_count / self.word_count))
        return round(score, 4)

    def FleschKincaidGradeLevel(self):
        score = 0.0
        if self.word_count > 0.0:
            score = 0.39 * (self.avg_words_p_sentence) + 11.8 * \
                (self.syllable_count / self.word_count) - 15.59
        return round(score, 4)

    def GunningFogIndex(self):
        score = 0.0
        if self.word_count > 0.0:
            score = 0.4 * ((self.avg_words_p_sentence) + (100 *
                                                          (self.complex_word_count / self.word_count)))
        return round(score, 4)

    def SMOGIndex(self):
        score = 0.0
        if self.word_count > 0.0:
            score = (math.sqrt(self.complex_word_count * (30 / self.sentence_count)) + 3)
        return score

    def ColemanLiauIndex(self):
        score = 0.0
        if self.word_count > 0.0:
            score = (5.89 * (self.char_count / self.word_count)) - \
                (30 * (self.sentence_count / self.word_count)) - 15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        score = 0.0
        if self.word_count > 0.0:
            score = self.word_count / self.sentence_count + \
                float(100 * self.long_word_count) / self.word_count
        return score

    def RIX(self):
        longwords = 0.0
        score = 0.0
        if self.word_count > 0.0:
            score = self.long_word_count / self.sentence_count
        return score
