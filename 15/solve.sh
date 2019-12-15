#! /bin/sh

BASE='http://whale.hacking-lab.com:2080/'

args=(
	-v
)

curl "${args[@]}" "${BASE}"
