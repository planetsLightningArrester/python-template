#!/bin/bash

virtualenv ./.venv

source .venv/bin/activate
python3 -m pip install \
    pylint==2.17.4 \
    black==23.7.0

# Install hooks
if [[ -d .git ]]; then
    cp -rf hooks/* ./git/hooks/
fi

# EOF