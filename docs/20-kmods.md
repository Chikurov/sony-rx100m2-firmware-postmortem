# Драйверы ядра из initrd

Всего **39** модулей `*.ko` (ELF ARM, символы сохранены).

| Модуль | Размер | Функций | Примеры символов |
|---|---|---|---|
| `accel.ko` | 16536 | 8 | `psm_acc_async_thread`, `accel_res`, `accel_sus` |
| `cdrom.ko` | 37980 | 18 | `cdrom_dummy_generic_packet`, `cdrom_sysctl_handler`, `cdrom_mrw_exit` |
| `cec.ko` | 81504 | 241 | `hdmi_util_timer_cb`, `cec_core_status_entry_wait_hpd_status`, `cec_core_status_entry_wait_update_phy_addr` |
| `compass.ko` | 6552 | 7 | `compass_res`, `compass_sus`, `cmps_api_cb` |
| `dmm.ko` | 169396 | 207 | `dmm_module_ResumeModule`, `dmm_module_SuspendModule`, `dmm_module_ExitModule` |
| `hdmi.ko` | 140492 | 315 | `hdmi_core_safe_release`, `hdmi_core_status_entry_outputting`, `hdmi_core_status_exit_power_off` |
| `htmd.ko` | 5272 | 4 | `htd_disconnect`, `htd_probe`, `cleanup_module` |
| `kikilog.ko` | 36612 | 55 | `kikilog_fops_open`, `kikilog_fops_close`, `kikilog_main_thread` |
| `liro.ko` | 70480 | 191 | `cache_flush_range`, `cache_inv_range`, `prints` |
| `mag.ko` | 14204 | 7 | `mag_res`, `mag_sus`, `mag_api_cb` |
| `mcmn_drv.ko` | 71740 | 125 | `mcmnd_drv_open`, `mcmnd_drv_close`, `mcmnd_resume` |
| `mmc_drv.ko` | 102112 | 341 | `mmc_remove`, `mmc_probe`, `mmc_driver_exit` |
| `ms_drv.ko` | 244776 | 606 | `jet_alw_reject_set`, `get_transfer_rate`, `cnl_core_thread` |
| `msen_drv.ko` | 28568 | 52 | `msen_init`, `msen_driver_resume`, `msen_driver_init` |
| `nfc.ko` | 15816 | 33 | `sio_comm_cb`, `nfc_rsrc_almhdl`, `nfc_rsrc_irq` |
| `sata_drv.ko` | 71496 | 93 | `sata_driver_Open`, `sata_driver_Release`, `sata_driver_Resume` |
| `scsi_mod.ko` | 111924 | 238 | `scsi_sony_ext_release`, `scsi_sony_ext_open`, `scsi_sony_ext_ioctl` |
| `scsi_wait_scan.ko` | 2440 | 2 | `cleanup_module`, `init_module` |
| `sd_mod.ko` | 28812 | 31 | `sd_prepare_flush`, `sd_show_app_tag_own`, `sd_show_protection_type` |
| `sircs.ko` | 11464 | 12 | `sircs_init`, `sircs_exit`, `sircs_utimer_callback` |
| `sr_mod.ko` | 18444 | 30 | `sr_done`, `sr_remove`, `sr_kref_release` |
| `stream.ko` | 4228 | 6 | `stream_exit`, `stream_mmap`, `stream_ioctl` |
| `stream2.ko` | 5016 | 6 | `stream_exit`, `stream_ioctl`, `stream_mmap` |
| `unidrv1.ko` | 153604 | 304 | `fsp_resume`, `fsp_suspend`, `fsp_remove` |
| `unidrv2.ko` | 175548 | 308 | `ulogio_module_resume`, `ulogio_module_suspend`, `ulogio_module_exit` |
| `upm.ko` | 138608 | 262 | `k_upm_apicb_upm_pmcb`, `k_upm_apicb_upm_tsk`, `k_upm_apicb_acv` |
| `usb-storage.ko` | 28048 | 50 | `host_info`, `store_max_sectors`, `show_max_sectors` |
| `usb_buspwr.ko` | 14556 | 18 | `usb_buspwr_fops_open`, `usb_buspwr_fops_close`, `usb_buspwr_procRead` |
| `usb_current.ko` | 5408 | 11 | `usb_current_bind`, `usb_current_unbind`, `usb_current_query_oc` |
| `usb_extcmd.ko` | 15632 | 31 | `disable_inquiry_state`, `extcmd_mem_free`, `clear_bit_req_flag` |
| `usb_max14648.ko` | 43080 | 38 | `usb_max14648_fops_open`, `usb_max14648_fops_close`, `usb_max14648_AlarmHandler` |
| `usb_portMonitor.ko` | 21748 | 20 | `usb_portMonitor_bind`, `usb_portMonitor_unbind`, `usb_portMonitor_fops_open` |
| `usb_shcd.ko` | 31060 | 52 | `scd_host_start`, `scd_host_stop`, `scd_host_shutdown` |
| `usbcore.ko` | 127312 | 267 | `usb_dev_prepare`, `usb_dev_restore`, `usb_dev_thaw` |
| `usbg_buspower.ko` | 15720 | 42 | `core_cb_nop`, `usbg_buspower_core_write_comp`, `usbg_buspower_ep0_comp` |
| `usbg_cmn.ko` | 4604 | 10 | `usbg_cmn_copy_probe_info`, `usbg_cmn_clear_ep_list`, `usbg_cmn_delete` |
| `usbg_sen.ko` | 32872 | 57 | `fops_te_release`, `fops_se_release`, `fops_te_open` |
| `usbg_stillimage.ko` | 24416 | 65 | `core_cb_nop`, `sicd_ep0_comp`, `core_cb_clear_halt` |
| `usbg_storage.ko` | 72404 | 222 | `bdio_end_io`, `storage_release`, `storage_open` |
