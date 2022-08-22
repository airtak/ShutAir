#!/bin/bash
read -p "..........ENTER Your Network Name >" o
echo $o
k=/bash/name.sh
p="$(pwd 2>&1)"
s=$p$k
echo "b=""${o}">$s 
echo 'echo $b'>>$s