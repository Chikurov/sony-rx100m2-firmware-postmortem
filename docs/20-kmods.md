# Драйверы ядра из initrd

Всего **39** модулей `*.ko` (ELF ARM, символы не удалены).

| Модуль | Размер | Функций | Заметки |
|---|---|---|---|
| `accel.ko` | 16536 | 8 |  |
| `cdrom.ko` | 37980 | 18 |  |
| `cec.ko` | 81504 | 242 | CEC (HDMI control) |
| `compass.ko` | 6552 | 7 |  |
| `dmm.ko` | 169396 | 208 | менеджер памяти/буферов (DMM) |
| `hdmi.ko` | 140492 | 316 | HDMI-контроллер (много `hdmi_core_*`) |
| `htmd.ko` | 5272 | 4 |  |
| `kikilog.ko` | 36612 | 56 |  |
| `liro.ko` | 70480 | 195 | `[LIRO] resume/suspend (WBI)` |
| `mag.ko` | 14204 | 7 |  |
| `mcmn_drv.ko` | 71740 | 125 |  |
| `mmc_drv.ko` | 102112 | 341 | SD/MMC |
| `ms_drv.ko` | 244776 | 606 | Memory Stick |
| `msen_drv.ko` | 28568 | 53 |  |
| `nfc.ko` | 15816 | 34 |  |
| `sata_drv.ko` | 71496 | 93 |  |
| `scsi_mod.ko` | 111924 | 252 | SCSI core (для USB mass storage) |
| `scsi_wait_scan.ko` | 2440 | 2 |  |
| `sd_mod.ko` | 28812 | 31 |  |
| `sircs.ko` | 11464 | 13 |  |
| `sr_mod.ko` | 18444 | 30 |  |
| `stream.ko` | 4228 | 6 | `stream_ioctl`, `stream_mmap` |
| `stream2.ko` | 5016 | 6 | `stream_ioctl`, `stream_mmap` |
| `unidrv1.ko` | 153604 | 342 | NAND/OneNAND: `onenand_register`, `__nand_probe`, `nflasha`, `onenand_set_dfs_mode` |
| `unidrv2.ko` | 175548 | 312 | импортирует `wbi_drop`, `wbi_drop() error` |
| `upm.ko` | 138608 | 263 | `upm_senser_wbi_drop`, `k_dfs_do_full_nand`, `wbi_drop` |
| `usb-storage.ko` | 28048 | 50 |  |
| `usb_buspwr.ko` | 14556 | 18 |  |
| `usb_current.ko` | 5408 | 11 |  |
| `usb_extcmd.ko` | 15632 | 31 |  |
| `usb_max14648.ko` | 43080 | 40 |  |
| `usb_portMonitor.ko` | 21748 | 21 |  |
| `usb_shcd.ko` | 31060 | 52 |  |
| `usbcore.ko` | 127312 | 270 | USB core |
| `usbg_buspower.ko` | 15720 | 43 |  |
| `usbg_cmn.ko` | 4604 | 10 |  |
| `usbg_sen.ko` | 32872 | 57 |  |
| `usbg_stillimage.ko` | 24416 | 65 |  |
| `usbg_storage.ko` | 72404 | 222 |  |
