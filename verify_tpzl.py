"""Verify a TPZL/LZPT container against constraints observed in Sony images.

Checks: header, TOC, block decompression, literal-chunk sizes, entry sizes.
Usage: python3 verify_tpzl.py image.tpzl [--ref reference.tpzl]
"""
import sys, struct, io

def inflate(f):
    t = f.read(1)
    if not t:
        return b''
    if t[0] == 0x0F:
        f.read(1)
        l = struct.unpack('<H', f.read(2))[0]
        return f.read(l)
    if t[0] != 0xF0:
        raise ValueError('bad stream type 0x%02x' % t[0])
    out = bytearray()
    lengths = list(range(3, 17)) + [32, 64]
    while True:
        fb = f.read(1)
        if not fb:
            return bytes(out)
        flags = fb[0]
        if flags == 0:
            out += f.read(8)
            continue
        for i in range(8):
            if (flags >> i) & 1:
                d = f.read(2)
                if len(d) < 2:
                    return bytes(out)
                l = lengths[d[0] >> 4]
                bd = ((d[0] & 0xF) << 8) | d[1]
                if bd == 0:
                    return bytes(out)
                seg = out[-bd:]
                out += (seg * (l // len(seg) + 1))[:l]
            else:
                b = f.read(1)
                if not b:
                    return bytes(out)
                out += b

def check(path, ref=None):
    d = open(path, 'rb').read()
    magic, blog, toc, tocsz = struct.unpack_from('<4sIII', d, 0)
    ok = True
    print(f"{path}: size={len(d)} magic={magic} block_log={blog} toc={toc:#x} toc_size={tocsz:#x}")
    if magic != b'TPZL':
        print("  FAIL magic"); return False
    n = tocsz // 8
    bs = 1 << blog
    prev_end = 0
    stats = {'lit_lens': {}, 'entry_max': 0, 'over_65600': 0}
    out_len = 0
    for i in range(n):
        off, sz = struct.unpack_from('<II', d, toc + i*8)
        if off < toc + tocsz or off + sz > len(d):
            print(f"  FAIL entry {i} bounds"); ok = False
        if off < prev_end:
            print(f"  WARN entry {i} overlaps"); ok = False
        prev_end = off + sz
        stats['entry_max'] = max(stats['entry_max'], sz)
        if sz > 65600:
            stats['over_65600'] += 1
        f = io.BytesIO(d[off:off+sz]); read = 0; streams = 0
        while read < bs:
            pos = f.tell()
            t = f.read(1)
            if not t: break
            f.seek(pos)
            chunk = inflate(f); streams += 1
            if not chunk: break
            read += len(chunk)
            if t[0] == 0x0F:
                stats['lit_lens'][len(chunk)] = stats['lit_lens'].get(len(chunk), 0) + 1
        if read != bs and i != n-1:
            print(f"  FAIL entry {i}: decompressed {read} != {bs}"); ok = False
        out_len += read
    print(f"  entries={n} out={out_len} entry_max={stats['entry_max']}")
    print(f"  literal chunk sizes: {stats['lit_lens']}")
    if stats['over_65600']:
        print(f"  WARN {stats['over_65600']} entries > 65600 (reference max)")
    if ref:
        r = open(ref, 'rb').read()
        same = sum(1 for i in range(n) if d[toc+i*8:toc+i*8+8] == r[toc+i*8:toc+i*8+8])
        print(f"  identical TOC entries vs reference: {same}/{n}")
    print("  RESULT:", "PASS" if ok else "FAIL")
    return ok

if __name__ == '__main__':
    ref = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == '--ref' else None
    check(sys.argv[1], ref)
