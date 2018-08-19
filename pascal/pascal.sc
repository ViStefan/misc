#!/bin/sh
exec scala "$0" "$@"
!#

def pascal(c: Int, r: Int): Int = {
    def nxt(l: List[Int], r: List[Int] = List()): List[Int] =
        if (l.length > 1)
            nxt(l.tail, (l(0) + l(1)) :: r)
        else
            r

    def one(cond : Boolean): List[Int] =
        if (cond) List() else List(1)
            
    def pas(x: Int, y: Int, l: List[Int], r: Int): Int =
        if (r <= y)
            pas(x, y, one(r > y - x) ++ nxt(l) ++ one(r > x), r + 1)
        else
            l(0)

    pas(c, r, List(1), 1)
}

println(pascal(args(0).toInt, args(1).toInt))
