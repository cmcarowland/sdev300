if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1;
fi

if [ ! -d $1 ]; then
  mkdir -p "${1}/src";
  mkdir -p "${1}/tests";
else
  echo "Directory Already Exists";
  exit 2;
fi

cp ./project.sh $1/
touch $1/src/$1.py
touch $1/tests/$1_tests.py
