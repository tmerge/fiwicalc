#!/usr/bin/python3

import argparse
import numpy


def main(args):
    print(args)
    if args.vt != None:
        print("calc vt")




if __name__ == "__main__":
    # consts
    vt = False
    v0 = False

    # inital parser
    parser = argparse.ArgumentParser(description="Fiwi key figures calucaltion")
    parser.add_argument("-vt", help="calculate end value", action="store_const", default=vt, const=not(vt))
    parser.add_argument("-v0", help="calcualte net present value", action="store_const", default=v0, const=not(v0))
    parser.add_argument("-a", help="set series of payment")
    parser.add_argument("-i", help="set interest rate")
    parser.add_argument("-t", help="set period")
    args = parser.parse_args()

    print("1")

    # call calculator with args
    main(args)