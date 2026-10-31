# Тела модулей ядра: карта функций

Всего функций в модулях: **4460**.
Каждый `.ko` слинкован (`tools/link_ko.py`), рядом лежит `.syms`.

| Модуль | Функций | Ключевые |
|---|---|---|
| `accel.ko` | 8 | `accel_exit`, `accel_init` |
| `cdrom.ko` | 18 | `cdrom_mrw_exit`, `cdrom_ioctl`, `cdrom_open` |
| `cec.ko` | 242 | `cec_dev_write`, `cec_dev_read`, `cec_dev_ioctl`, `cec_dev_open`, `cec_module_exit` |
| `compass.ko` | 7 | `compass_exit`, `compass_init` |
| `dmm.ko` | 208 | `proc_write`, `dmm_udm_slock_spin_lock_init` |
| `hdmi.ko` | 316 | `hdmi_dev_write`, `hdmi_dev_read`, `hdmi_dev_ioctl`, `hdmi_dev_open`, `hdmi_module_exit` |
| `htmd.ko` | 4 | `htd_probe` |
| `kikilog.ko` | 56 | `kikilog_fops_open`, `kikilog_fops_ioctl`, `combilog_init`, `kikilog_proc_write`, `kikilog_init` |
| `liro.ko` | 195 | `proc_delay_write`, `liro_exit`, `liro_init`, `os_set_thread_register`, `malloc_init` |
| `mag.ko` | 7 | `mag_exit`, `mag_init` |
| `mcmn_drv.ko` | 125 | `mcmnd_drv_open`, `mcmnd_exit`, `mcmnd_init`, `mcmnd_drv_ioctl`, `mcmnd_ioctl` |
| `mmc_drv.ko` | 341 | `mmc_probe`, `mmc_driver_exit`, `mmc_driver_init`, `multi_lun_ioctl`, `mmcd_char_open` |
| `ms_drv.ko` | 606 | `ms_open`, `ms_char_open`, `ms_exit`, `ms_char_ioctl`, `ms_init` |
| `msen_drv.ko` | 53 | `msen_init`, `msen_driver_init`, `msen_exit`, `msen_driver_exit`, `msen_uipc_exit` |
| `nfc.ko` | 34 | `nfc_rsrc_exit`, `nfc_rsrc_init`, `nfc_rsrc_sio_init`, `nfc_rsrc_thread_exit`, `nfc_rsrc_timer_init` |
| `sata_drv.ko` | 93 | `sata_udif_cdev_init`, `sata_udif_cdev_register`, `sata_ioctl` |
| `scsi_mod.ko` | 252 | `scsi_sony_ext_open`, `scsi_sony_ext_ioctl`, `proc_scsi_devinfo_open`, `proc_scsi_devinfo_write`, `proc_scsi_read` |
| `scsi_wait_scan.ko` | 2 |  |
| `sd_mod.ko` | 31 | `sd_probe`, `sd_ioctl`, `sd_open` |
| `sircs.ko` | 13 | `sircs_init`, `sircs_exit`, `sircs_probe` |
| `sr_mod.ko` | 30 | `sr_open`, `sr_block_ioctl`, `sr_block_open`, `sr_probe`, `sr_vendor_init` |
| `stream.ko` | 6 | `stream_exit`, `stream_ioctl`, `stream_init` |
| `stream2.ko` | 6 | `stream_exit`, `stream_ioctl`, `stream_init` |
| `unidrv1.ko` | 342 | `fsp_probe`, `fsp_exit`, `fsp_init`, `udif_dmac_open`, `udif_dmac_ioctl` |
| `unidrv2.ko` | 312 | `ulogio_module_exit`, `ulogio_module_init`, `backup_open`, `backup_ioctl`, `backup_read` |
| `upm.ko` | 263 | `k_upm_exit`, `k_upm_init`, `k_upm_kikilog_if_init`, `k_upm_kikilog_if_exit`, `k_dfs_do_init_register` |
| `usb-storage.ko` | 50 | `storage_probe`, `option_ms_init`, `sierra_ms_init`, `usb_stor_huawei_e220_init`, `usb_stor_euscsi_init` |
| `usb_buspwr.ko` | 18 | `usb_buspwr_fops_open`, `usb_buspwr_exit`, `usb_buspwr_init`, `usb_buspwr_fops_ioctl` |
| `usb_current.ko` | 11 | `usb_current_fops_open`, `usb_current_exit`, `usb_current_fops_ioctl`, `usb_current_init` |
| `usb_extcmd.ko` | 31 | `extcmd_open`, `list_init`, `extcmd_ioctl` |
| `usb_max14648.ko` | 40 | `usb_max14648_fops_open`, `usb_max14648_fops_ioctl`, `usb_max14648_exit`, `usb_max14648_proc_read`, `usb_max14648_init` |
| `usb_portMonitor.ko` | 21 | `usb_portMonitor_fops_open`, `usb_portMonitor_exit`, `usb_portMonitor_fops_ioctl`, `usb_portMonitor_init` |
| `usb_shcd.ko` | 52 | `scd_host_intf_probe`, `usb_scd_hcd_exit`, `scd_hep_cntl_init`, `scd_port_init`, `scd_hep_rx_init` |
| `usbcore.ko` | 270 | `usb_sony_ext_open`, `usb_sony_ext_ioctl`, `hub_ioctl`, `hub_probe`, `usb_open` |
| `usbg_buspower.ko` | 43 | `usbg_buspower_core_write`, `usbg_buspower_core_ioctl`, `usbg_buspower_core_open` |
| `usbg_cmn.ko` | 10 |  |
| `usbg_sen.ko` | 57 | `fops_te_open`, `fops_se_open`, `fops_ioctl`, `usbg_sen_console_write`, `usbg_ldisc_buf_read` |
| `usbg_stillimage.ko` | 65 | `sicd_event_open`, `sicd_core_open`, `sicd_event_write`, `sicd_data_read`, `sicd_data_ioctl` |
| `usbg_storage.ko` | 222 | `storage_open`, `storage_ioctl`, `bdio_init`, `storage_read`, `storage_write` |


## Декомпиляция ключевых функций (пример)

Для `upm`, `unidrv2`, `liro` слинкованные образы импортированы в Ghidra
с картой символов (`.syms`), функции переименованы, ключевые
`*_init`/`*_exit`/`*_drop`/`*_write` декомпилированы.

Пример — `upm_senser_wbi_drop`:

```c
void upm_senser_wbi_drop(undefined1 *param_1)
{
  uVar1 = func_0xc0042cbc();          // wbi_drop() в ядре
  param_1[0x13] = uVar1 >> 24;
  param_1[1] = 1; *param_1 = 8;
  *(u32*)(param_1+8) = 0; *(u32*)(param_1+0xc) = 4;
  param_1[0x11] = uVar1 >> 8; param_1[0x12] = uVar1 >> 16;
  param_1[0x10] = uVar1;
}
```

Внешний вызов разрешился в **`0xC0042CBC`** — это `wbi_drop` в ядре
(по kallsyms `0xC0042CC4`), то есть линковка работает.

Большинство автоматически выбранных функций — тривиальные
`*_init`/`*_exit`; для содержательного разбора нужен выбор по
назначению (ioctl/probe), а не по суффиксу.
