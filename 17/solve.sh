#! /bin/sh

BASE='http://whale.hacking-lab.com:8881'

args=(
	-v
	-b cook
	-c cook
)

if [ "${1}" = 'login' ]
then
	curl "${args[@]}" "${BASE}/login.php"
	args+=(
		-X POST
		--data "username=test&pwd=test"
	)
	curl "${args[@]}" "${BASE}/login.php"
else
	curl "${args[@]}" "${BASE}/${1}"
fi
