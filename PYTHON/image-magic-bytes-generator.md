Generate valid sample image files with correct magic bytes for file-upload and MIME-type validation testing.

<img width="368" height="286" alt="image" src="https://github.com/user-attachments/assets/3bb74620-f41a-444d-b6ce-fcfd764d8311" />


```python 
#!/usr/bin/env python3

import os
import struct
import zlib


def png_data():
    """Return a valid minimal 1x1 RGB PNG."""
    signature = b"\x89PNG\r\n\x1a\n"

    def chunk(kind, data):
        return (
            struct.pack(">I", len(data))
            + kind
            + data
            + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        )

    ihdr = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
    raw = b"\x00\x00\x00\x00"  # filter + black RGB pixel
    return signature + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def gif_data():
    """Return a valid minimal 1x1 GIF89a."""
    return (
        b"GIF89a"
        b"\x01\x00\x01\x00"      # width, height
        b"\x80\x00\x00"          # global color table flag + background + aspect
        b"\x00\x00\x00"          # black
        b"\xff\xff\xff"          # white
        b"\x2c\x00\x00\x00\x00"  # image descriptor + position
        b"\x01\x00\x01\x00"      # image width, height
        b"\x00"                  # no local color table
        b"\x02\x02\x44\x01\x00"  # LZW data
        b"\x3b"                  # trailer
    )


def jpeg_data():
    """Return a tiny valid JPEG image."""
    # 1x1 grayscale JPEG.
    return bytes.fromhex(
        "FFD8"
        "FFE000104A46494600010100000100010000"
        "FFDB004300"
        "080606070605080707070909080A0C140D0C0B0B0C190E0F0F0F0F0F"
        "0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F"
        "0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F"
        "FFC0000B080001000101011100"
        "FFDA0008010100003F00"
        "FFD9"
    )


def bmp_data():
    """Return a valid minimal 1x1 24-bit BMP."""
    pixel = b"\x00\x00\x00\x00"  # BGR + 1 byte row padding
    offset = 54
    size = offset + len(pixel)

    header = b"BM" + struct.pack("<IHHI", size, 0, 0, offset)
    dib = struct.pack(
        "<IiiHHIIiiII",
        40, 1, 1, 1, 24, 0, len(pixel), 0, 0, 0, 0
    )
    return header + dib + pixel


GENERATORS = {
    "1": ("png", png_data),
    "2": ("jpg", jpeg_data),
    "3": ("jpeg", jpeg_data),
    "4": ("gif", gif_data),
    "5": ("bmp", bmp_data),
}


def main():
    print("Image Generator")
    print("----------------")
    print("1. PNG")
    print("2. JPG")
    print("3. JPEG")
    print("4. GIF")
    print("5. BMP")

    choice = input("\nSelect format [1-5]: ").strip()

    if choice not in GENERATORS:
        raise SystemExit("Invalid selection.")

    ext, generator = GENERATORS[choice]

    filename = input(f"Filename [sample.{ext}]: ").strip()
    if not filename:
        filename = f"sample.{ext}"

    if os.path.basename(filename) != filename:
        raise SystemExit("Please provide a filename only, not a path.")

    if os.path.exists(filename):
        answer = input(f"{filename} exists. Overwrite? [y/N]: ").strip().lower()
        if answer != "y":
            raise SystemExit("Cancelled.")

    data = generator()

    with open(filename, "wb") as f:
        f.write(data)

    print(f"\nCreated: {filename}")
    print(f"Size:    {len(data)} bytes")
    print(f"Magic:   {data[:8].hex().upper()}")


if __name__ == "__main__":
    main()

```
