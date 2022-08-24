class BestMemer:
    """class pronounce some memes"""

    def __init__(self, list_of_phrases):
        self.phrases = list_of_phrases
        self.index = 0
        self.phrases_len = len(list_of_phrases) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.phrases_len:
            raise StopIteration
        result = self.phrases[self.index]
        self.index += 1
        return result

    @property
    def phrases(self):
        return self._phrases

    @phrases.setter
    def phrases(self, list_of_phrases):
        if type(list_of_phrases) is list:
            self._phrases = list_of_phrases
            self.phrases_len = len(list_of_phrases) - 1
            self.index = 0

    def meme2(self):
        pass

    def meme3(self):
        pass

meme = BestMemer(['your', 'back', 'is', 'white'])
print(next(meme))
print(next(meme))
print(next(meme))
print(next(meme))
meme.phrases = [1, 2, 3, 4]
print(next(meme))
print(next(meme))
print(next(meme))
print(next(meme))
print(next(meme))

