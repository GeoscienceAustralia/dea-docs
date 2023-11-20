#!/bin/bash

python -m pip install -r ./requirements.txt

npm install -g sass

apt-get install -y pandoc

mkdir -p ./output

if [ "$PRODUCTION_MODE" == "Yes" ]
then
    sass --style=compressed ./docs/_static/styles/index.scss ./docs/_static/styles/styles.css
else
    sass --style=expanded ./docs/_static/styles/index.scss ./docs/_static/styles/styles.css
fi

if [ "$PRODUCTION_MODE" == "Yes" ]
then
    cp ./docs/_robots/robots-prod.txt ./docs/robots.txt
else
    cp ./docs/_robots/robots-dev.txt ./docs/robots.txt
fi

sphinx-build -b dirhtml -j auto ./docs ./output