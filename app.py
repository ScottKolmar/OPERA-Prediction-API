from flask import Flask, request, send_file
import os
import csv

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the OPERA Prediction Microservice.'

@app.route('/logBCF/', methods = ['GET', 'POST'])
def predict_logBCF():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -logBCF -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/BP/', methods = ['GET', 'POST'])
def predict_BP():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -logBCF -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/logP/', methods = ['GET', 'POST'])
def predict_logP():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -logP -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/MP/', methods = ['GET', 'POST'])
def predict_MP():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -MP -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/VP/', methods = ['GET', 'POST'])
def predict_VP():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -VP -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/WS/', methods = ['GET', 'POST'])
def predict_WS():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -WS -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/AOH/', methods = ['GET', 'POST'])
def predict_AOH():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -AOH -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/BioDeg/', methods = ['GET', 'POST'])
def predict_BioDeg():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -BioDeg -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/RB/', methods = ['GET', 'POST'])
def predict_RB():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -RB -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/HL/', methods = ['GET', 'POST'])
def predict_HL():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -HL -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/KM/', methods = ['GET', 'POST'])
def predict_KM():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -KM -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/KOA/', methods = ['GET', 'POST'])
def predict_KOA():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -KOA -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/Koc/', methods = ['GET', 'POST'])
def predict_Koc():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -Koc -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/RT/', methods = ['GET', 'POST'])
def predict_RT():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -RT -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/pKa/', methods = ['GET', 'POST'])
def predict_pKa():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -pKa -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/logD/', methods = ['GET', 'POST'])
def predict_logD():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -logD -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/CERAPP/', methods = ['GET', 'POST'])
def predict_CERAPP():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -CERAPP -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/CoMPARA/', methods = ['GET', 'POST'])
def predict_CoMPARA():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -CoMPARA -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

@app.route('/CATMOs/', methods = ['GET', 'POST'])
def predict_CATMOs():
    """

    """

    # Filter for POST requests
    if request.method == 'POST':
        pass

    else:

        # Extract SMILES string
        smiles = request.args.get('smiles')

        # Find the current directory, path, and hardcode path to OPERA directory
        projdir = os.getcwd()
        projpath = os.path.normpath(projdir)
        relpath = os.path.normpath(r'C:\Program Files\OPERA\application')

        # Define input and output file paths
        filename = 'input.smi'
        inputfilepath = os.path.normpath(os.path.join(projdir, filename))
        outputfilepath = os.path.normpath(os.path.join(projdir, 'output.csv'))

        # Write SMILES as input.smi
        with open(inputfilepath, 'w') as f:
            f.write(smiles)
            f.close()

        # Run opera command Docker
        precommand = './../usr/local/bin/OPERA/application/run_OPERA.sh ../usr/local/MATLAB/MATLAB_Runtime/v94'
        command = ' -s {} -o {} -CATMOs -c'.format(inputfilepath, outputfilepath)
        os.system(precommand + command)

        # Read prediction from output
        with open(outputfilepath, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append(row)
        prediction = rows[1][1]

        # Write prediction to a TSV
        tsv_filename = 'prediction.tsv'
        tsv_filepath = os.path.normpath(os.path.join(projdir, tsv_filename))
        with open(tsv_filepath, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([smiles, prediction])

        # Remove output.csv, summary file, and input.smi
        os.remove(outputfilepath)
        os.remove(inputfilepath)

        # Transfer the TSV to a returnable object
        predictfile = send_file(tsv_filepath)

    return predictfile

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
