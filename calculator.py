#!/usr/bin/python3

import argparse
import numpy

# function to calc annuity of given net present values
# formula: v0 * q^T * (q-1) / q^T - 1
def calcAnnuity(v0, i, t):
    q = float(1 + (i/1000))
    g = v0 * ((q**t * (q-1)) / (q**t - 1))
    return numpy.round_(g, 4)


# function to calc end value
def calcVT(a, i, t):
    a = numpy.array(a)
    vt = 0
    q = float(1 + (i/100))
    counter = 0
    if len(a) <= 0:
        print("series of payment is empty")
        return 0
    if t <= 0: 
        print("period of time is to short")
        return 0
    # loop over all parts of payments and calc based on formula
    # formula: SUM t=0 til T of [at * 1^T-t]
    for value in a:
        vt += value * q**(t - counter)
        counter += 1
    return numpy.round_(vt, 4)

def calcV0(a, i, t):
    a = numpy.array(a)
    v0 = 0
    q = float(1 + (i/100))
    print(q)
    counter = 0
    if len(a) <= 0:
        print("series of payment is empty")
        return 0
    if t <= 0: 
        print("period of time is to short")
        return 0
    # loop over all parts of payments and calc based on formula
    # formula: SUM t=0 til T of [at * 1^-t]
    for value in a:
        v0 += value * q**(-t)
        t += 1
        counter += 1
    return numpy.round_(v0, 4)

def main(args):
    # check what value user is looking for
    if args.vt == True and args.v0 == False:
        resultVT = calcVT(args.a, args.i, args.t)
        print(f"Result for VT: {resultVT}")
    elif args.v0 == True and args.vt == False:
        resultV0 = calcV0(args.a, args.i, args.t)
        print(f"Result for VT: {resultV0}")
    elif args.g == True:
        resultG = calcAnnuity(calcV0(args.a, args.i, args.t), args.i, args.t)
        print(f"Result for equivalent annuity: {resultG}")




if __name__ == "__main__":
    # consts
    vt = False
    v0 = False
    g = False

    # inital parser
    parser = argparse.ArgumentParser(description="Fiwi key figures calucaltion")
    parser.add_argument("-vt", help="calculate end value", action="store_const", default=vt, const=not(vt))
    parser.add_argument("-v0", help="calculate net present value", action="store_const", default=v0, const=not(v0))
    parser.add_argument("-g", help="calculate equivanlent annuity", action="store_const", default=g, const=not(g))
    parser.add_argument("-a", help="set series of payment", nargs="+", type=float)
    parser.add_argument("-i", help="set interest rate", type=float)
    parser.add_argument("-t", help="set period", type=float)
    args = parser.parse_args()
    
    # call calculator with args
    main(args)