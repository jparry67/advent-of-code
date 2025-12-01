import argparse # get day/year input for past problems

from datetime import datetime # to get today's date
from pytz import timezone # to get today's date in correct timezone

from aocd import get_data

# import requests # for reading today's problem
# from bs4 import BeautifulSoup


def GetProblemDay():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", dest="year", help="Advent Year")
    parser.add_argument("-d", "--day", dest="day", help="Problem Day")
    args = parser.parse_args()

    todayYear = datetime.now().year
    todayDay = datetime.now(timezone('US/Eastern')).day

    year = int(args.year) if args.year is not None else todayYear
    day = int(args.day) if args.day is not None else todayDay

    return year,day

def GetProblemInput(year, day):
    data = get_data(day=day, year=year)
    f = open('{}/{}/input.txt'.format(year, day), 'w')
    f.write(data)
    f.close()


if __name__ == '__main__':
    year,day = GetProblemDay()
    GetProblemInput(year, day)
    # problemUrl = 'https://adventofcode.com/{}/day/{}'.format(year, day)
    
    # print(problemUrl)