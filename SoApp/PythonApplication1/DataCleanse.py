import json 
import glob
import os

from bs4 import BeautifulSoup


user_id = 792935
DATA_PATH = 'W:\\GITHUB\\NLP_SO\\Data\\'
USER_PATH = os.path.join(DATA_PATH, '{}'.format(user_id))
CLEAN_DATA_PATH = os.path.join(DATA_PATH, '{}clean'.format(user_id))

def main(): 

    # loop through existing files 
    for f in glob.glob( os.path.join(USER_PATH, '*.json') ):
        print(f)

        with open(f) as json_file: 
            data = json.load(json_file)

        body = data.get('body')
        # print(body)

        # cleaning 
        soup = BeautifulSoup(body, 'html.parser')

        #strip <code> 
        [s.extract() for s in soup('code')]
        #strip <a>
        # TODO: might want to keep the text inside <a>, but later
        [s.extract() for s in soup('a')]

        # print(soup.get_text())
        filename = os.path.join(CLEAN_DATA_PATH, '{}.txt'.format(os.path.basename(f)))

        with open(filename, 'w', encoding='utf-8') as output:
            output.write(soup.get_text())



#def ClearBody(body):
    # need to remove <code> tags from message as it's not relevant


#def StripHTML(body):





# this will fire the main method
if __name__ == '__main__':
    main()

