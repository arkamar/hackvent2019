struct ff_hdr {
	char magic[8];
	uint32_t width;
	uint32_t height;
};

struct ff_color {
	uint16_t r, g, b, a;
};

struct ff_pixel {
	uint16_t r, g, b, a;
};
