# for running as dev
from app import app

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app.run(os.environ.get('IP_ADDRESS'), port=os.getenv('PORT'), debug=os.environ.get('DEBUG'))

