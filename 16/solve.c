#include <stdio.h>
#include <stdint.h>

int
main() {
	uint32_t a;
	// 00401bb6 plus
	a = 0x1762a070 + 0x21ceb5d8;
	fwrite(&a, 1, sizeof a, stdout);
	// 004015c4 minus
	a = 0xaae5b913 - 0x38b57698;
	fwrite(&a, 1, sizeof a, stdout);
	// 00401be4 division
	a = 0xbec8cad6 / 2;
	fwrite(&a, 1, sizeof a, stdout);
	// 00401bd4 mult
	a = 2 * 0x33b0b623;
	fwrite(&a, 1, sizeof a, stdout);

	a = 0x53bd761a + 0x18a3cd45;
	fwrite(&a, 1, sizeof a, stdout);

	a = 0xa8359657 - 0x46c920f4;
	fwrite(&a, 1, sizeof a, stdout);

	a = 0x1f5c8c1d * 4;
	fwrite(&a, 1, sizeof a, stdout);

	return 0;
}
