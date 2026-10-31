# `unidrv1.ko` — драйвер OneNAND

Модуль 153 604 Б, ELF ARM (ET_REL), символы сохранены.

## Что внутри (по символам)

- регистрация: `onenand_register`, `mms_register_nand_device`, `__nand_probe`;
- блочный слой: `read_sectors`, `write_sectors`, `erase_block`,
  `mms_rewrite`, `mms_sdmblk_do_ioctl`;
- LZP-разделы: `sdmlzp_register`, `sdmlzp_unregister`, `sdmlzp_request`,
  `sdm_setup_partition`, `sdm_load_partition_table`;
- режим DFS: `onenand_set_dfs_mode`;
- WBI: `sdmwbi_register` / `sdmwbi_unregister` (вызываются при
  переинициализации разделов).

## Таблица разделов (по псевдокоду `sdm_setup_partition`)

- читается 512-байтный заголовок с устройства;
- число разделов `count` ≤ 31;
- записи по 16 Б: `{start, size, flags, valid}`, где `start` и `size`
  должны быть кратны 512 (`& 0x1ff == 0`), `valid = flags & 1`;
- проверяется, что `start + size ≤` числа блоков устройства;
- при успехе число разделов сохраняется (`0x20`).

Строки: `error reading header from partition %d!`,
`found LZP partition %d : blksize=%x tbl1=%x`,
`0x%04x is badblock`, `OneNAND:read_req: replace ECC error block %d`.

## Оговорка

`.ko` — перемещаемый объект (ET_REL): без применения релокаций часть
констант в псевдокоде выглядит как код (например `0xE92D4030`).
Абсолютные адреса и «магические» значения требуют линковки/релокации.
