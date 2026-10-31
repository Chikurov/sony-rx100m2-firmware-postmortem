# Таблица символов ядра (kallsyms) — декодирована

В `vmlinux.bin` (raw ARM, база `0xC0008000`) найдены и декодированы
таблицы `kallsyms`:

| Таблица | Смещение | Размер |
|---|---|---|
| `kallsyms_addresses` | 0x1EA160 | 16 421 × u32 |
| `kallsyms_num_syms` | 0x1FA200 | 0x4025 = 16 421 |
| `kallsyms_names` | 0x1FA210 | до 0x224608 |
| `kallsyms_markers` | 0x224610 | 65 × u32 |
| `kallsyms_token_table` | 0x224720 | 899 Б |
| `kallsyms_token_index` | 0x224AB0 | 256 × u16 |

Проверка: смещения маркеров совпали с позициями каждой 256-й записи
(`[0, 2596, 5187, …]`), первая запись — `T__init_begin` по адресу
`0xC0008000`, последняя — `A_etext` (`0xC0277000`).

## Результат

`data/kallsyms.txt` — 16 421 символ: `адрес тип-имя`.

Например: `wbi_exec` `0xC004608C`, `wbi_send_sections` `0xC00463F4`,
`wbi_drop` `0xC0042CC4`, `wbi_register_compressor` `0xC0042CE4`.

## Как повторить

Скрипт: см. `tools/` (декодер в истории). Порядок таблиц:
`addresses → num_syms → names → markers → token_table → token_index`;
имена распаковываются по токенам из `token_table` через `token_index`.
