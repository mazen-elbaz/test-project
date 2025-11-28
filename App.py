from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# The route() decorator binds a URL to a function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Main driver function to run the application
if __name__ == '__main__':
    # Run the app on the local development server
    app.run()
