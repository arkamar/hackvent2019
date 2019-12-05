# Hackvent 2019

01. [`HV19{just-4-PREview!}`](#day-1)
02. [`HV19{Cr4ck_Th3_B411!}`](#day-2)
03. [`HV19{h01d-th3-d00r-4204-ld4Y}`](#day-3)
04. [`HV19{R3memb3r, rem3mber - the 24th 0f December}`](#day-4)
05. [`HV19{D1fficult_to_g3t_a_SPT_R3ader}`](#day-5)

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

## notes

- https://ranking.academy.hacking-lab.com/
- https://hv19.idocker.hacking-lab.com/
