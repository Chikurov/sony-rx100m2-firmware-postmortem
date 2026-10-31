# Ядро: `ext2` и сеть (по символам)

`ext2`: **97** функций; сеть (net/tcp/udp/ip/sock): **489**.

## ext2 по категориям

| Категория | Функций |
|---|---|
| other | 51 |
| inode | 17 |
| dir | 8 |
| super | 6 |
| free | 5 |
| alloc | 4 |
| file | 3 |
| group | 1 |
| reserv | 1 |
| truncate | 1 |

## Примеры ext2

| Адрес | Функция |
|---|---|
| `0xc00ec694` | `ext2_bg_has_super` |
| `0xc00ec720` | `ext2_bg_num_gdb` |
| `0xc00ec73c` | `ext2_get_group_desc` |
| `0xc00ec7e0` | `ext2_count_free_blocks` |
| `0xc00ec89c` | `ext2_discard_reservation` |
| `0xc00eca24` | `ext2_try_to_allocate` |
| `0xc00ecddc` | `ext2_free_blocks` |
| `0xc00ed0a8` | `ext2_init_block_alloc_info` |
| `0xc00ed118` | `ext2_rsv_window_add` |
| `0xc00ed1a8` | `ext2_try_to_allocate_with_rsv` |
| `0xc00ed654` | `ext2_new_blocks` |
| `0xc00edb7c` | `ext2_new_block` |

## Примеры сети

| Адрес | Функция |
|---|---|
| `0xc0029d2c` | `netdev_init` |
| `0xc0029ff4` | `netdev_boot_setup` |
| `0xc002a2ac` | `netlink_net_init` |
| `0xc002a598` | `ip_static_sysctl_init` |
| `0xc002a6d4` | `ip_rt_init` |
| `0xc002a8c0` | `ip_rt_do_proc_init` |
| `0xc002a9c8` | `ip_init` |
| `0xc002aa20` | `tcp_init` |
| `0xc002adf4` | `tcp_v4_init` |
| `0xc002ae30` | `tcp_sk_init` |
| `0xc002aed0` | `udp_table_init` |
| `0xc002af28` | `udp_init` |
