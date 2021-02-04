install:
		pip install --upgrade pip&&\
					pip install -r requirements.txt
					pip install awsebcli --upgrade

lint:
	pylint --disable=R,C application.py

create:
	eb init -p python-3.7 ebcd-app --region us-east-1
	eb create ebcd-env


deploy:
	echo "Deploying webapp"
	eb deploy ebcd-env

all: install lint