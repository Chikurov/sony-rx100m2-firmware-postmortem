# Загрузка, ядро и initrd

## Цепочка

```
sabin (ssboot / sa_dfdet / idt_cam)
  → vmlinux.bin (nflasha3, FAT12)
  → initrd.img (AXFS)  → /
  → /usr (nflasha8, ext2)  → приложение/UI
```

## Ядро

- `Linux 2.6.29.6-rt24-alp_nl`, `#1 SMP PREEMPT RT`,
  gcc 4.3.3 (Sony CE Linux 6.0.0.4), сборка 19.12.2014 15:30 JST.
- Размер `vmlinux.bin` — 2 747 296 Б.
- В строках ядра: `nand_fdmac`, `RAMDISK: cramfs/squashfs filesystem found`,
  `axfs: wrong axfs signature`.

## initrd (AXFS)

- 660 inodes, 562 файла, 74 симлинка, 4,5 МБ.
- `/bin/busybox` — ELF ARM EABI4, 324 484 Б.
- `/lib`: `libsonyc`, `libsonycrypt` (NetBSD crypt/md5crypt), `libsonydl`,
  `libsonyld` → `sonyld.so` (сырой ARM-код, 172 760 Б), `libsony*`.
- `/kmod` — 39 модулей: `accel`, `cdrom`, `cec`, `compass`, `dmm`, `hdmi`,
  `htmd`, `kikilog`, `liro`, `mag`, `mcmn_drv`, `mmc_drv`, `ms_drv`,
  `msen_drv`, `nfc`, `sata_drv`, `scsi_mod`, `scsi_wait_scan`, `sd_mod`,
  `sircs`, `sr_mod`, `stream`, `stream2`, `unidrv1`, `unidrv2`, `upm`,
  `usb-storage`, `usb_buspwr`, `usb_current`, `usb_extcmd`, `usb_max14648`,
  `usb_portMonitor`, `usb_shcd`, `usbcore`, `usbg_*`.
- `/version.txt` = `23210_06.2014121901`.

## /usr (ext2, отдельный раздел)

- glibc 2.9 в `/glib`, интерпретатор `/lib/libsonyld.so` (из initrd).
- `kmod`: `ar6000.ko` (WiFi), `sdio_busdriver`, `sdio_lib`, `mmcioWrapper`.
- `sabin`: 60 DSP-модулей алгоритмов (`AA0A1391`, `SA…__0.01`).

## Updater body

cramfs в FDAT: версия 31.01.52, CXD4132; `libupdaterbody`, `us_*.sh`,
`ud_*.elf`, `pformat3.elf`; проверки — CRC32.
