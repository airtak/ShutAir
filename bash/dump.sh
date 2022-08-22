#!/bin/bash
o=/bash/name.sh
p="$(pwd 2>&1)"
s=$p$o
source $s
a="mon"
b=${b}${a}
echo $b

airodump-ng $b