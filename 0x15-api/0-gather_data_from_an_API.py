#!/usr/bin/env python3
"""This script uses READ API for a given employee id,
and returns information about the employees TODO
list progress. The script takes one argument, which is
the employee id. The script then makes two requests to
the JSONPlaceholder API: one to get the user information
for the given id, and one to get the todos for the given
id. The script then prints out the employees name, the
number of todos they have completed, and a list of their
completed todos. """
import json
import requests
from sys import argv
def get_user_info(user_id):
	"""Gets user information from the JSONPlaceholder API."""
	url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
	response = requests.request("GET", url)
	return json.loads(response.content.decode("utf-8"))
def get_todos(user_id):
	"""Gets todos from the JSONPlaceholder API."""
	url = "https://jsonplaceholder.typicode.com/todos/"
	params = {"userId": user_id}
	response = requests.request("GET", url, params=params)
	return json.loads(response.content.decode("utf-8"))
def main():
	"""Main function."""
	# Get the user id from the command line arguments. 
	user_id = int(argv[1])
 # Get the user information for the given id. 
 user_info = get_user_info(user_id)
 # Get the todos for the given id. 
 todos = get_todos(user_id)
 # Print out the employees name. 
 print("Employee: {}". format(user_info["name"]))
 # Print out the numbers of todos completed. 
 completed_todos = len([todo for todo in todos if todo["completed"]]) 
 total_todos = len(todos) 
 print("Completed todos: {}/{}". format(completed_todos, total_todos)) 
 # Print out a list of the completed todos. 
 for todo in todos: 
 if todo["completed"]: 
 print("\
