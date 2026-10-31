# /usr (ext2) — пользовательские компоненты

556 файлов, ~91 МБ. Ниже — проверенные размеры и типы.

## bin (36)

| Файл | Размер | Назначение (по строкам/имени) |
|---|---|---|
| `orb-server` | 1 629 832 | сетевой/remote-сервер (запускается `WebApiLauncher.sh`) |
| `wpa_supplicant` | 1 160 552 | WiFi WPA |
| `adjstctl.elf` | 74 536 | управление юстировкой |
| `top` | 61 015 | busybox-подобный `top` |
| `im.elf`, `msdump.elf`, `sen.elf`, `bootin.elf`, `WS_SubProcess.elf` | 2–20 КБ | сервисные утилиты |
| `ulogio.elf`, `athtestcmd`, `rcvcmd.elf`, `sndcmd.elf`, `testcmd.elf` | — | отладка/тесты |
| `up.sh`, `change_mode.sh`, `network.sh`, `usb_insmod.sh` | — | скрипты запуска/режимов |

## lib (154)

| Файл | Размер | Роль (по символам) |
|---|---|---|
| `libObj.so` | 16 428 524 | UI/объектная модель; содержит `WrapperArtFilter::setArtFilter` |
| `libmpr.so` | 7 961 696 | медиа-подсистема (playback/record) |
| `libcrypto.so.0.9.8` | 1 232 936 | OpenSSL 0.9.8 |
| `libInfraDlnaControl.so` | 1 038 176 | DLNA |
| `viewUnified4.so` | 1 036 824 | UI |
| `libNetService.so` | 620 628 | сеть |
| `libSysDef.so` | 402 864 | системные определения |
| `libncurses.so.5.7` | 262 864 | TUI |

## glib

glibc 2.9: `libc-2.9.so`, `libm`, `libpthread`, `librt`, `libstdc++ 6.0.10`,
`ld-2.9.so`.

## kmod (4)

`ar6000.ko` (WiFi Atheros), `sdio_busdriver.ko`, `sdio_lib.ko`,
`mmcioWrapper.ko`.

## sabin (60)

DSP-модули алгоритмов: сигнатура `AA 0A 13 91`, имя `SA<NAME>__0.01`
(`SABFNR__0.01`, `SACAMDSP_BAYER` и др.) — аудио/видео/камера.

## share (244)

`app/` — UXC-ресурсы, шрифты (`Sony_DI_Icons.ttf`, `*.ltt`), `lang.uxb`,
`global.xdb`; `aveffect/`, `avsystemsound/`, `network/`, `pmbp/`,
`startbinary/logo.bin`, `terminfo/`.
