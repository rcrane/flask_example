import os
import subprocess
from flask import Flask, request, redirect, render_template
import backend


app = Flask(__name__, template_folder='frontend')


@app.route('/', methods=['GET'])
def service_home():
    return render_template('index.html')


@app.route('/run_some_backend_stuff/')
def name_doesnt_matter():
    text = subprocess.check_output("pwd", universal_newlines=True, stderr=subprocess.PIPE)
    print("Current working_path: ", text, flush=True)
    return backend.run_bash_script()


@app.route('/', methods=['GET', 'POST'])
def upload_client_session():

    if request.method == 'POST':
        client_input_id = request.form['input_id']
        # check if the session_id is not provided
        if client_input_id == '':
            print('~~~~~ No input given! ~~~~~', flush=True)
            return redirect(request.url)

        else:
            # just to show that bash can be used as well:
            os.system(f"echo id='\"{client_input_id}\"'")

            # do some python magic here

            # feed data to the website
            return render_template("index.html", data=client_input_id)


@app.route('/hello_world/', methods=['GET'])
def print_message():

    print("Hello World triggerd!", flush=True)
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
