if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1;
fi

if [ ! -d $1 ]; then
  mkdir -p "${1}/src";
else
  echo "Directory Already Exists";
  exit 2;
fi

scriptname=`echo $1 | tr '[:upper:]' '[:lower:]'`
cp ./project.sh $1/
touch $1/src/$scriptname.py
touch $1/src/${scriptname}_tests.py
