# Документация по прошивке Sony DSC-RX100M2 v1.10

| Файл | Содержание |
|---|---|
| [00-overview.md](00-overview.md) | устройство, цепочка загрузки, карта разделов, состав `/usr` |
| [01-containers.md](01-containers.md) | внешний контейнер, UFU/FDAT, TAR, TPZL, WBI1, UXC |
| [02-initrd.md](02-initrd.md) | AXFS: суперблок, дескрипторы, таблицы, извлечение |
| [03-uxc.md](03-uxc.md) | формат UXC: строки, цвета |
| [04-wbi.md](04-wbi.md) | раздел `nflasha5` (WBI1) |
| [05-dsp.md](05-dsp.md) | `av-cam.bin`: формат, символы, таблица параметров |
| [06-boot.md](06-boot.md) | ядро, initrd, модули, `/usr` |
| [07-userland.md](07-userland.md) | пользовательские бинарники и библиотеки |
| [08-open-questions.md](08-open-questions.md) | что осталось неразобранным |
| [09-dsp-api.md](09-dsp-api.md) | инвентарь 256 сигнатур DSP |
| [10-artifacts.md](10-artifacts.md) | SHA-256 ключевых артефактов |
| [11-inventory.md](11-inventory.md) | опознание прошивки, разделы, инвентари |

Инструменты: `tools/axfs_extract.py`, `tools/verify_tpzl.py`, `tools/lzpt.py`,
`tools/pack_lzpt.py`, `tools/build_fw.py`, `tools/repack_test.py`,
`tools/make_test_fdat.py`. Данные: `data/` (инвентари, карта функций, сигнатуры).
