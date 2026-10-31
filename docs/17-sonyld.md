# `libsonyld.so` — загрузчик Sony

ФАКТЫ из ELF-заголовка и динамической секции (`initrd_root/lib/sonyld.so`):

- 172 760 Б, ELF32 ARM EABI4, тип DYN, stripped;
- SONAME `libsonyld.so`, **нет `DT_NEEDED`** — самодостаточен;
- entry `0xE48`, `INIT` `0xCD0`, `FINI` `0x23D68`,
  `INIT_ARRAY` `0x2F000` (1 запись);
- экспорт: `__dlopen`, `__dlsym`, `__dladdr`, `rtld_dlerror`,
  TLS-хелперы (`_rtld_tls_*`), `_sony_rtld_exidx`;
- строки: `/etc/ld.so.cache`, `Fatal error`, `%s: read error: %s`.

## Кто его использует (ФАКТ)

`PT_INTERP` многих утилит `/bin` указывает на `/lib/libsonyld.so`:
`GPIO2SDIO.elf`, `SetPort.elf`, `adjstctl.elf`, `bootin.elf`, `bk.elf`,
`im.elf`, `mpr_monio.elf` и др.

При этом основные приложения (например `orb-server`) используют
glibc-загрузчик `/usr/glib/ld-linux.so.3`. То есть в системе два
независимых runtime-мира.

## Ограничения

Внутренняя логика (разрешение символов, `dlopen`, TLS) не разбиралась:
библиотека stripped, символов мало.
