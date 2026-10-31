# Граф зависимостей модулей ядра

Рёбер: **57** (импорт символа из другого модуля).

| Откуда | Куда | Ссылок |
|---|---|---|
| `upm.ko` | `unidrv1.ko` | 1182 |
| `unidrv2.ko` | `unidrv1.ko` | 227 |
| `hdmi.ko` | `unidrv1.ko` | 96 |
| `cec.ko` | `unidrv1.ko` | 78 |
| `dmm.ko` | `unidrv1.ko` | 78 |
| `nfc.ko` | `unidrv2.ko` | 66 |
| `cec.ko` | `hdmi.ko` | 63 |
| `mcmn_drv.ko` | `unidrv1.ko` | 63 |
| `sata_drv.ko` | `mcmn_drv.ko` | 61 |
| `upm.ko` | `unidrv2.ko` | 61 |
| `msen_drv.ko` | `unidrv1.ko` | 59 |
| `accel.ko` | `unidrv1.ko` | 47 |
| `usb_portMonitor.ko` | `unidrv1.ko` | 47 |
| `ms_drv.ko` | `unidrv1.ko` | 45 |
| `nfc.ko` | `unidrv1.ko` | 43 |
| `sd_mod.ko` | `scsi_mod.ko` | 42 |
| `mag.ko` | `unidrv1.ko` | 41 |
| `mmc_drv.ko` | `mcmn_drv.ko` | 37 |
| `kikilog.ko` | `unidrv1.ko` | 36 |
| `usbg_buspower.ko` | `unidrv1.ko` | 35 |
| `usb_max14648.ko` | `unidrv1.ko` | 33 |
| `liro.ko` | `unidrv2.ko` | 32 |
| `liro.ko` | `unidrv1.ko` | 31 |
| `mcmn_drv.ko` | `unidrv2.ko` | 29 |
| `compass.ko` | `unidrv1.ko` | 28 |
