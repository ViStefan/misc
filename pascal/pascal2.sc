#!/bin/sh
exec scala "$0" "$@"
!#

def pascal(c: Int, r: Int): Int = {
  def pas(x: Int, y: Int, l: List[Int], n: List[Int], r: Int): Int =
    if (n.length < l.length)
      pas(x, y, l, n ++ List(l(n.length) + n.reverse.head), r)
    else
      if (r < x)
        pas(x, y, n, List(1), r + 1)
      else
        n.reverse.head

  if (c > 0 && c != r)
    pas(c, r, (0 to r - c).map{_ => 1}.toList, List(1), 1)
  else
    1
}

println(pascal(args(0).toInt, args(1).toInt))
