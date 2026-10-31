# Архитектура и взаимодействия (диаграммы)

Схемы составлены по фактам из `docs/`; пунктир — предположения.

## 1. Состав прошивки и загрузка

```mermaid
flowchart TD
  EXE["Update_DSCRX100M2V110.exe<br/>PE32 + контейнер"] --> UFU["UFU<br/>DATV/PROV/UDID/FDAT/DEND"]
  UFU --> FDAT["FDAT<br/>AES-128-ECB, блоки 1024 Б"]
  FDAT --> TAR["TAR<br/>49 записей"]
  TAR --> CFG["config/partconf/loader"]
  TAR --> IMG["part_image:<br/>nflasha3, nflasha5(WBI), nflasha8"]
  TAR --> UXC["UXC/uxd ресурсы"]
  IMG --> N3["nflasha3: FAT12<br/>vmlinux + initrd + av-cam + sabin + bonobo"]
  IMG --> N8["nflasha8: ext2<br/>/usr (glibc, libObj, orb-server)"]
  IMG --> N5["nflasha5: WBI<br/>буфер записи (стирается)"]
  N3 --> BOOT["BootROM → ssboot → kernel 2.6.29"]
  BOOT --> INITRD["initrd AXFS → init"]
  INITRD --> ROOT["/usr ext2"]
  BOOT --> DSP["DSP: av-cam.bin + sabin/*.bin + bonobo.bin"]
```

## 2. Обновление (updater body)

```mermaid
sequenceDiagram
  participant C as config.xml
  participant S as shell-шаги
  participant K as kernel/модули
  participant N as NAND
  C->>S: config_sum → us_crc32sum + chkfirm + edit_mount
  S->>S: проверка CRC *.sum
  S->>N: edisx partinf.conf (разметка)
  S->>N: pformat3 (nandb, onenandboot)
  S->>N: uc_mkfs full|app
  S->>N: backup restore (ud_keep_backup)
  S->>N: ud_wbi_drop (стереть WBI)
  S->>K: перезагрузка в новую систему
```

## 3. Модули ядра (по графу зависимостей)

```mermaid
flowchart LR
  upm --> unidrv1
  unidrv2 --> unidrv1
  hdmi --> unidrv1
  cec --> hdmi
  cec --> unidrv1
  dmm --> unidrv1
  nfc --> unidrv2
  mcmn_drv --> unidrv1
  sata_drv --> mcmn_drv
  upm --> unidrv2
  unidrv2 -.->|wbi_drop| KERNEL["ядро: wbi_*"]
  upm -.->|wbi_drop| KERNEL
```

## 4. DSP art-effect

```mermaid
sequenceDiagram
  participant H as host (libObj)
  participant D as DSP
  H->>D: Start_Art_Effect (params 0x2B3…)
  D->>D: 0xC3915CE0 (планировщик)
  D->>D: callback 0xC391A5CC
  D->>D: 0xC391A93C → 0xC3791D2E → 0xC3791DD2
  D->>D: 0xC384184E/196A (геометрия)
  D->>D: 0xC3791EC2/2024/2140
  D->>D: FUN_c375442e(0x30,0x33…0x37)
  D-->>H: результат
```

## Ограничения

Схемы не показывают тайминги и реальные вызовы; DSP-часть — статический
каркас, а не трассировка.
