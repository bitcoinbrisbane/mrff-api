# for running as dev
from app import app
#from dotenv import load_dotenv
import os

#load_dotenv()

print('***')
print(os.environ.get('IP_ADDRESS'))

if __name__ == '__main__':
    app.run(os.environ.get('IP_ADDRESS'), port=os.environ.get('PORT'), debug=os.environ.get('DEBUG'))

