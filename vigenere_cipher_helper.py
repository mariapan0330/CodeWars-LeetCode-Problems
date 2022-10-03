"""
4 kyu

The shift is derived by applying a Caesar shift to a character with the 
corresponding index of the key in the alphabet.

Visual representation:

"my secret code i want to secure"  // message
"passwordpasswordpasswordpasswor"  // key

Write a class that, when given a key and an alphabet, can be used to encode 
and decode from the cipher.

EXAMPLE: 
alphabet = 'abcdefghijklmnopqrstuvwxyz';
key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key

c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'

"""

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key_dict = {}
        self.key = key
        self.alphabet = alphabet
        for i,c in enumerate(self.key):
            self.key_dict[i] = self.alphabet.index(c)


    def encode(self, text):
        res = ''
        # for each character in the text, the encoded character is:
        #     the position of that character + the position of the character at that index in the key.
        for i,c in enumerate(text):
            if c in set(self.alphabet):
                pos = self.alphabet.index(c) + self.key_dict[i % len(self.key_dict)]
                res += self.alphabet[pos % len(self.alphabet)]
            else:
                res += c
        return res

    def decode(self, text):
        res = ''
        # for each character in the text, the decoded character is:
            # the position of that character - the position of the character at the same index in the key
        for i, c in enumerate(text):
            res += self.alphabet[self.alphabet.index(c) - self.key_dict[i % len(self.key_dict)]] if c in set(self.alphabet) else c
        return res


abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'
c = VigenereCipher(key, abc)
# print(c.encode('codewars'))
# print(c.decode('rovwsoiv'))
# print(c.encode('cOdEwArS'))
# print(c.decode('rOvEsAiS'))
# print(c.decode('laxxhsj'))

print(c.encode("it's a shift cipher!"))
# "xt'k o vwixl qzswej!"
print(c.decode("xt'k o vwixl qzswej!"))