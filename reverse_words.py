# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    temp_word = ""
    text_list = []
    for i, x in enumerate(text):
        if x == " ":
            text_list.append(temp_word)
            temp_word = ""
            text_list.append(" ")
            continue
        temp_word += x
        if i == len(text)-1:
            text_list.append(temp_word)
            temp_word = ""

    res = []
    for w in text_list:
        w = w[::-1]
        res.append(w)
    return "".join(res)

print(reverse_words("This  is an example!"))
