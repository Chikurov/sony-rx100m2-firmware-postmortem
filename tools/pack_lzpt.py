import struct, sys

def literal_stream(data):
    # LZ77 literal stream: 0x0F, pad byte, u16 len, bytes
    return bytes([0x0F, 0x00]) + struct.pack('<H', len(data)) + data

def pack_lzpt(img, block_log=16):
    bs = 1 << block_log
    n = (len(img) + bs - 1)//bs
    blocks = []
    for i in range(n):
        chunk = img[i*bs:(i+1)*bs]
        parts = []
        off = 0
        while off < len(chunk):
            take = min(65535, len(chunk)-off)
            parts.append(literal_stream(chunk[off:off+take]))
            off += take
        blocks.append(b''.join(parts))
    toc_size = 8*n
    data_start = 0x18 + toc_size
    toc = b''
    off = data_start
    for b in blocks:
        toc += struct.pack('<II', off, len(b))
        off += len(b)
    hdr = b'TPZL' + struct.pack('<III', block_log, 0x18, toc_size)
    return hdr + b'\x00'*8 + toc + b''.join(blocks)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    img = open(src,'rb').read()
    out = pack_lzpt(img)
    open(dst,'wb').write(out)
    print("packed", src, len(img), "->", dst, len(out))
