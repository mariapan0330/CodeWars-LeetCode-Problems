def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    n_count = walk.count("n")
    s_count = walk.count("s")
    e_count = walk.count("e")
    w_count = walk.count("w")
    return True if n_count == s_count and e_count == w_count else False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))