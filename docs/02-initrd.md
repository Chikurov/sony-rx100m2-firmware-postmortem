# initrd.img — AXFS (Advanced XIP FS)

ФАКТЫ, полученные разбором `systemfs/initrd.img` (3 223 552 Б).

## Суперблок (big-endian)

| Смещение | Поле | Значение |
|---|---|---|
| 0x00 | magic | `0x48A0E4CD` |
| 0x04 | signature | "Advanced XIP FS\0" (16 Б) |
| 0x14 | digest | 40 Б (SHA-1, здесь нули) |
| 0x3C | cblock_size | 4096 |
| 0x40 | files (inodes) | 660 |
| 0x48 | size | 3 223 552 |
| 0x50 | blocks (nodes) | 1180 (фактически 1183 записи в таблицах) |
| 0x58 | mmap_size | 3 223 552 |
| 0x60… | смещения дескрипторов регионов | 18 полей |

Версия: 1.9.1, compression_type = 0 (zlib).

## Дескриптор региона (36 Б, big-endian)

```
u64 fsoffset; u64 size; u64 compressed_size; u64 max_index; u8 depth; u8 incore;
```

Регионы: `strings`, `xip`, `byte_aligned`, `compressed`,
`node_type`, `node_index`, `cnode_offset`, `cnode_index`,
`banode_offset`, `cblock_offset`, `inode_*`, `modes`, `uids`, `gids`.

## Таблицы — byte-plane (важно)

Значения таблиц хранятся **плоскостями**: сначала младшие байты всех
элементов, затем следующая плоскость и т.д.

```
value[i] = p0[i] | p1[i]<<8 | p2[i]<<16 | p3[i]<<24
```

Это отличается от row-major логики в патче AXFS 2008 года — проверено
на `inode_name_offset` (0,3,7,11… → "./","bin","dev"…).

## Индексация узлов

- `node_type[node]`: 0 = XIP, 1 = compressed, 2 = byte_aligned.
- `node_index[node]`: номер блока по 4096 Б внутри XIP-региона
  (смещение = значение × 4096).
- `cblock_offset[cnode]`: смещение сжатого блока;
  `cnode = номер сжатого узла по порядку` (не `node`).
- `banode_offset[banode]`: смещение в byte_aligned-регионе;
  `banode = номер byte_aligned-узла по порядку`.
- Файл: `first = inode_array_index`, `n = inode_num_entries` (число блоков),
  `size = inode_file_size`; блоки — `node = first + b`.
- Каталог: `first` = первый inode ребёнка, `n` = число детей
  (дети идут подряд, обход depth-first).

## Что извлечено

`initrd_root/`: 562 файла, 74 симлинка, 24 каталога — ровно 660 inodes
(сверено с полем `files` суперблока), 4.5 МБ; из них 58 ELF
(39 модулей `*.ko` — валидные ELF ARM EABI4).

- `/bin/busybox` (324 484 Б, ELF ARM EABI4), applet-ссылки;
- `/lib/sonyld.so` (172 760 Б) — **ELF ARM** динамический загрузчик
  (`e_type=DYN`, entry 0xE48); на него указывает `/lib/libsonyld.so`;
- `/lib/*.so` — библиотеки загрузчика;
- `/etc` (`dhcpd.conf`, `toprc`), `/version.txt` = `23210_06.2014121901`;
- `/kmod/*.ko`: 39 модулей (`accel`, `cdrom`, `cec`, `compass`, `dmm`,
  `hdmi`, `htmd`, `kikilog`, `liro`, `mag`, `usb*`, `usbg_*`, …),
  vermagic `2.6.29.6-rt24-alp_nl SMP preempt mod_unload ARMv6`;
- `/lib/modules/2.6.29.6-rt24-alp_nl/` — `modules.dep`, `modules.alias`,
  `modules.usbmap` и др.;
- `/root/common.src` — скрипт updater core, `/root/chassis` = `CXD4132`.

## Инструмент

`axfs_extract.py` — парсер и распаковщик (`python3 axfs_extract.py
initrd.img outdir`).

## Ограничения

- digest (SHA-1) в образе нулевой — проверка целостности не выполнялась.
- `sonyld.so` — ELF DYN, точка входа 0xE48; внутренняя логика не разбиралась.
