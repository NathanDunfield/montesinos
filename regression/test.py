import subprocess
import os
import random
import math

def run_py2(filename, args):
    return subprocess.check_output(['py27', 'two/' + filename, '-f'] + args).decode()

def run_py3(filename, args):
    return subprocess.check_output(['py38', 'three/' + filename, '-f'] + args).decode()

def check_two_bridge():
    script = 'two_bridge_bdry.py'
    for n in range(100):
        q = random.randrange(1000)
        p = random.randrange(q)
        a = math.gcd(p, q)
        p, q = p//a, q//a
        args = [repr(p), repr(q)]
        ans2 = run_py2(script, args)
        ans3 = run_py3(script, args)
        assert ans2 == ans3
        print(p, q, ans2 == ans3, len(ans2))

def rand_frac(n):
    q = random.randrange(2, n)
    p = random.randrange(q)
    a = math.gcd(p, q)
    p, q = p//a, q//a
    s = random.choice(['-', ''])
    return s + '%d/%d' % (p, q)


def check_montesinos():
    for n in range(1000):
        script = 'montesinos_bdry.py'
        t = random.randrange(3, 6)
        fracs = [rand_frac(40) for _ in range(t)]
        ans2 = run_py2(script, fracs)
        ans3 = run_py3(script, fracs)
        assert ans2 == ans3
        if ans2 != ans3:
            file = open('out2.txt', 'w')
            file.write(ans2)
            file.close()
            file = open('out3.txt', 'w')
            file.write(ans3)
            file.close()
        
        print(fracs, ans2 == ans3, len(ans2))
