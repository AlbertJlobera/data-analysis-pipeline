import pandas as pd
import matplotlib
import sys
import os
import GrapApi
from argparse import ArgumentParser
from analysis import *
from path import *
from graphics import *
import matplotlib.pyplot as plt



def parse():
  parser = ArgumentParser(description="Check the sales or popularity of Nintendo video games")
  parser.add_argument("-d", dest='decade' ,help="Select the decade available: 1990, 1980,2000")
  parser.add_argument("-c",dest='country' ,help="write the country you ant to check: JP_Sales, EU_Sales, NA_Sales ")
  return parser.parse_args()


def main():
  args=parse()
  decade=args.decade
  country=args.country
  print(decade)
  print(country)
  df=acquire()
  s=Sales(df,decade,country)
  gra=visualize(df)
  
  print(gra)
  print(s)

if __name__ == '__main__':
  main()



