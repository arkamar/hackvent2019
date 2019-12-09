#include <endian.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ff.h"

void
char2ff(const unsigned char c) {
	struct ff_color color;

	memset(&color, 0, sizeof color);
	color.a = 0xffff;

	switch (c) {
	case ' ':
	case 'w':
	case '0':
		color.r = 0xffff;
		color.g = 0xffff;
		color.b = 0xffff;
		break;
	case '#':
	case 'B':
	case '1':
		break;
	default:
		color.a = 0;
		fprintf(stderr, "Shit, unknown color: %02x <%c>\n", c, c);
		break;
	}

	fwrite(&color, 1, sizeof color, stdout);
}

int
main(int argc, char * argv[]) {
	struct ff_hdr hdr = { "farbfeld" };
	unsigned int width, size;
	unsigned char c;
	int i;

	if (argc < 2) {
		fprintf(stderr, "not enough arguments\n");
		exit(1);
	}

	width = atoi(argv[1]);

	hdr.width = htobe32(width);
	hdr.height = htobe32(width);
	size = width * width;

	fwrite(&hdr, 1, sizeof hdr, stdout);

	for (i = 0; fread(&c, 1, 1, stdin) == sizeof c; i++) {
		if (c != '\n')
			char2ff(c);
	}

	return 0;
}
