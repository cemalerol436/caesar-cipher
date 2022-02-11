alp = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


alp2 = []
for i in range(len(alp)):
    alp2.append(alp[i].upper())

def cemal_pass(x : str, k: int):
    new_word = ""
    for i in range(len(x)):

        if x[i] not in alp:

            if x[i].isupper():

                temp_index = (alp2.index(x[i]) + k) % len(alp2)
                new_word += (alp2[temp_index])
            else:
                new_word += (x[i])
        else:
            temp_index = (alp.index(x[i]) + k) % len(alp)
            new_word += (alp[temp_index])
    print(new_word)


cemal_pass("Always-Look-on-the-Bright-Side-of-Life",5)

