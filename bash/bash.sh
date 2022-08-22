#!/bin/bash  
o=/bash/whoami.sh
p="$(pwd 2>&1)"
s=$p$o
if $s | grep -q 'root'; 
then
  echo "-----------------------"
else 
  echo "You Are Not ROOT!!"
fi



