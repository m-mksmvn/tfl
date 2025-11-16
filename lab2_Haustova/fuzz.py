import random
from itertools import product

nfa = {
    "states": {
        "start", "s1", "ls_accept",
        "m1", "m2", "m3", "m4",
        "rs_start", "rs_accept",
        "r1_s", "r1_e", "r1_a1", "r1_b1", "r1_b2", "r1_a2",
        "r1_a3", "r1_a4", "r1_b3",
        "r2_s", "r2_e", "r2_a1", "r2_b1", "r2_b2", "r2_a2",
        "r2_a3", "r2_a4", "r2_b3"
    },

    "alphabet": {"a", "b"},

    "start": "start",
    "accepting": {"rs_accept"},

    "transitions": {
        # Start
        "start": {"ε": {"s1"}},

        # Left star
        "s1": {"ε": {"ls_accept", "r1_s"}},
        "r1_e": {"ε": {"r1_s", "ls_accept"}},

        # R1: aba
        "r1_s": {"a": {"r1_a1"}, "b": {"r1_b2"}, "a": {"r1_a3"}}, 

        "r1_s": {
            "a": {"r1_a1", "r1_a3"},
            "b": {"r1_b2"}
        },
        "r1_a1": {"b": {"r1_b1"}},
        "r1_b1": {"a": {"r1_e"}},

        # R1: bab
        "r1_b2": {"a": {"r1_a2"}},
        "r1_a2": {"b": {"r1_e"}},

        # R1: aabb
        "r1_a3": {"a": {"r1_a4"}},
        "r1_a4": {"b": {"r1_b3"}},
        "r1_b3": {"b": {"r1_e"}},

        # Middle: (a|b)(a|b) b b a
        "ls_accept": {"a": {"m1"}, "b": {"m1"}},
        "m1": {"a": {"m2"}, "b": {"m2"}},
        "m2": {"b": {"m3"}},
        "m3": {"b": {"m4"}},
        "m4": {"a": {"rs_start"}},

        # Right star
        "rs_start": {"ε": {"rs_accept", "r2_s"}},
        "r2_e": {"ε": {"r2_s", "rs_accept"}},

        # R2: aba
        "r2_s": {"a": {"r2_a1"}, "b": {"r2_b2"}, "a": {"r2_a3"}},

        "r2_s": {
            "a": {"r2_a1", "r2_a3"},
            "b": {"r2_b2"}
        },
        "r2_a1": {"b": {"r2_b1"}},
        "r2_b1": {"a": {"r2_e"}},

        # R2: bab
        "r2_b2": {"a": {"r2_a2"}},
        "r2_a2": {"b": {"r2_e"}},

        # R2: aabb
        "r2_a3": {"a": {"r2_a4"}},
        "r2_a4": {"b": {"r2_b3"}},
        "r2_b3": {"b": {"r2_e"}}
    }
}

dfa = {
    "states": {
        "0","1","2","3","4","5","6","7","8","9",
        "10","11","12","13","14","15","16","17","18","19",
        "20","21","22","23","24","25","26","27","28","29",
        "30","31","32","33","34","35","36","37","38","39",
        "40","41","42","43"
    },

    "alphabet": {"a", "b"},


    "start": "24",


    "accepting": {"0","1","2","3","4","5","6","7","8","9"},

    "transitions": {
        "0":  {"a": "13", "b": "43"},
        "1":  {"a": "12", "b": "43"},
        "2":  {"a": "17", "b": "11"},
        "3":  {"a": "18", "b": "23"},
        "4":  {"a": "29", "b": "25"},
        "5":  {"a": "20", "b": "10"},
        "6":  {"a": "12", "b": "25"},
        "7":  {"a": "12", "b": "21"},
        "8":  {"a": "12", "b": "4"},
        "9":  {"a": "0",  "b": "25"},
        "10": {"a": "42", "b": "41"},
        "11": {"a": "42", "b": "31"},
        "12": {"a": "30", "b": "41"},
        "13": {"a": "30", "b": "40"},
        "14": {"a": "39", "b": "38"},
        "15": {"a": "36", "b": "27"},
        "16": {"a": "36", "b": "22"},
        "17": {"a": "30", "b": "35"},
        "18": {"a": "30", "b": "33"},
        "19": {"a": "16", "b": "32"},
        "20": {"a": "15", "b": "32"},
        "21": {"a": "26", "b": "32"},
        "22": {"a": "24", "b": "31"},
        "23": {"a": "28", "b": "31"},
        "24": {"a": "16", "b": "14"},
        "25": {"a": "42"},
        "26": {"a": "36", "b": "5"},
        "27": {"a": "24", "b": "1"},
        "28": {"a": "16", "b": "2"},
        "29": {"a": "30", "b": "9"},
        "30": {"b": "42"},
        "31": {"b": "41"},
        "32": {"a": "7",  "b": "38"},
        "33": {"a": "6",  "b": "37"},
        "34": {"b": "37"},
        "35": {"a": "3",  "b": "32"},
        "36": {"b": "34"},
        "37": {"a": "3",  "b": "14"},
        "38": {"b": "31"},
        "39": {"b": "19"},
        "40": {"a": "6",  "b": "6"},
        "41": {"a": "6"},
        "42": {"b": "6"},
        "43": {"a": "8"}
    }
}


pka = {
    "states": [
        # Левая ветвь (полный NFA)
        "amp", "s1", "ls_accept",
        "m1", "m2", "m3", "m4",
        "rs_start", "rs_accept",

        # R1 (левая звезда)
        "r1_s", "r1_e",
        "r1_a1", "r1_b1",
        "r1_b2", "r1_a2",
        "r1_a3", "r1_a4", "r1_b3",

        # R2 (правая звезда)
        "r2_s", "r2_e",
        "r2_a1", "r2_b1",
        "r2_b2", "r2_a2",
        "r2_a3", "r2_a4", "r2_b3",

        # Правая ветвь (упрощённая NFA)
        "q0", "q1", "q2", "q3", "q4", "qA"
    ],

    "alphabet": ["a", "b", "ε"],

    "start": "amp",

    "accept_states": ["rs_accept", "qA"],

    "transitions": {

        "amp": {"ε": ["s1", "q0"]},

        # Left R*
        "s1": {"ε": ["ls_accept", "r1_s"]},
        "r1_e": {"ε": ["r1_s", "ls_accept"]},

        # R1 = {aba, bab, aabb}
        "r1_s": {"a": ["r1_a1", "r1_a3"], "b": ["r1_b2"]},
        "r1_a1": {"b": ["r1_b1"]},
        "r1_b1": {"a": ["r1_e"]},
        "r1_b2": {"a": ["r1_a2"]},
        "r1_a2": {"b": ["r1_e"]},
        "r1_a3": {"a": ["r1_a4"]},
        "r1_a4": {"b": ["r1_b3"]},
        "r1_b3": {"b": ["r1_e"]},

        # Middle chunk
        "ls_accept": {"a": ["m1"], "b": ["m1"]},
        "m1": {"a": ["m2"], "b": ["m2"]},
        "m2": {"b": ["m3"]},
        "m3": {"b": ["m4"]},
        "m4": {"a": ["rs_start"]},

        # Right R*
        "rs_start": {"ε": ["rs_accept", "r2_s"]},
        "r2_e": {"ε": ["r2_s", "rs_accept"]},

        # R2 = {aba, bab, aabb}
        "r2_s": {"a": ["r2_a1", "r2_a3"], "b": ["r2_b2"]},
        "r2_a1": {"b": ["r2_b1"]},
        "r2_b1": {"a": ["r2_e"]},
        "r2_b2": {"a": ["r2_a2"]},
        "r2_a2": {"b": ["r2_e"]},
        "r2_a3": {"a": ["r2_a4"]},
        "r2_a4": {"b": ["r2_b3"]},
        "r2_b3": {"b": ["r2_e"]},

        "q0": {"a": ["q0", "q1"], "b": ["q0", "q1"]},
        "q1": {"a": ["q2"], "b": ["q2"]},
        "q2": {"b": ["q3"]},
        "q3": {"b": ["q4"]},
        "q4": {"a": ["qA"]},
        "qA": {"a": ["qA"], "b": ["qA"]}
    }
}


def epsilon_closure(pka, states):
    stack = list(states)
    closure = set(states)

    while stack:
        s = stack.pop()
        for t in pka['transitions'].get(s, {}).get('ε', []):
            if t not in closure:
                closure.add(t)
                stack.append(t)
    return closure


def nfa_step(pka, states, ch):
    result = set()

    for s in states:
        for t in pka['transitions'].get(s, {}).get(ch, []):
            result.add(t)

    return epsilon_closure(pka, result)


def pka_accepts(pka, word):
    starts = pka['transitions'][pka['start']].get('ε', [])
    left  = epsilon_closure(pka, {starts[0]})
    right = epsilon_closure(pka, {starts[1]})

    for ch in word:
        left  = nfa_step(pka, left, ch)
        right = nfa_step(pka, right, ch)

        if not left or not right:
            return False

    accepting = set(pka['accept_states'])

    if len((left  & accepting) and (right & accepting)) != 0:
        return True
    return False


def nfa_accepts(nfa, word):
    current_states = epsilon_closure(nfa, {nfa['start']})
    for symbol in word:
        next_states = set()
        for state in current_states:
            next_states |= nfa['transitions'].get(state, {}).get(symbol, set())
        current_states = epsilon_closure(nfa, next_states)
    return bool(current_states & nfa['accepting'])


def dfa_accepts(dfa, word):
    state = dfa['start']
    for symbol in word:
        state = dfa['transitions'].get(state, {}).get(symbol)
        if state is None:
            return False
    return state in dfa['accepting']


def random_word(alphabet, max_len=20):
    length = random.randint(1, max_len)
    return ''.join(random.choice(list(alphabet)) for _ in range(length))


def fuzz_test(nfa, dfa, pka, iterations=10, max_len=20):
    for i in range(iterations):
        w = random_word(nfa['alphabet'], max_len)
        nfa_res = nfa_accepts(nfa, w)
        dfa_res = dfa_accepts(dfa, w)
        pka_res = pka_accepts(pka, w)

        consistent = (nfa_res == dfa_res == pka_res)

        status = "✅" if consistent else "❌"
        print(f"Word: {w:10} | NFA: {nfa_res} | DFA: {dfa_res} | PKA: {pka_res} | {status}")


fuzz_test(nfa, dfa, pka, iterations=1000)
