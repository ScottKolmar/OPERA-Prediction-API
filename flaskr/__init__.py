from flask import Flask, json, request, send_file, jsonify, abort
import os
import csv

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def welcome():
        return jsonify({
            'success': True,
            'message': 'Welcome to the OPERA Prediction Microservice.'
        })
    
    @app.route('/<prediction_tag>/', methods = ['GET', 'POST'])
    def predict(prediction_tag):
        """
        Predicts the provided OPERA endpoint on a given smiles string.
        """
        # Filter for POST requests
        if request.method == 'POST':
            pass

        else:

            # Check prediction tag
            prediction_tag_list = [
                'BCF',
                'logBCF',
                'BP',
                'logP',
                'MP',
                'VP',
                'logVP',
                'WS',
                'AOH',
                'BioDeg',
                'RB',
                'ReadyBiodeg',
                'HL',
                'logHL',
                'KM',
                'logKM',
                'KOA',
                'Koc',
                'logKoc',
                'RT',
                'pKa',
                'logD',
                'CERAPP',
                'ER',
                'CoMPARA',
                'AR',
                'CATMoS',
                'AcuteTox',
                'Fu',
                'FuB',
                'Cl',
                'Clint'
                ]

            if prediction not in prediction_tag_list:
                abort(422)

            # Extract SMILES string
            smiles = request.args.get('smiles')

            # Find the current directory, path, and hardcode path to OPERA directory
            projdir = r'/app'
            projpath = os.path.normpath(projdir)

            # Define input and output file paths
            inputfilepath = os.path.normpath(os.path.join(projpath, 'input.smi'))
            outputfilepath = os.path.normpath(os.path.join(projpath, 'output.csv'))

            # Write SMILES as input.smi
            with open(inputfilepath, 'w') as f:
                f.write(smiles)
                f.close()

            try:
                # Run opera command
                opera_shell = '../usr/local/bin/OPERA/application/run_OPERA.sh'
                matlab_runtime = '..//usr/local/MATLAB/MATLAB_Runtime/v99'
                command = f'./{opera_shell} {matlab_runtime} -s {inputfilepath} -o {outputfilepath} -{prediction_tag}'
                os.system(command)
            
            except:
                abort(422)

            # Read prediction from output
            with open(outputfilepath, 'r') as f:
                reader = csv.reader(f)
                rows = []
                for row in reader:
                    rows.append(row)
            prediction = rows[1][1]
               
        return jsonify({
            "success": True,
            "prediction": prediction
        })
    
    # Error Handlers
    @app.errorhandler(404)
    def unprocessable_request(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        })

    @app.errorhandler(422)
    def unprocessable_request(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Request"
        })
    
    return app
