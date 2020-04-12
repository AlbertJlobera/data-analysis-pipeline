import argparse
import os
from main import ejecutar

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate Nintendo Sales report')
  parser.add_argument('-f', dest='filePath',
                    default= None,
                    help='.csv Sales Nintendo.')
  
  args = parser.parse_args()

  if isinstance(args.filePath, str):
    print(args.filePath)
    ejecutar(os.path.normpath(args.filePath))
  else:
    print('Indicate the csv file path')
