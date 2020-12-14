import csv


def pure_condition(num_t):
    """
    generates trials for pure condition
    """


def mixed_condition(num_t):
    """
    generates trials for mixed condition
    """


pos_dr = csv.DictReader(open('pos_pool.csv', 'r'))
pos_d = [l for l in pos_dr]
#  print(pos_d)

neg_dr = csv.DictReader(open('neg_pool.csv', 'r'))
neg_d = [l for l in neg_dr]
#  print(pos_d)

neu_dr = csv.DictReader(open('neu_pool.csv', 'r'))
neu_d = [l for l in neu_dr]
#  print(pos_d)

num_trials = int(input("Nubmer of trials: "))
pure_or_mixed = input("p for pure, m for mixed: ")

if pure_or_mixed == 'p':
    pure_condition(num_trials)

if pure_or_mixed == 'm':
    mixed_condition(num_trials)
