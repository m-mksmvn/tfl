from itertools import count
import random
import re


class NFA:
    def __init__(self):
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()
        self._id_counter = count()

    def new_state(self):
        return next(self._id_counter)

    def add_transition(self, src, symbol, dst):
        self.transitions.setdefault(src, {}).setdefault(symbol, set()).add(dst)

    def add_epsilon_transition(self, src, dst):
        self.add_transition(src, None, dst)

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for next_state in self.transitions.get(state, {}).get(None, []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, states, symbol):
        result = set()
        for state in states:
            result |= self.transitions.get(state, {}).get(symbol, set())
        return result


def build_block(nfa):
    s_start = nfa.new_state()
    s_end = nfa.new_state()
    # aba
    a1,b1,a2 = nfa.new_state(), nfa.new_state(), nfa.new_state()
    nfa.add_transition(a1,'a',b1)
    nfa.add_transition(b1,'b',a2)
    nfa.add_transition(a2,'a',s_end)
    # bab
    b2,a3,b3 = nfa.new_state(), nfa.new_state(), nfa.new_state()
    nfa.add_transition(b2,'b',a3)
    nfa.add_transition(a3,'a',b3)
    nfa.add_transition(b3,'b',s_end)
    # aabb
    a4,a5,b4,b5 = nfa.new_state(),nfa.new_state(),nfa.new_state(),nfa.new_state()
    nfa.add_transition(a4,'a',a5)
    nfa.add_transition(a5,'a',b4)
    nfa.add_transition(b4,'b',b5)
    nfa.add_transition(b5,'b',s_end)
    # ε-переходы для *
    nfa.add_epsilon_transition(s_start,a1)
    nfa.add_epsilon_transition(s_start,b2)
    nfa.add_epsilon_transition(s_start,a4)
    nfa.add_epsilon_transition(s_start,s_end)
    nfa.add_epsilon_transition(s_end,s_start)
    return s_start,s_end


def build_full_nfa():
    nfa = NFA()
    nfa.start_state = nfa.new_state()
    left_start,left_end = build_block(nfa)
    nfa.add_epsilon_transition(nfa.start_state,left_start)
    # средняя часть (a|b)(a|b)bba
    m1,m2,m3,m4,m5 = [nfa.new_state() for _ in range(5)]
    nfa.add_transition(left_end,'a',m1)
    nfa.add_transition(left_end,'b',m1)
    nfa.add_transition(m1,'a',m2)
    nfa.add_transition(m1,'b',m2)
    nfa.add_transition(m2,'b',m3)
    nfa.add_transition(m3,'b',m4)
    nfa.add_transition(m4,'a',m5)
    # правая часть
    right_start,right_end = build_block(nfa)
    nfa.add_epsilon_transition(m5,right_start)
    nfa.accept_states.add(right_end)
    return nfa


def nfa_to_dfa(nfa):
    dfa_states = {}
    dfa_start = frozenset(nfa.epsilon_closure({nfa.start_state}))
    unmarked = [dfa_start]
    dfa_trans = {}
    dfa_accept = set()
    state_ids = {}
    next_id = 0
    while unmarked:
        curr = unmarked.pop()
        if curr in dfa_states: continue
        dfa_states[curr]=True
        state_ids[curr]=next_id
        next_id+=1
        dfa_trans[curr]={}
        symbols=set()
        for s in curr:
            symbols.update(k for k in nfa.transitions.get(s,{}) if k is not None)
        for sym in symbols:
            next_set = nfa.epsilon_closure(nfa.move(curr,sym))
            if next_set:
                dfa_trans[curr][sym] = frozenset(next_set)
                if frozenset(next_set) not in dfa_states:
                    unmarked.append(frozenset(next_set))
        if curr & nfa.accept_states:
            dfa_accept.add(curr)
    return dfa_start, dfa_trans, dfa_accept, state_ids




def dfa_accepts(start,trans,accept,word):
    curr=start
    for c in word:
        if c not in trans[curr]: return False
        curr = trans[curr][c]
    return curr in accept


if __name__=="__main__":
    nfa = build_full_nfa()
    dfa_start,dfa_trans,dfa_accept,state_ids = nfa_to_dfa(nfa)


regex = re.compile(r'^(?:aba|bab|aabb)*(?:a|b)(?:a|b)bba(?:aba|bab|aabb)*$')


def nfa_accepts(nfa, word):
    current = nfa.epsilon_closure({nfa.start_state})
    for c in word:
        current = nfa.epsilon_closure(nfa.move(current, c))
        if not current:
            return False
    return len(current & nfa.accept_states) > 0


def pka_accepts(start, trans, accept, word):
    return dfa_accepts(start, trans, accept, word)


def random_word(max_len=20):
    L = random.randint(0, max_len)
    return ''.join(random.choice('ab') for _ in range(L))


def fuzz_test(iterations=5000):
    for i in range(iterations):
        w = random_word()

        r = bool(regex.fullmatch(w))
        n = nfa_accepts(nfa, w)
        d = dfa_accepts(dfa_start, dfa_trans, dfa_accept, w)
        p = pka_accepts(dfa_start, dfa_trans, dfa_accept, w)

        if not (r == n == d == p):
            print("Слово:", w)
            print("Regex:", r)
            print("NFA:  ", n)
            print("DFA:  ", d)
            print("PDA:  ", p)
            return

    print(f"несоответствий нет")


fuzz_test(5000)

