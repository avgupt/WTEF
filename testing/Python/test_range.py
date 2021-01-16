import pytest
from range import *


def test_init_zeroArg():
    r0 = Range()
    assert r0.start == 0 and r0.limit == 0

def test_init_oneArg():
    r1 = Range(3)
    assert r1.start == 0 and r1.limit == 3

def test_init_twoArg():
    r1 = Range(2, 5)
    assert r1.start == 2 and r1.limit == 5

    r2 = Range(5, 2)
    assert r2.start == 2 and r2.limit == 5

def test_init_threeArg():
    r3 = Range(2, 6, 4)
    assert r3.start == 0 and r3.limit == 0


def test_combine():
    r1 = Range(2, 6)
    r2 = Range(8)
    r3 = Range(11, 17)

    r4 = r1.combine(r2)
    assert r4.start == 0 and r4.limit == 8

    r5 = r1.combine(r3)
    assert r5.start == 2 and r5.limit == 17

    r6 = r2.combine(r3)
    assert r6.start == 0 and r6.limit == 17


def test_overlaps():
    r1 = Range(1, 4)
    r2 = Range(2, 7)
    r3 = Range(5, 6)

    assert r1.overlaps(r2) == True
    assert r2.overlaps(r3) == True
    assert r1.overlaps(r3) == False
