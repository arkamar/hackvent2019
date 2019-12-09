#include <endian.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "ff.h"

int
main(int argc, char * argv[]) {
	struct ff_hdr hdr;
	struct ff_pixel p;
	int width;

	if (argc < 2) {
		fprintf(stderr, "usage %s WIDTH\n", argv[0]);
		exit(1);
	}

	width = atoi(argv[1]);

	fread(&hdr, sizeof hdr, 1, stdin);
	fprintf(stderr, "width: %u height: %u\n", be32toh(hdr.width), be32toh(hdr.height));

	for (int y = 0; y < be32toh(hdr.height); y++) {
		for (int x = 0; x < be32toh(hdr.width); x++) {
			fread(&p, sizeof p, 1, stdin);
			if (x % width == 0 && y % width == 0) {
				if (p.r) {
					fputc(' ', stdout);
				} else {
					fputc('#', stdout);
				}
			}
		}
		if (y % width == 0) {
			fputc('\n', stdout);
		}
	}
	return 0;
}
