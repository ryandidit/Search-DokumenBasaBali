def create_NFA(keyword):
    # INIT QUINTUPLE
    state = []
    symbol = []
    delta = {}
    start_state = 'S0'
    final_state = {}
    # MANY OF STATE
    n = 1
    for i in keyword:
        n += len(i)
    # CREATE STATE
    for i in range(n):
        state.append('S'+str(i))
        delta['S'+str(i)] = {}
    # CREATE SYMBOL
    symbol = list(set(''.join(map(str, keyword))))
    # Create DELTA
    delta_NFA(keyword, delta, final_state)
    return state, symbol, delta, start_state, final_state


def delta_NFA(keyword, delta, final_state):
    count = 0
    for key in keyword:
        for i in range(len(key)):
            temp = str(count+1)
            if i == 0:
                if key[i] not in delta['S0']:
                    delta['S0'][key[0]] = []
                delta['S0'][key[i]].append('S'+temp)
            else:
                delta['S'+str(count)][key[i]] = 'S'+temp

            count += 1
            if i == len(key)-1:
                final_state['S'+str(count)] = str(key)


# ===================== MAIN ===================================
def generate(k):
    # INPUT KEYWORD
    keyword = [item for item in k.lower().split(' ')]
    # REMOVE EMPTY STRING IN KEYWORD
    keyword = list(filter(None, keyword))
    # ERROR IF INPUT IS EMPTY STRING
    if not keyword:
        return False
    else:
        # CREATE NFA
        state, symbol, delta, start_state, final_state = create_NFA(keyword)
        print("State :" + str(state))
        print("Symbol :" + str(symbol))
        print("Delta :"+str(delta))
        print("Start State :" + str(start_state))
        print("Final State :"+str(final_state))
    return state, symbol, delta, start_state, final_state
