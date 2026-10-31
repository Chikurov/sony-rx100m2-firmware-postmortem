# Как работает обновление (updater body)

Источник: `config.xml`, `*.sh`, `body_version` (31.01.52, CXD4132).
ФАКТЫ — из скриптов; пометки «вероятно» — вывод по коду.

## Шаги (из config.xml)

Каждый `proc` привязан к файлу сумм и запускает shell/dll:

| Ключ | Что делает |
|---|---|
| `config_sum/config.sum` | `us_crc32sum.sh` + `chkfirm.sh` + `edit_mount.sh` + `keep_big_backup.sh` |
| `updater_sum/updater.sum` | проверка CRC образа обновлятора |
| `appli_sum/appli.sum` | проверка CRC приложений |
| `part_image_sum/part_image.sum` | проверка CRC образов разделов |
| `partconf/partinf.conf` | `chknandcapa.elf` + `loader_writer.sh` (pformat3) |
| `partconf_sum/partconf.sum` | CRC + `us_mkfs.sh` |
| `front_sum` / `ca_sum` | прошивка фронтальной/CA-части (`ud_frfup2.elf`, `uc_ca_firmup.elf`) |
| `backup_sum` / `prfile_sum` / `accsy_sum` | backup/настройки/аксессуары |

## Порядок в `us_mkfs.sh`

1. Проверяет наличие `mount.conf` и `partinf.conf` (иначе LED-код `0x41`).
2. `edisx.elf /dev/nflasha -f partinf.conf` — разметка.
3. При необходимости `pformat3.elf /dev/nflashb -v -onenandboot` и
   `edisx.elf /dev/nflashb -f partinf1.conf`.
4. `uc_mkfs.elf -m full|app -f mount.conf` — форматирование разделов.
5. Backup: `ud_keep_backup.elf -s`, восстановление из `/setting`.
6. `ud_wbi_drop.elf partinf.conf` — обработка WBI (код `0x68`).
7. `dosfsck -Y /dev/nflasha2`, монтирование `/setting`, служебные файлы
   (`/setting/sen/smode`).

## Режимы (`UPDATER_ACTION_MODE`)

`PRODUCT=1`, `LOADER_UPDATER=2`, `USER=3`, `SERVICE=4`, `MINOR=5`,
`MSCRYPT=6`, `VERSKIP=7`. От режима зависит `fmode` (`full`/`app`) и
объём записи (например, USER/MINOR пропускают запись загрузчика).

## Флаги следующей загрузки

`/setting/updater/mode*` (`up.sh`, `startupdate.sh`): наличие флага
переключает следующую загрузку в режим UFP/обновления.

## LED-коды ошибок (из скриптов)

`0x41` firmware, `0x51` plugin, `0x52` bad block, `0x61` partition,
`0x62` logical format, `0x66` CA, `0x68` WBI drop, `0x72` mount.

## Что это значит для модификаций

- Разметка и формат делаются **до** записи образов; ошибка на любом шаге
  оставляет систему в промежуточном состоянии.
- Загрузчик пишется только в режимах PRODUCT/LOADER_UPDATER — это самый
  опасный этап.
- Проверки — CRC32, модель/LSI; подписи в этом пути нет.
