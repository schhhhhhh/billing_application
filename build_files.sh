# build_files.sh

echo "Building the project..."
#python3.9 -m pip install -r requirements.txt

#echo "Make migration..."
#python3.9 manage.py makemigrations --no-input
#python3.9 manage.py migrate --no-input

#echo "Collect static..."
#python3.9 manage.py collectstatic --no-input --clear

pip install -r requirements.txt
python3.9 manage.py collectstatic
