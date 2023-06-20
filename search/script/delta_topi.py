from .generate_nfa import generate


def check_word(text, i, key):
    c1 = c2 = False
    if i != (len(key)-1):
        if text[i-(len(key))].isalpha() or text[i-(len(key))].isdigit():
            c1 = True
    if i+1 < len(text):
        if text[i+1].isalpha() or text[i+1].isdigit():
            c2 = True

    if c1 or c2:
        return False
    else:
        return True


def delta_topi(text, state, symbol, delta, start_state, final_state):
    stop = False
    state_hasil = [start_state]
    for i, char in enumerate(text):
        # print(str(i)+' '+char)
        state_cek = state_hasil
        state_hasil = [start_state]
        for state in state_cek:
            if char in delta[state]:
                if state is start_state:
                    if any(item in delta[state][char] for item in final_state):
                        key = final_state[''.join(
                            [j for j in delta[state][char] if j in final_state])]
                        if check_word(text, i, key):
                            index = i
                            stop = True
                            break
                    state_hasil = list(
                        set(delta[state][char]) | set(state_hasil))
                else:
                    if delta[state][char] in final_state:
                        key = final_state[delta[state][char]]
                        if check_word(text, i, key):
                            index = i
                            stop = True
                            break
                    if delta[state][char] not in state_hasil:
                        state_hasil.append(delta[state][char])
        if stop:
            break

    # KONDISI APAKAH DIDALAM TEXT TERDAPAT SALAH SATU DARI KEYWORD
    if stop:
        return str(index)
    else:
        return False


# ================ MAIN ========================

# GENERATE NFA FROM KEYWORD INPUT
def main(k):
    return generate(k)
    # PROGRAM AKAN MERETURN
    # 1. key = salah satu word yang terkandung dalam text
    # 2. index = index char terakhir dari key yang ada pada text,
