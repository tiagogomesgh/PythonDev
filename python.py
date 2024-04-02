# Tiago Gomes - Python Development Training
import math

def main ():

  p0 = int(input("Enter the starting population: "))
  percent = int(input("Enter the percentage increase: "))
  aug = int(input("Enter the augmented increase: "))
  p = int(input("Enter the desired population: "))

  nb_year(p0,percent,aug,p)




# Growth of Population
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

def nb_year(p0,percent,aug,p):
    percentage = percent * .01
    n = 0
    while p0 <= p:
      p0 = p0 + (p0 * percentage) + aug
      p0 = math.floor(p0)
      print(f'End of year population {p0}')
      n += 1

    print(f'It will need {n} entire years')






if __name__ == '__main__':
  main()
