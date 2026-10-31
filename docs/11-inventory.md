# Инвентарь и опознание прошивки

## Прошивка

- Модель: **Sony DSC-RX100M2**, шасси **CXD4132**.
- Версия: **1.10** (FDAT `UDTRFIRM`, `0100`, model `0x32020010`, region 0).
- Пакет: `Update_DSCRX100M2V110.exe`, 110 469 120 Б,
  SHA-256 `0621fe4cce53c80497fbae3647ed6da1b621c9b12d6c423a4100f3271d630e5f`.

## Разделы (из `partinf.conf`)

| Раздел | Смещение | Размер | Назначение |
|---|---|---|---|
| nflasha1 | 0x00020000 | 4 МБ | updater |
| nflasha2 | 0x00420000 | 10 МБ | setting (vfat) |
| nflasha3 | 0x00E20000 | 21 МБ | system/main |
| nflasha5 | 0x02D20000 | 40 МБ | WBI (reserved) |
| nflasha7 | 0x05A20000 | 45 МБ | work (/tmp) |
| nflasha8 | 0x08720000 | 95 МБ | user (/usr, ext2) |
| nflasha12 | 0x0E620000 | 20.75 МБ | PMB |

## Инвентари (факты: имена, размеры, SHA-256)

| Файл | Что внутри |
|---|---|
| `data/inventory/initrd.txt` | 635 записей AXFS: файлы, симлинки, размеры, хеши |
| `data/inventory/usr.txt` | 556 записей ext2 `/usr` |
| `data/inventory/sabin.txt` | 60 DSP-модулей `sa_*.bin` |
| `data/inventory/updater-body.txt` | 38 файлов updater body |
| `data/inventory/part-images.txt` | 3 образа разделов (`nflasha3/5/8`) |

## Ключевые компоненты

- Ядро: Linux `2.6.29.6-rt24-alp_nl`, gcc 4.3.3, сборка 19.12.2014.
- initrd: AXFS, 660 inodes (24 каталога + 562 файла + 74 симлинка).
- 39 модулей `*.ko`, vermagic `2.6.29.6-rt24-alp_nl SMP preempt mod_unload ARMv6`.
- `/usr`: glibc 2.9, `libObj.so` 16,4 МБ, `libmpr.so` 8 МБ, 60 `sabin`-модулей.
- Updater body: версия `31.01.52`, chassis `CXD4132`.

## Как проверить у себя

1. Сверить SHA-256 исходного пакета с указанным выше.
2. Распаковать образ и сравнить хеши файлов с `data/inventory/*`.
3. Для `/usr` — `debugfs`/`e2fsck`, для initrd — `tools/axfs_extract.py`.

Все инвентари содержат только метаданные (имена, размеры, хеши) —
кода Sony в репозитории нет.
