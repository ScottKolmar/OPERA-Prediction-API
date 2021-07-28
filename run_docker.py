import os
import subprocess
import sys
import csv
import argparse

# Parse through optional arguments
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-h", "--hostname", help="Host URL", required=False, default = '0.0.0.0')
parser.add_argument("-p", "--port", help="Port Number", required=False, default = 5000)
args = parser.parse_args()

# Build image
docker_build = 'docker build -t pf_opera_predictions .'
os.system(docker_build)

# Get image name
image_output = subprocess.check_output(['docker', 'image', 'ls'])
image = str(image_output.split()[8]).split("'")[1]
print(image)

# Run the docker container from docker image
docker_run = f'docker run -e FLASK_APP=flaskr -p {args.port}:5000 -d -it {image}'
os.system(docker_run)

# Get container name
container_output = subprocess.check_output(['docker', 'container', 'ls'])
container = str(container_output.split()[8]).split("'")[1]

# Start Flask
docker_exec = f'docker exec {container} flask run {args.hostname} {args.port}'
os.system(docker_exec)
