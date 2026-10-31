import struct, os, sys, zlib

class AXFS:
    def _init_maps(self):
        n = self.blocks
        self.types = [self.val('node_type', i) for i in range(n)]
        cb = {}; c = 0
        for i, t in enumerate(self.types):
            if t == 1:
                cb[i] = c; c += 1
        self.cblock_map = cb
        self.n_cblocks = c
        ba = {}; b = 0
        for i, t in enumerate(self.types):
            if t == 2:
                ba[i] = b; b += 1
        self.banode_map = ba

    def __init__(self, path):
        self.d = open(path,'rb').read()
        d = self.d
        self.be64 = lambda o: struct.unpack_from('>Q', d, o)[0]
        assert struct.unpack_from('>I', d, 0)[0] == 0x48A0E4CD
        self.size = self.be64(0x48); self.files = self.be64(0x40)
        self.blocks = self.be64(0x50); self.cblock = struct.unpack_from('>I', d, 0x3C)[0]
        names = ["strings","xip","byte_aligned","compressed","node_type","node_index",
                 "cnode_offset","cnode_index","banode_offset","cblock_offset",
                 "inode_file_size","inode_name_offset","inode_num_entries",
                 "inode_mode_index","inode_array_index","modes","uids","gids"]
        self.reg = {}
        for i,n in enumerate(names):
            o = self.be64(0x60 + 8*i)
            self.reg[n] = dict(off=self.be64(o), size=self.be64(o+8),
                               max=self.be64(o+24), depth=d[o+32])
        self._init_maps()
    def val(self, region, idx):
        r = self.reg[region]; depth = r['depth'] or 1
        v = 0
        for k in range(depth):
            v |= self.d[r['off'] + k*r['max'] + idx] << (8*k)
        return v
    def name(self, i):
        off = self.val('inode_name_offset', i)
        b = self.reg['strings']['off'] + off
        e = self.d.index(b'\0', b)
        return self.d[b:e].decode('utf-8','replace')
    def mode(self, i):
        mi = self.val('inode_mode_index', i)
        return self.val('modes', mi)
    def read_file(self, i):
        size = self.val('inode_file_size', i)
        first = self.val('inode_array_index', i)
        nblocks = self.val('inode_num_entries', i)
        out = bytearray()
        for b in range(nblocks):
            n = first + b
            t = self.types[n]
            want = min(self.cblock, size - b*self.cblock)
            if t == 0:  # XIP
                off = self.val('node_index', n) * self.cblock
                out += self.d[self.reg['xip']['off']+off:self.reg['xip']['off']+off+want]
            elif t == 2:  # byte aligned
                off = self.val('banode_offset', self.banode_map[n])
                out += self.d[self.reg['byte_aligned']['off']+off:self.reg['byte_aligned']['off']+off+want]
            elif t == 1:  # compressed
                ci = self.cblock_map[n]
                off = self.val('cblock_offset', ci)
                nxt = self.val('cblock_offset', ci+1) if ci+1 <= self.reg['cblock_offset']['max'] else self.reg['compressed']['size']
                raw = self.d[self.reg['compressed']['off']+off:self.reg['compressed']['off']+nxt]
                out += zlib.decompress(raw)[:want]
            else:
                raise ValueError('node type %d' % t)
        return bytes(out[:size])

def extract(path, outdir):
    a = AXFS(path)
    os.makedirs(outdir, exist_ok=True)
    def walk(inode, prefix):
        n = a.val('inode_num_entries', inode)
        first = a.val('inode_array_index', inode)
        for k in range(n):
            child = first + k
            name = a.name(child); full = os.path.join(prefix, name)
            m = a.mode(child)
            if (m & 0o170000) == 0o040000:
                os.makedirs(os.path.join(outdir, full), exist_ok=True)
                walk(child, full)
            elif (m & 0o170000) == 0o120000:
                target = a.read_file(child).decode('utf-8','replace')
                p = os.path.join(outdir, full)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                if not os.path.lexists(p):
                    os.symlink(target, p)
            else:
                data = a.read_file(child)
                p = os.path.join(outdir, full)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p,'wb').write(data)
    walk(0, '')
    return a

if __name__ == '__main__':
    a = extract(sys.argv[1], sys.argv[2])
    print("files", a.files, "blocks", a.blocks, "size", a.size)
