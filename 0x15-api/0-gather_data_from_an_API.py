#!/usr/bin/env python3
'''
Using https:// jsonplaceholder . typicod e. com
returns info about employee T O D O progress
Implemented using recursion
'''
 import requests , sys
 from functools import reduce
 from operator import attrgetter
 API = " https:// jsonplaceholder . typicode. com"  # REST API url
 def get(url):  return requests . get(url) . json () # GET request
 def main():  # main function
     id = sys . argv[ :2 ]
     id = reduce(attrgetter(' id '), id ) # get employee id
     res1 = get(' {} / users / {} ' . format ( API , id ) ) # get user info
     res2 = get(' {} / todos ' . format ( API ) ) # get todos
     uname = res1[' name '] ; todos = res2
     td = [ todo for todo in todos if todo[' userId '] == id and todo[' completed '] ] # filter todos
     tn = [ todo[' title '] for todo in td ] ; print( ' Employee {} is 
             done with t a s k s( {}/{} ):' . format(uname , len(td) , len(todos )))
         for t in tn : print('\t {}' . form a t(t)) # print todos done
 if __ name__ = = '__ main__ ': main ( )
