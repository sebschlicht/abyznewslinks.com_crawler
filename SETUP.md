# Initial Development Environment Setup

Run the following commands in the project folder, to initially setup a local Python development environment for this project:

    sudo apt install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Then unpack the Ansible vault (templating sensible files) using [vauly](https://github.com/sebschlicht/vauly)

    vauly unpack

or template the sensitive files (see vauly.yml) by other means, e.g. manually.
