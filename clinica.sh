#!/bin/sh
echo "Move to"
cd /home/fj/clinica
pwd
echo "Virtual environments"
. venv/bin/activate
echo "Clinica scripts"
py clinica.py
echo "Closed"