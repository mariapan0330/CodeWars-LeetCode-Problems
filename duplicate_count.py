def duplicate_count(text):
    found_letts = set()
    found_dups = set()
    dup_count = 0
    for x in text.lower():
        if x in found_letts and x not in found_dups:
            dup_count += 1
            found_dups.add(x)
        else:
            found_letts.add(x)
    return dup_count
        

print(duplicate_count("abcde"))
print(duplicate_count("abcdaae"))
print(duplicate_count("abcdAe"))