#!/usr/bin/env python3
'''
This program uses the READ API to retrieve information
about an employees TODOs. The program takes one argument, an
employee ID. Once the ID is provided, the program will
retrieve the information from the API and print it to the
console.'''

## Import necessary modules
import json
import requests

## Define function to retrieve employee information
def get_employee_information(employee_ID):
'''This function retrieves employee information from
the READ API using the provided employee_ID.'''

## Create the request URL
request_url = f'https://api.mycompany.net/v1/employees/{employee_ID}'

## Make the request
response = json.loads(requests.request('GET', request_url).content)
return response

## Define function to print employee information
def print_employee_information(employee):
'''This function prints employee information to
the console.'''
print('Employee ID:', employee['employeeID'])
print('Name:', employee['name'])
print('Department:', employee['department'])
print('Title:', employee['title'])

## Get employee information from user
employee_ID = input('Enter employee\'s ID: ')
employee = get_employee_information(employee_ID)

## Print employee information to console
print_employee_information(employee)
