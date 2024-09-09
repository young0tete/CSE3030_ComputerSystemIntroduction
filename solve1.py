#!/usr/bin/python3
import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from helper import Program


# TODO: Complete this function (do not touch anything else).
def solve():
    prog = Program("./problem1.bin")
    print(prog.read_line()) # Read the initial message of the program.
    prog.send_line("CSE3030@Sogang") # Send your input to the program.
    print(prog.read_line()) # Read the response from the program.


if __name__ == "__main__":
    solve()
