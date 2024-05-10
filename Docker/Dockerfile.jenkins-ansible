# Use the official Jenkins image as base
FROM jenkins/jenkins:latest

# Switch to root user to install Ansible and dependencies
USER root

# Install dependencies for Ansible
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    software-properties-common \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment for Ansible
RUN python3 -m venv /opt/ansible

# Activate the virtual environment and install Ansible
RUN /opt/ansible/bin/pip install ansible

# Switch back to the Jenkins user
USER jenkins
