import struct, zlib, sys
from pack_lzpt import pack_lzpt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
KEY=bytes.fromhex("E3B0C44298FC1C149AFBF4C8996FB924")
def aes(): return Cipher(algorithms.AES(KEY), modes.ECB())

def enc(plain):
    out=bytearray(); bs=1020; total=(len(plain)+bs-1)//bs; ctx=aes().encryptor()
    for i in range(total):
        chunk=plain[i*bs:(i+1)*bs]; size=len(chunk)
        block=bytearray(4)+chunk+b'\xff'*(bs-size)
        struct.pack_into('<H',block,2,size|(0x8000 if i==total-1 else 0))
        struct.pack_into('<H',block,0,sum(struct.unpack_from('<511H',block,2))&0xffff)
        out+=ctx.update(bytes(block))
    return bytes(out)

def parse_tar(buf):
    off=0; res=[]
    while off+512<=len(buf):
        h=buf[off:off+512]
        if h[:1]==b'\0': break
        name=h[:100].split(b'\0')[0].decode('latin1')
        size=int(h[124:136].rstrip(b'\0 ') or b'0',8)
        res.append((name,off,size,h))
        off+=512+((size+511)//512)*512
    return res

def tar_header(size, hdr):
    h=bytearray(hdr)
    h[124:136]=("%011o\0"%size).encode()
    h[148:156]=b' '*8
    c=sum(h)
    h[148:156]=("%06o\0 "%c).encode()
    return bytes(h)

def rebuild_tar(orig, repl):
    out=bytearray()
    for name,off,size,h in parse_tar(orig):
        data=repl.get(name, orig[off+512:off+512+size])
        out+=tar_header(len(data),h)+data+b'\0'*((-len(data))%512)
    out+=b'\0'*1024
    return bytes(out)

def build(n8_tpzl, out_path):
    orig_tar=open("firmware_image.bin","rb").read()
    # update part_image.sum
    ents={n:(o,s) for n,o,s,_ in parse_tar(orig_tar)}
    so,ss=ents["0701_part_image_sum/part_image.sum"]
    old_sum=orig_tar[so+512:so+512+ss].decode()
    lines=[]
    for ln in old_sum.strip().split('\n'):
        p=ln.split(',')
        if p[-2]=="dev/nflasha8":
            p[1]="%08x"%(zlib.crc32(n8_tpzl)&0xffffffff)
            p[2]="%08x"%len(n8_tpzl)
        lines.append(','.join(p))
    new_sum=('\n'.join(lines)+'\n').encode()
    tar=rebuild_tar(orig_tar,{"0700_part_image/dev/nflasha8":n8_tpzl,"0701_part_image_sum/part_image.sum":new_sum})
    fs = open("fs_image.bin","rb").read()
    hdr=bytearray(512)
    hdr[0:8]=b'UDTRFIRM'; hdr[12:16]=b'0100'
    hdr[16:17]=b'U'; hdr[20:21]=b'N'
    hdr[32]=0x10; hdr[33]=0x01
    struct.pack_into('<II',hdr,36,0x32020010,0)
    fw_off=0x200+len(fs)
    struct.pack_into('<III',hdr,48,fw_off,len(tar),2)
    struct.pack_into('<c3xII4x',hdr,64,b'U',0x200,len(fs))
    struct.pack_into('<c3xII4x',hdr,80,b'P',0x200,0)
    plain=bytes(hdr)+fs+tar
    struct.pack_into('<I',hdr,8,0)
    plain=bytes(hdr)+fs+tar
    struct.pack_into('<I',hdr,8,zlib.crc32(plain[12:512])&0xffffffff)
    plain=bytes(hdr)+fs+tar
    ct=enc(plain)
    body=bytearray()
    body+=b'\x89UFU\r\n\x1a\n'
    body+=b'\x00\x00\x00\x04DATV'+struct.pack('<I',1)
    body+=b'\x00\x00\x00\x04PROV'+struct.pack('<I',1)
    udid=open("fw_extract/FirmwareData_DSCRX100M2V110.dat","rb").read()[0x28:0x54]
    body+=b'\x00\x00\x00\x2cUDID'+udid
    body+=struct.pack('>I',len(ct))+b'FDAT'+ct
    body+=b'\x00\x00\x00\x04DEND'+struct.pack('>I',zlib.crc32(bytes(body))&0xffffffff)
    open(out_path,"wb").write(bytes(body))
    print("built",out_path,len(body),"tar",len(tar),"tpzl",len(n8_tpzl))

if __name__=='__main__':
    img=open("nflasha8.img","rb").read()
    tp=pack_lzpt(img)
    open("nflasha8_test.tpzl","wb").write(tp)
    build(tp,"test_fw.dat")
