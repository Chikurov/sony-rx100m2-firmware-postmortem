# Sony RX100M2 — разбор прошивки и как я её убил

![status](https://img.shields.io/badge/status-bricked-red)
![device](https://img.shields.io/badge/device-DSC--RX100M2-lightgrey)
![firmware](https://img.shields.io/badge/firmware-1.10-blue)
![tools](https://img.shields.io/badge/tools-Ghidra%2012.1.4-informational)

> [!WARNING]
> Камера после кастомной сборки **не загружается**. Это разбор ошибок,
> а не инструкция. Перед повторением прочитайте
> [ПРАВИЛА.md](reports/ПРАВИЛА.md) и чек-лист ниже.

**EN:** Reverse engineering of the Sony DSC-RX100M2 v1.10 firmware
(UFU/FDAT/TPZL, AXFS, UXC, DSP) and a postmortem of a failed custom
build that bricked the camera.

---

## Структура

```
docs/     разбор форматов (00–10)
reports/  отчёт, итоги, выводы, уроки, правила, журнал находок
tools/    axfs_extract, verify_tpzl, lzpt, pack_lzpt, build_fw
data/     карта функций DSP (23 088) и 256 сигнатур
```

## Что разобрано

| Объект | Результат | Документ |
|---|---|---|
| Внешний апдейтер | PE32 + контейнер, 25 файлов, подпись Sony (PKCS#7) | [docs/01](docs/01-containers.md) |
| UFU/FDAT | AES-128-ECB, блоки 1024 Б, CRC16, DEND CRC32 | [docs/01](docs/01-containers.md) |
| TAR | 49 записей: конфиги, образы разделов, UXC | [docs/01](docs/01-containers.md) |
| TPZL | LZ77 (0xF0/0x0F); эталон: literal 4096, запись ≤ 65600 | [docs/01](docs/01-containers.md) |
| nflasha3 | FAT12: ядро 2.6.29.6-rt24-alp_nl, initrd, `av-cam.bin` | [docs/06](docs/06-boot.md) |
| nflasha8 | ext2: 556 файлов, glibc 2.9, `libObj.so` 16,4 МБ | [docs/07](docs/07-userland.md) |
| AXFS (initrd) | 660 inodes: 24 каталога, 562 файла, 74 симлинка; 39 `.ko` | [docs/02](docs/02-initrd.md) |
| UXC | строки `{u16 id; u16 0x1E04; str}`, цвета `{u16 id; u16 0x3A09; RGBA}` | [docs/03](docs/03-uxc.md) |
| DSP `av-cam.bin` | база `0xC3440000`, 23 088 функций, 118 параметров | [docs/05](docs/05-dsp.md) |
| Art-effect | `Start_Art_Effect → 0xC3915CE0 → callback 0xC391A5CC` | [docs/05](docs/05-dsp.md) |

Краткая сводка — [ИТОГИ.md](reports/ИТОГИ.md). Полный отчёт —
[ОТЧЁТ_О_РАБОТЕ.md](reports/ОТЧЁТ_О_РАБОТЕ.md). Журнал фактов —
[НАХОДКИ.md](reports/НАХОДКИ.md).

## Почему не сработало

| Причина | Статус |
|---|---|
| Патч был мёртвым: рабочая копия `setArtFilter` — в `libObj.so`, не в `wrapperArtFilter.so` | ФАКТ |
| TPZL пересобран с literal 65535 вместо эталонных 4096 | ФАКТ |
| Метаданные ext2 изменены (`uid/gid 0`, даты 2026) | ФАКТ |
| Точная причина отказа на стороне камеры | НЕИЗВЕСТНО (нет консоли) |

Структурные проверки (CRC, `fsck`, round-trip) проходили — но они не
проверяют совместимость с декомпрессором устройства.

## Инструмент, который ловит эту ошибку

```
$ python3 tools/verify_tpzl.py reference.tpzl
literal chunk sizes: {4096: 710}              PASS

$ python3 tools/verify_tpzl.py custom.tpzl
literal chunk sizes: {65535: 1394, 1: 1394}   ← вне эталона
```

## Чек-лист перед прошивкой

1. Доказать, что правка **исполняется** (`DT_NEEDED`, `dlopen`,
   дубликаты символов).
2. Менять минимум байт; остальное — байт-в-байт.
3. Перекодировать только затронутые блоки, строго в границах эталона.
4. `verify_tpzl.py --ref` — literal-размеры должны совпадать с эталоном.
5. Пересборка без изменений = байт-в-байт оригинал.
6. Вернуть `uid/gid/права/даты`, проверить `fsck` и чтение обратно.
7. Убедиться, что откат **не зависит** от изменяемого раздела.
8. Только потом — устройство и явное подтверждение.

## Открытые вопросы

Числовые «рецепты» эффектов (формируются в рантайме), WBI1, таблица UXC,
внутренности `sonyld.so`, сырой дамп NAND — см.
[docs/08-open-questions.md](docs/08-open-questions.md).

## Последствия

Камера выставлена на продажу как донор. Ответственность за решение
прошивать — на агенте: оценка риска была необоснованной.

## Лицензия

Код — MIT, текст — CC BY 4.0. Используйте на свой риск.
