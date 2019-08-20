#import StackAPI
import json 

#get comments

from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
comments = SITE.fetch('comments')

# comments is a dict object
print(comments)


dump = json.dumps(comments)

# dump comments to text file
with open('..\\output.json', 'w') as f:
	f.write(dump)

