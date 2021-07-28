import os
import subprocess
import sys
import csv

# Build image
docker_build = 'docker build -t pf_opera_predictions .'
os.system(docker_build)

# Get image name
image_output = subprocess.check_output(['docker', 'image', 'ls'])
image = str(image_output.split()[8]).split("'")[1]
print(image)

# Run the docker container from docker image
docker_run = f'docker run -e FLASK_APP=flaskr -p 5000:5000 -d -it {image}'
os.system(docker_run)

# Get container name
container_output = subprocess.check_output(['docker', 'container', 'ls'])
container = str(container_output.split()[8]).split("'")[1]

# Extract optional parameters
if len(sys.argv) == 1:
    host_url = '0.0.0.0'
    port_num = '5000'

elif len(sys.argv) == 2:
    host_url = sys.argv[1]
    port_num = '5000'

elif len(sys.argv) == 3:
    host_url = sys.argv[1]
    port_num = sys.argv[2]

# Start Flask
docker_exec = f'docker exec {container} flask run -h {host_url} -p {port_num}'
os.system(docker_exec)
