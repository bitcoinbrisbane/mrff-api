from app import app
import os

if __name__ == '__main__':
    print('Starting')

    PORT = os.environ.get('PORT')
    app.run('127.0.0.1', port=PORT, debug=False)
