#include <endian.h>
#include <stdint.h>
#include <stdio.h>

struct hdr {
	char mag[8];
	uint32_t width;
	uint32_t height;
};

struct pixel {
	uint16_t r;
	uint16_t g;
	uint16_t b;
	uint16_t a;
};

int
main() {
	struct hdr hdr;
	struct pixel p;

	fread(&hdr, sizeof hdr, 1, stdin);

	for (int i = 0; i < be32toh(hdr.width); i++) {
		fread(&p, sizeof p, 1, stdin);
		printf("%4x %4x %4x %4x\n", p.r, p.g, p.b, p.a);
	}
	return 0;
}
