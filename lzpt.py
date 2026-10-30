import io, struct, sys

def inflate_lz77(f):
    t = f.read(1)
    if not t: return b''
    t = t[0]
    if t == 0x0f:
        f.read(1)
        l = struct.unpack('<H', f.read(2))[0]
        return f.read(l)
    if t != 0xf0:
        raise ValueError('bad type %02x' % t)
    out = bytearray()
    lengths = list(range(3, 17)) + [32, 64]
    while True:
        fb = f.read(1)
        if not fb: return bytes(out)
        flags = fb[0]
        if flags == 0:
            out += f.read(8)
        else:
            for i in range(8):
                if (flags >> i) & 1:
                    d = f.read(2)
                    if len(d) < 2: return bytes(out)
                    l = lengths[d[0] >> 4]
                    bd = ((d[0] & 0xf) << 8) | d[1]
                    if bd == 0:
                        return bytes(out)
                    seg = out[-bd:]
                    rep = seg * (l // len(seg) + 1)
                    out += rep[:l]
                else:
                    b = f.read(1)
                    if not b: return bytes(out)
                    out += b

def read_lzpt(path, out_path):
    d = open(path, 'rb').read()
    magic, block_log, toc_off, toc_size = struct.unpack_from('<4sIII', d, 0)
    assert magic == b'TPZL', magic
    n = toc_size // 8
    entries = [struct.unpack_from('<II', d, toc_off + i*8) for i in range(n)]
    out = bytearray()
    for off, size in entries:
        f = io.BytesIO(d[off:off+size])
        read = 0
        while read < (1 << block_log):
            chunk = inflate_lz77(f)
            if not chunk: break
            out += chunk
            read += len(chunk)
            if f.tell() >= size: break
    open(out_path, 'wb').write(out)
    print(path, "->", out_path, "blocks", n, "out", len(out), hex(len(out)), "head", out[:16].hex(' '))

if __name__ == '__main__':
    read_lzpt(sys.argv[1], sys.argv[2])
