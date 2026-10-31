# DSC-RX100M2: обзор прошивки

Все утверждения ниже — ФАКТ, если не помечено иначе.

## Устройство и прошивка

- Модель: Sony DSC-RX100M2, шасси **CXD4132**.
- Прошивка: **1.10** (FDAT: `UDTRFIRM`, version `0100`, model `0x32020010`, region 0).
- Пакет: `Update_DSCRX100M2V110.exe`, 110 469 120 Б,
  SHA-256 `0621fe4cce53c80497fbae3647ed6da1b621c9b12d6c423a4100f3271d630e5f`.

## Цепочка загрузки (ФАКТ по содержимому)

1. Загрузчик (`sabin`: `ssboot.bin`, `ssboot_any.bin`, `sa_dfdet.bin`, `idt_cam.bin`).
2. Ядро Linux **2.6.29.6-rt24-alp_nl** (gcc 4.3.3, Sony CE Linux 6.0.0.4,
   сборка 19.12.2014) — `vmlinux.bin` из `nflasha3`.
3. `initrd.img` — **AXFS** (Advanced XIP FS).
4. Корень `/` — из initrd; `/usr` — ext2 с раздела `nflasha8`.
5. Приложение/UI — ELF ARM EABI5, интерпретатор `/lib/libsonyld.so`
   (в образе `/usr` его нет — он в initrd).

## Карта разделов (из `partinf.conf`)

| Раздел | Смещение | Размер | Назначение |
|---|---|---|---|
| nflasha1 | 0x00020000 | 4 МБ | updater |
| nflasha2 | 0x00420000 | 10 МБ | setting (vfat) |
| nflasha3 | 0x00E20000 | 21 МБ | system/main (raw) |
| nflasha4 | 0x02320000 | 10 МБ | MPR backup |
| nflasha5 | 0x02D20000 | 40 МБ | WBI (reserved) |
| nflasha6 | 0x05520000 | 5 МБ | Jiritsu |
| nflasha7 | 0x05A20000 | 45 МБ | work (/tmp) |
| nflasha8 | 0x08720000 | 95 МБ | user (/usr, ext2) |
| nflasha12 | 0x0E620000 | 20.75 МБ | PMB |

## Что лежит в `/usr` (nflasha8, ext2)

556 файлов, ~91 МБ:

| Каталог | Файлов | Что |
|---|---|---|
| `bin` | 36 | сервисные ELF (`scenario.elf`, `orb-server`, `testcmd` и др.) |
| `sbin` | 2 | `dhcpd`, `pump` |
| `lib` | 154 | библиотеки камеры (`libObj.so` 16 МБ, `wrapper*`, `libInfra*`) |
| `glib` | 15 | glibc 2.9 (libc, libm, libpthread, libstdc++) |
| `kmod` | 4 | `ar6000.ko` (WiFi), `sdio_*` |
| `sabin` | 60 | DSP-модули алгоритмов, сигнатура `AA0A1391`, имена `SA…__0.01` |
| `scenario` | 32 | сценарии AV (`AVBB_SCN_*`) |
| `share` | 244 | ресурсы: UXC, шрифты, языки, `global.xdb` |
| `tool`, `wlan` | 9 | отладка, WiFi-утилиты |

## Updater body (cramfs в FDAT)

38 файлов, версия **31.01.52**, шасси CXD4132: `libupdaterbody.so`,
`libupdatercommon.so`, `config.xml`, `us_*.sh`, `ud_*.elf`, `pformat3.elf`.
Проверки целостности — **CRC32** (`uc_crc32sum.elf`), проверки модели/LSI.
