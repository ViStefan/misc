#!/bin/sh

test()
{
    f=$1
    x=$2
    y=$3
    assert=$4

    calc=`./"$f" $x $y`
    if [ "$calc" = "$assert" ]; then
        result='ok'
    else
        result='failed'
    fi

    echo "$x, $y => $calc - $result"
}

if [ -f "$1" ]; then
    test "$1" 0 0 1
    test "$1" 0 1 1
    test "$1" 1 1 1
    test "$1" 0 10 1
    test "$1" 10 10 1
    test "$1" 2 4 6
    test "$1" 6 13 1716
else
    echo "Usage: $0 file_to_test"
fi
