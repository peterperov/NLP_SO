import json 
import os
from stackapi import StackAPI

user_id = 792935
SITE = StackAPI('stackoverflow')
DATA_PATH = 'W:\\GITHUB\\NLP_SO\\Data\\'



def main():

    u = SITE.fetch('users/{}/comments'.format(user_id))
    dumpJson('comments000', u)

    # de facto URL limit ~2000 chars. so let's get comments in batches by 100
    i = 1
    ids = []

    comments = u.get('items')

    for item in comments: 
        i = i+1 
        ids.append( item.get('comment_id') )
        print (item.get('comment_id'))

        if i%100 == 0: 
            #got 100 item
            print("**************************************")
            print("hit 100")
            print("**************************************")
            GetComments('comments', 'comment_id', ids)
            i = 0
            ids = []
    else:
        # when the loop is finished
        if i > 0: 
            GetComments('comments','comment_id', ids)

    # answers
    a = SITE.fetch('users/{}/answers'.format(user_id))
    dumpJson('answers000', a)
    i = 1
    ids = []
    for item in a.get('items'):
        i=i+1
        ids.append(item.get('answer_id'))
        print( 'answer {}'.format(item.get('answer_id')))
        if i%100 == 0: 
            GetComments('answers', 'answer_id', ids)
            i = 0
            ids = []
    else: 
        if i > 0:
            GetComments('answers','answer_id', ids) 


def GetComments(vector, idName, ids):

    comments = SITE.fetch(vector, ids=ids, filter='withbody')

    for item in comments.get('items'):
        comment_id = item.get(idName)
        # build filename 
        filename = os.path.join(DATA_PATH, '{}'.format(user_id), '{}{}.json'.format(vector, comment_id))

        if not os.path.exists(filename):
            #save file here
            with open(filename, 'w') as f:
                f.write(json.dumps(item))


def dumpJson(file, data):
    filename = os.path.join(DATA_PATH, '{}.json'.format(file))
    with open(filename, 'w') as f:
        f.write(json.dumps(data))



# this will fire the main method
if __name__ == '__main__':
    main()




