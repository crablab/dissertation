from app import create_app
import os

app = create_app("settings")

# CSRF Key 
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == '__main__':

    app.run(debug=True)