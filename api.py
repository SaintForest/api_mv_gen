from flask import Flask, request
from infer import main
app = Flask(__name__)
@app.route('/analyze', methods=['POST'])
def analyze_data():
    description = request.form.get('description')  # Get the 'overview' data from the request's form data

    # Perform analysis or processing on the data
    # For example, you could print the received data and return a response
    result = main(["--description", description])
    print("Received data:", description)

    return "Result: " + str(result)
    
if __name__ == '__main__':
    app.run(port=8000)






