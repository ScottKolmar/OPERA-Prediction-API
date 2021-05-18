# Import Docker image
FROM ubuntu:18.04

# Put source code in docker container
WORKDIR /app
COPY . /app

# Update apt
RUN apt-get update

# Install unzip
RUN apt install unzip

# Install python
RUN echo "Y" | apt install python3.8

# Install distutils
RUN echo "y" | apt install python3.8-distutils

# Install Curl
RUN echo "Y" | apt install curl

# Install libxmu6
RUN echo "Y" | apt install libxmu6

# Download OPERA
RUN curl -L -O https://github.com/kmansouri/OPERA/releases/download/v2.6-beta2/OPERA2.6_CL.tar.gz

# Decompress OPERA
RUN tar -xzvf OPERA2.6_CL.tar.gz

# Install OPERA
RUN ./OPERA2_CL/OPERA2.6_CL.install -mode silent -agreeToLicense yes

# Install pip
RUN echo "Y" | apt install python3-pip

# Install dependencies
RUN /usr/bin/pip3 install -r ./requirements.txt

# Expose port
EXPOSE 5000

# Run source code
CMD ["../usr/bin/python3", "./app.py"]
