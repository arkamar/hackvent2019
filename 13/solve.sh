#! /bin/sh

BASE='http://whale.hacking-lab.com:8888/trieme'

args=(
	-v
	-c cook
)


if [ ${#} -gt 0 ]
then
	args+=(
		-b cook
		-H 'Content-Type: application/x-www-form-urlencoded'
		--data-urlencode 'j_idt14=j_idt14'
		--data-urlencode 'j_idt14:j_idt15=login'
		--data-urlencode "javax.faces.ViewState=${1}"
	)
fi

if [ ${#} -gt 1 ]
then
	args+=( --data-urlencode "j_idt14:name=${2}" )
fi

curl "${args[@]}" "${BASE}/faces/index.xhtml"
