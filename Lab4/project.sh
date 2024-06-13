if [ ${PWD##*/} = "sdev300" ]; then
    echo "Cannot run from outside a project"
    exit 1;
fi

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1;
fi
scriptname=`echo ${PWD##*/} | tr '[:upper:]' '[:lower:]'`
case $1 in
    run)
        echo "Running src/${scriptname}.py ..."
        python src/${scriptname}.py
        ;;
    lint)
        echo "Linting..."
        pylint src/${scriptname}.py
        ;;
    test)
        echo "Testing..."
        pytest src/${scriptname}_tests.py -vv
        ;;
    all)
        echo "All..."
        pylint src/${scriptname}.py
        pytest src/${scriptname}_tests.py -vv
        python src/${scriptname}.py
        ;;
*)
    echo "$1 is not supported"
esac