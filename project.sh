if [ ${PWD##*/} = "sdev300" ]; then
    echo "Cannot run from outside a project"
    exit 1;
fi

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit 1;
fi

case $1 in
    run)
        echo "Running src/${PWD##*/}.py ..."
        python src/${PWD##*/}.py
        ;;
    lint)
        echo "Linting..."
        pylint src/${PWD##*/}.py
        ;;
    test)
        echo "Testing..."
        pytest tests/${PWD##*/}_tests.py
        ;;
    all)
        echo "All..."
        pylint src/${PWD##*/}.py
        pytest tests/${PWD##*/}_tests.py
        python src/${PWD##*/}.py
        ;;
*)
    echo "$1 is not supported"
esac