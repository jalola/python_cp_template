#!/usr/bin/env python
import sys
input = lambda: sys.stdin.readline()

def read_ints():
    return [int(x) for x in input().split(" ")]

def read_int():
    return int(input())

def prepare_out(case_x, output):
    return "Case #{}: {}".format(case_x + 1, output)

def prepare_all_out(cases):
    return "\n".join(cases)