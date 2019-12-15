# Hackvent 2019

- 01 [`HV19{just-4-PREview!}`](#day-1)
- 02 [`HV19{Cr4ck_Th3_B411!}`](#day-2)
- 03 [`HV19{h01d-th3-d00r-4204-ld4Y}`](#day-3)
- 04 [`HV19{R3memb3r, rem3mber - the 24th 0f December}`](#day-4)
- 05 [`HV19{D1fficult_to_g3t_a_SPT_R3ader}`](#day-5)
- 06 [`HV19{BACONCIPHERISSIMPLEBUTCOOL}`](#day-6)
- 07 [`HV19{1m_als0_w0rk1ng_0n_a_r3m0t3_c0ntr0l}`](#day-7)
- 08 [`HV19{5M113-420H4-KK3A1-19801}`](#day-8)
- 09 [`HV19{Cha0tic_yet-0rdered}`](#day-9)
- 10 [`HV19{Sh3ll_0bfuscat10n_1s_fut1l3}`](#day-10)
- 11 [`HV19{th3_cha1n_1s_0nly_as_str0ng_as_th3_w3ak3st_l1nk}`](#day-11)
- 14 [`HV19{s@@jSfx4gPcvtiwxPCagrtQ@,y^p-za-oPQ^a-z\x20\n^&&s[(.)(..)][\2\1]g;s%4(...)%"p$1t"%ee}`](#day-14)

- H1 [`HV19{1stHiddenFound}`](#hidden-1)
- H2 [`HV19{Dont_confuse_0_and_O}`](#hidden-2)
- H3 [`HV19{an0ther_DAILY_fl4g}`](#hidden-3)

## Day 1

> I got this little image, but it looks like the best part got censored on the
> way. Even the tiny preview icon looks clearer than this! Maybe they missed
> something that would let you restore the original content?

![ball](01/f182d5f0-1d10-4f0f-a0c1-7cba0981b6da.jpg)

There is an another image inside from 332th byte. ![thumb](01/thumb.jpg)

## Day 2

> Today we give away decorations for your Christmas tree. But be careful and do not break it.

The [Triangulation.stl](02/Triangulation.stl) is stereolithography format for 3D model.
There is a QR code in the middle of the ball.
![flag](02/flag.png)

## Day 3

I used https://tio.run/#hodor to interpret the [script](03/script.hd).

## Day 4

> Santa released a new password policy (more than 40 characters, upper, lower,
> digit, special).
>
> The elves can't remember such long passwords, so they found a way to continue to
> use their old (bad) password:
>
> merry christmas geeks

Run windows, install [AutoHotKey](https://www.autohotkey.com/), run the script [HV19-PPC.ahk](04/HV19-PPC.ahk), open notepad, write slowly `merry christmas geeks` and it will be replaced with the flag.

## Day 5

> To handle the huge load of parcels Santa introduced this year a parcel tracking
> system. He didn't like the black and white barcode, so he invented a more
> solemn barcode. Unfortunately the common barcode readers can't read it anymore,
> it only works with the pimped models santa owns. Can you read the barcode

![code](05/157de28f-2190-4c6d-a1dc-02ce9e385b5c.png)

I wrote small [program](05/dump.c) to dump hex colors from the first line of the image and processed it with following pipeline
```sh
< 157de28f-2190-4c6d-a1dc-02ce9e385b5c.png png2ff | ./dump | uniq | grep -vF 'ffff ffff' | cut -c11-12 | h2b
```
The flag is in the middle of other letters.
```
X8YIOF0ZP4S8HV19{D1fficult_to_g3t_a_SPT_R3ader}S1090OMZE0E3NFP6E
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

## Day 6

> *F*ra*n*cis Baco*n* *w*a*s* *a*n E*ng*lish ph*i*l*os*o*p*her a*n*d *s*tat*e*sm*a*n w*h*o se*rve*d *a*s At*t*or*n*ey Gen*e*ral and as *L*or*d* *Ch*an*ce*l*l*or of *En*g*l*an*d*. Hi*s* *w*orks ar*e* c*red*it*e*d w*ith* d*e*ve*lo*pi*ng* *t*h*e* sci*e*nt*i*fic me*t*hod and re*m*ai*ned* in*fl*u*en*ti*al* th*rou*gh *t*he s*cien*tific *r*ev*o*l*u*ti*o*n.
> *B*a*co*n h*as* *b*e*e*n ca*l*led *th*e *f*ath*e*r o*f* emp*iric*i*s*m. *Hi*s *wor*ks ar*g*ued for th*e* po*ssi*bi*li*t*y* of s*c*ie*n*tifi*c* *kno*wl*edg*e b*a*se*d* onl*y* u*p*on i*n*du*c*t*i*ve *r*ea*s*onin*g* *a*nd c*aref*u*l* o*bs*er*v*ation o*f* *e*v*e*nt*s* in *na*tur*e*. Mo*st* *i*mp*ort*an*t*l*y*, *he* a*rgue*d sc*i*en*c*e co*uld* *b*e *a*c*hi*eved by us*e* of a *s*ce*p*t*ical* a*nd* me*t*hod*i*ca*l* *a*pp*roa*ch wh*er*eby *s*cientist*s* ai*m* t*o* avo*i*d m*i*sl*ead*in*g* themsel*ve*s. *A*lth*oug*h *h*is *p*ra*c*tic*a*l i*d*e*a*s ab*out* *s*u*ch* *a* *m*et*h*od, *t*he B*a*con*i*an meth*o*d, d*i*d no*t* have *a* l*o*n*g*-*la*s*t*ing *i*nfluen*c*e, *th*e *g*e*ne*ral *i*dea *of* *t*he imp*o*rta*n*ce and pos*s*i*b*il*it*y o*f* a s*c*ept*i*cal methodology makes Bacon the father of the scientific method. This method was a new rhetorical and theoretical framework for science, the practical details of which are still central in debates about science and methodology.

This is [the Baconian cipher](http://www.wondersandmarvels.com/2012/12/shakespeares-secrets-a-hidden-cipher-in-literatures-greatest-works.html).
The original cypher text is in file [`text.html`](06/text.html). I wrote a small lex/yacc parser (see [`decode_lex.py`](06/decode_lex.py) and [`decode.py`](06/decode.py)) to transfer it to binary representation and [`solve.py`](06/solve.py) decrypts the cipher.

```
SANTALIKESHISBACONBUTALSOTHISBACONTHEPASSWORDISHVXBACONCIPHERISSIMPLEBUTCOOLXREPLACEXWITHBRACKETSANDUSEUPPERCASE
```
With extra spaces:
```
SANTA LIKES HIS BACON BUT ALSO THIS BACON THE PASSWORD IS HV X BACON CIPHER IS SIMPLE BUT COOL X REPLACE X WITH BRACKETS AND USE UPPERCASE
```

## Day 7

The [video](07/3DULK2N7DcpXFg8qGo9Z9qEQqvaEDpUCBB1v.mp4) with 8 blinking LEDs represents byte stream.
After conversion to png
```sh
ffmpeg -i 3DULK2N7DcpXFg8qGo9Z9qEQqvaEDpUCBB1v.mp4 out%04d.png
```
and a lot of manual work we got the flag.
The final solution is generated by [this](07/solve.py) simple python script.

## Day 8

> Introduction
>
> You hacked into the system of very-secure-shopping.com and you found a
> [SQL-Dump](08/dump.sql) with $$-creditcards numbers. As a good hacker you inform the company
> from which you got the dump. The managers tell you that they don't worry,
> because the data is encrypted.
>
> Goal
>
> Analyze the "Encryption"-method and try to decrypt the flag.
>
> Hints
>
> - CC-Numbers are real/valid ones.
> - Cyber-Managers often doesn't know the difference between encoding and encryption.

When I saw the [dump](08/dump.sql), I noticed the sequence for **Severus Snape**: `:)RPQRSTUVWXYZ[\]^`.
Credit cards use [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) for validation and I decided to search valid number for following pattern `*111111111111111` (Actually I searched lots of them, but this one was the correct one) and found `4111111111111111`.
I did following calculations
```python
ord('R') - 4 = 78
ord('P') - 1 = 79
ord('Q') - 1 = 80
ord('R') - 1 = 81
ord('S') - 1 = 82
```
that lead me to a following algorithm.
```python
s = 'RPQRSTUVWXYZ[\]^'
o = ''
for i in range(len(s)):
	o += str(ord(s[i]) - 78 - i)
```
It works for all credit card numbers, but it does not generate correct flag.
Well, here I have to thank you to @MartinDrab because he helped me to realize that I am searching index to the ascii table.
```python
def decode(s):
    s = s[2:]
    o = ''
    for i in range(len(s)):
        o += chr(ord(s[i]) - 30 - i)
    return o
```
Complete script is [here](08/solve.py).

## Day 9

> ### Santas Quick Response 3.0
>
> Visiting the following railway station has left lasting memories.
>
> ![img](09/railway.jpg)
>
> Santas brand new gifts distribution system is heavily inspired by it. Here is
> your personal gift, can you extract the destination path of it?
>
> ![img](09/qr.png)
>
> Hints
> - it starts with a single pixel
> - centering is hard

I found [this article](https://www.wikiwand.com/en/Rule_30) when searching the railway image which describes [Rule 30](https://en.wikipedia.org/wiki/Rule_30).
It is necessary to generate mask with Rule 30 (I wrote [this](09/solve.py) python script) and `xor` it with broken QR code.

![img](09/qr.png) `XOR` ![mask](09/mask.png) `=` ![out](09/out.png)

## Day 10

> ### Guess what
>
> The flag is right, of course

TL;DR: Run the `guess` binary and look to the `/proc/<PID>/cmdline`.

The binary constructs environment variable based on the PID of the process and re-execs itself via bash.
In the second exec it detects the variable, deciphers the shell scripts and execs it.

```sh
#!/bin/bash

read -p "Your input: " input

if [ $input = "HV19{Sh3ll_0bfuscat10n_1s_fut1l3}" ]
then
  echo "success"
else
  echo "nooooh. try harder!"
fi
```

## Day 11

> ### Frolicsome Santa Jokes API
>
> The elves created an API where you get random jokes about santa.
>
> Go and try it here: http://whale.hacking-lab.com:10101

API encodes information to the `token`.
This [script](11/solve.sh) access platinum part with the flag.

## Day 12

> ### back to basic
>
> Santa used his time machine to get a present from the past. get your rusty
> tools out of your cellar and solve this one!

## Day 13

> ### TrieMe
>
> Switzerland's national security is at risk. As you try to infiltrate a secret
> spy facility to save the nation you stumble upon an interesting looking login
> portal.
>
> Can you break it and retrieve the critical information?
>
> #### Resources
>
> - Facility: http://whale.hacking-lab.com:8888/trieme/

## Day 14

> ### Achtung das Flag
>
> Let's play another little game this year. Once again, I promise it is hardly obfuscated.
>
> ```perl
> use Tk;use MIME::Base64;chomp(($a,$a,$b,$c,$f,$u,$z,$y,$r,$r,$u)=<DATA>);sub M{$M=shift;##
> @m=keys %::;(grep{(unpack("%32W*",$_).length($_))eq$M}@m)[0]};$zvYPxUpXMSsw=0x1337C0DE;###
> /_help_me_/;$PMMtQJOcHm8eFQfdsdNAS20=sub{$zvYPxUpXMSsw=($zvYPxUpXMSsw*16807)&0xFFFFFFFF;};
> ($a1Ivn0ECw49I5I0oE0='07&3-"11*/(')=~y$!-=$`-~$;($Sk61A7pO='K&:P3&44')=~y$!-=$`-~$;m/Mm/g;
> ($sk6i47pO='K&:R&-&"4&')=~y$!-=$`-~$;;;;$d28Vt03MEbdY0=sub{pack('n',$fff[$S9cXJIGB0BWce++]
> ^($PMMtQJOcHm8eFQfdsdNAS20->()&0xDEAD));};'42';($vgOjwRk4wIo7_=MainWindow->new)->title($r)
> ;($vMnyQdAkfgIIik=$vgOjwRk4wIo7_->Canvas("-$a"=>640,"-$b"=>480,"-$u"=>$f))->pack;@p=(42,42
> );$cqI=$vMnyQdAkfgIIik->createLine(@p,@p,"-$y"=>$c,"-$a"=>3);;;$S9cXJIGB0BWce=0;$_2kY10=0;
> $_8NZQooI5K4b=0;$Sk6lA7p0=0;$MMM__;$_=M(120812).'/'.M(191323).M(133418).M(98813).M(121913)
> .M(134214).M(101213).'/'.M(97312).M(6328).M(2853).'+'.M(4386);s|_||gi;@fff=map{unpack('n',
> $::{M(122413)}->($_))}m:...:g;($T=sub{$vMnyQdAkfgIIik->delete($t);$t=$vMnyQdAkfgIIik->#FOO
> createText($PMMtQJOcHm8eFQfdsdNAS20->()%600+20,$PMMtQJOcHm8eFQfdsdNAS20->()%440+20,#Perl!!
> "-text"=>$d28Vt03MEbdY0->(),"-$y"=>$z);})->();$HACK;$i=$vMnyQdAkfgIIik->repeat(25,sub{$_=(
> $_8NZQooI5K4b+=0.1*$Sk6lA7p0);;$p[0]+=3.0*cos;$p[1]-=3*sin;;($p[0]>1&&$p[1]>1&&$p[0]<639&&
> $p[1]<479)||$i->cancel();00;$q=($vMnyQdAkfgIIik->find($a1Ivn0ECw49I5I0oE0,$p[0]-1,$p[1]-1,
> $p[0]+1,$p[1]+1)||[])->[0];$q==$t&&$T->();$vMnyQdAkfgIIik->insert($cqI,'end',\@p);($q==###
> $cqI||$S9cXJIGB0BWce>44)&&$i->cancel();});$KE=5;$vgOjwRk4wIo7_->bind("<$Sk61A7pO-n>"=>sub{
> $Sk6lA7p0=1;});$vgOjwRk4wIo7_->bind("<$Sk61A7pO-m>"=>sub{$Sk6lA7p0=-1;});$vgOjwRk4wIo7_#%"
> ->bind("<$sk6i47pO-n>"=>sub{$Sk6lA7p0=0 if$Sk6lA7p0>0;});$vgOjwRk4wIo7_->bind("<$sk6i47pO"
> ."-m>"=>sub{$Sk6lA7p0=0 if $Sk6lA7p0<0;});$::{M(7998)}->();$M_decrypt=sub{'HACKVENT2019'};
> __DATA__
> The cake is a lie!
> width
> height
> orange
> black
> green
> cyan
> fill
> Only perl can parse Perl!
> Achtung das Flag! --> Use N and M
> background
> M'); DROP TABLE flags; -- 
> Run me in Perl!
> __DATA__
> ```

The `@fff` variable holds the encrypted flag.
This [scripts](14/solve.py) decrypts it.

## Day 15

> ### Santa's Workshop
>
> The Elves are working very hard.
> Look at http://whale.hacking-lab.com:2080/ to see how busy they are.

```
[+] subscribed $SYS/#
[+] Topic: $SYS/broker/version - Message: b'mosquitto version 1.4.11 (We elves are super-smart and know about CVE-2017-7650 and the POC. So we made a genious fix you never will be able to pass. Hohoho)'        
```

- https://morphuslabs.com/hacking-the-iot-with-mqtt-8edaf0d07b9b?gi=636999db8f1e
- [CVE-2017-7650](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7650)
- [PoC](https://bugs.eclipse.org/bugs/show_bug.cgi?id=516765)

## Hidden 1

The first hidden flag is hidden in copy to clipboard of the [Day 6](#day-6).

```
Born: January 22	     	 	   	   	 	       	     	  	  
Died: April 9   	  	 	    	  	      	   		  	  
Mother: Lady Anne   		 	   	   	      	  	      	  
Father: Sir Nicholas	 	      		    	    	  	  	      	      
Secrets: unknown      	 	  	 	    	    	   	       	  
```
The spaces behind text are spaces, tabs and newlines hiding the flag in the message vie `stegsnow` command.
```sh
python decode.py > msg
stegsnow -C msg
```

## Hidden 2

The video name `3DULK2N7DcpXFg8qGo9Z9qEQqvaEDpUCBB1v.mp4` from [Day 7](#day-7) encodes hidden flag with [Base 58](https://en.wikipedia.org/wiki/Base58).

## Hidden 3

Following script dumps the flag
```sh
while sleep 3600
do
	nc whale.hacking-lab.com 17
done
```

## notes

- https://ranking.academy.hacking-lab.com/
- https://hv19.idocker.hacking-lab.com/
