# build_files.sh

echo "Building the project..."
python3.10 -m pip install -r requirements.txt

echo "Make migration..."
python3.10 manage.py makemigrations --no-input
python3.10 manage.py migrate --no-input

echo "Collect static..."
python3.10 manage.py collectstatic --no-input --clear
