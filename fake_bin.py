def fake_bin(x):
    return "".join(list(map(lambda y: "0" if int(y) < 5 else "1", x)))

print(fake_bin("45385593107843568"))
print("01011110001100111")