#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/6/2018 3:02 PM
# @Author  : FaccordX
# @File    : treebranchleaf.py
import sys

dict_3tree = {
    'China': {
        'Liaoning': ['Shenyang', 'Dalian', 'Anshan', 'Fushun'],
        'Shandong': ['Jinan', 'Qingdao', 'Weihai', 'Rizhao'],
        'Heilongjiang': ['Haerbin', 'Qiqihaer', 'Mudanjiang', 'Nenjiang']
    },
    'Singapore': {
        'Bugis': ['Bugis Plus', 'Junction', 'Bugis Mall'],
        'Payalebar': ['One KM', 'City Plaza', 'Payalebar Square'],
        'Jurong East': ['Jcube', 'IMM', 'East Mall']
    }
}
try:
    while 1:
        country = input("Please type your order: ")
        if country in dict_3tree.keys():
            countryBefo = country
            for prov in dict_3tree[country]:
                print(prov)
            province = input("Please type your order: ")
            if province in dict_3tree[country].keys():
                for cites in dict_3tree[country][province]:
                    print(cites)
                provinceBefo = province
            elif province == 'b':
                if countryBefo:
                    print(countryBefo)
                    continue
            elif province == 'q':
                sys.exit(0)
        elif country == 'b':
            if provinceBefo:
                print(provinceBefo)
                provinceBefo = None
            elif countryBefo:
                print(countryBefo)
                countryBefo = None
            else:
                print("this is the top level")
        elif country == 'q':
            sys.exit(0)
        else:
            print("Cannot find this country name.")
except:
    print("Quit")
