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

Инструменты: `axfs_extract.py`, `verify_tpzl.py`, `lzpt.py`,
`pack_lzpt.py`, `build_fw.py`.
