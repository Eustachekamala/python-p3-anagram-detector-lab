class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
        
    def match(self, possible_anagrams):
        '''We craete an empty list before where we'll append the anagrams checked'''
        valid_anagrams = []
        
        for candidate in possible_anagrams:
            # Here we check if the candidate isn't the same with the original word
            if candidate != self.word:
                # Check if sorted characters of the candidate match sorted characters of the original word
                if ''.join(sorted(candidate)) == self.sorted_word:
                    valid_anagrams.append(candidate)
                    
        return valid_anagrams
    
anagram_checker = Anagram("listen")

possible_anagrams = ["enlist", "google", "inlets", "banana", "silent"]

matches = anagram_checker.match(possible_anagrams)

print(matches)

