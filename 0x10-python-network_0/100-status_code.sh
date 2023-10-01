#!/bin/bash
# Only status code
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
