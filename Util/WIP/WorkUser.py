


import sys
from stackapi import StackAPI
#from stackexchange import Site, StackOverflow

#https://stackoverflow.com/users/792935/b0rg?tab=answers

user_id = 792935


so = StackAPI('stackoverflow')

me = so.user(user_id)
answers = me.answers.fetch()
print (answers.fetch_next())
