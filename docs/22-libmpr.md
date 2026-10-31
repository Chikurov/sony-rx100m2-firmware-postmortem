# `libmpr.so` — медиа-слой (наблюдения)

7,96 МБ, ELF ARM. Имя = «MPR» (Media Processor/Manager).

## Роль (по символам)

- фасады: `MprIf`, `MprIfMcmd` (`USBEntry`, `USBHostEntry`, `USBExit`,
  `NewUsbAviMMgr`);
- менеджеры носителей: `AviMMgrIf::NewFlashAviMMgr`,
  `NewMsAviMMgr`, `NewSsdAviMMgr`, `NewUsbAviMMgr`, `NewHddAviMMgr`,
  `DiscMMgrIf::NewDvdDcfMMgr`, `BgmMMgr`;
- операции: `FirstMount`, `Mount`, `GetStillData`, `GetStillDataExifInfo`;
- ошибки: `CS_AviMprIf::MPR2AVIErr`, `AVI2MPRErr`, `MPR2CSErr`.

То есть это слой доступа к носителям (флеш/SD/MS/SSD/USB/HDD/DVD) и
извлечения файлов (Still/EXIF), а не транспорт к DSP.

## Оговорка

Внутренняя логика (команды MPR, состояния) не разбиралась: библиотека
большая, stripped.
