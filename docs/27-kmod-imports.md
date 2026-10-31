# Модули ядра: внешние зависимости

Всего модулей: **39**, уникальных импортируемых символов: **629**.

| Модуль | Импортов | Топ-5 символов |
|---|---|---|
| `accel.ko` | 74 | `osal_free_msg`×14, `memset`×7, `osal_snd_sync_direct`×7, `osal_snd_msg`×7, `memcpy`×6 |
| `cdrom.ko` | 235 | `printk`×101, `__memzero`×25, `__copy_from_user`×15, `__copy_to_user`×11, `kfree`×8 |
| `cec.ko` | 560 | `rt_spin_unlock`×53, `rt_spin_lock`×49, `memset`×39, `snprintf`×38, `osal_snd_sync_direct`×37 |
| `compass.ko` | 42 | `osal_free_msg`×7, `osal_valloc_msg_wait`×4, `osal_snd_sync_msg`×4, `memset`×4, `osal_snd_sync_direct`×4 |
| `dmm.ko` | 417 | `scnprintf`×89, `memcpy`×72, `__memzero`×36, `memset`×20, `__aeabi_unwind_cpp_pr0`×20 |
| `hdmi.ko` | 948 | `snprintf`×183, `rt_spin_unlock`×78, `rt_spin_lock`×73, `memset`×41, `memcpy`×36 |
| `htmd.ko` | 21 | `usb_control_msg`×6, `printk`×4, `__aeabi_unwind_cpp_pr0`×3, `usb_get_dev`×1, `usb_put_dev`×1 |
| `kikilog.ko` | 219 | `scnprintf`×29, `memset`×15, `kfree`×12, `memcpy`×10, `__aeabi_unwind_cpp_pr0`×10 |
| `liro.ko` | 408 | `printk`×80, `__aeabi_unwind_cpp_pr0`×33, `wake_up_process`×28, `boot_time_add`×24, `memcpy`×18 |
| `mag.ko` | 64 | `osal_free_msg`×10, `memset`×8, `osal_snd_sync_direct`×8, `osal_snd_msg`×7, `osal_valloc_msg_wait`×6 |
| `mcmn_drv.ko` | 374 | `memcpy`×84, `printk`×36, `Backup_read_4Byte`×20, `__memzero`×18, `memset`×18 |
| `mmc_drv.ko` | 391 | `__memzero`×39, `kfree`×31, `memcpy`×30, `kmem_cache_alloc`×16, `kmalloc_add_trace`×16 |
| `ms_drv.ko` | 1656 | `printk`×1022, `__aeabi_uidivmod`×73, `memset`×45, `__memzero`×43, `__copy_to_user`×34 |
| `msen_drv.ko` | 199 | `printk`×42, `__memzero`×17, `osal_free_msg`×14, `osal_valloc_msg_wait`×10, `memset`×10 |
| `nfc.ko` | 171 | `Backup_read_4Byte`×61, `memset`×17, `osal_snd_sync_direct`×16, `osal_free_msg`×8, `__aeabi_unwind_cpp_pr0`×7 |
| `sata_drv.ko` | 369 | `printk`×115, `__memzero`×37, `memcpy`×16, `kfree`×16, `mcmnd_api_setmediapower`×13 |
| `scsi_mod.ko` | 888 | `printk`×99, `rt_spin_unlock`×58, `rt_spin_lock`×55, `snprintf`×35, `put_device`×29 |
| `scsi_wait_scan.ko` | 3 | `__aeabi_unwind_cpp_pr0`×2, `scsi_complete_async_scans`×1 |
| `sd_mod.ko` | 300 | `dev_driver_string`×83, `printk`×72, `__memzero`×8, `scsi_mode_sense`×7, `snprintf`×6 |
| `sircs.ko` | 101 | `memset`×11, `osal_snd_sync_direct`×11, `printk`×11, `osal_unreg_msg_queue_cb`×5, `rt_spin_lock`×4 |
| `sr_mod.ko` | 164 | `printk`×17, `__memzero`×15, `kfree`×12, `kmem_cache_alloc`×10, `kmalloc_add_trace`×10 |
| `stream.ko` | 10 | `__aeabi_unwind_cpp_pr0`×3, `remap_pfn_range`×1, `__copy_to_user`×1, `udif_cdev_unregister`×1, `udif_driver_unregister`×1 |
| `stream2.ko` | 17 | `_mutex_unlock`×4, `__aeabi_unwind_cpp_pr0`×3, `printk`×2, `_mutex_lock`×2, `remap_pfn_range`×1 |
| `unidrv1.ko` | 978 | `printk`×179, `__memzero`×48, `__aeabi_unwind_cpp_pr0`×45, `_mutex_unlock`×43, `kfree`×43 |
| `unidrv2.ko` | 1220 | `printk`×213, `memcpy`×80, `scnprintf`×63, `__aeabi_unwind_cpp_pr0`×62, `snprintf`×46 |
| `upm.ko` | 1505 | `osal_wai_sem_tmo`×346, `osal_sig_sem`×330, `osal_valloc_msg_wait`×136, `osal_free_msg`×134, `osal_snd_msg`×87 |
| `usb-storage.ko` | 228 | `strcpy`×18, `printk`×13, `rt_spin_unlock`×9, `memcpy`×9, `__aeabi_unwind_cpp_pr0`×9 |
| `usb_buspwr.ko` | 82 | `scnprintf`×20, `osal_valloc_msg_wait`×3, `usb_buspw_ic_set_usb_suspend_mode`×3, `osal_unreg_msg_queue_cb`×3, `__aeabi_unwind_cpp_pr0`×3 |
| `usb_current.ko` | 13 | `__aeabi_unwind_cpp_pr0`×3, `_mutex_lock`×1, `_mutex_unlock`×1, `udif_cdev_unregister`×1, `usb_otgcore_unregister_driver`×1 |
| `usb_extcmd.ko` | 149 | `printk`×37, `_mutex_unlock`×22, `_mutex_lock`×20, `_clear_bit_le`×9, `_set_bit_le`×8 |
| `usb_max14648.ko` | 264 | `printk`×77, `scnprintf`×74, `Backup_read_4Byte`×24, `memset`×9, `osal_snd_sync_direct`×9 |
| `usb_portMonitor.ko` | 108 | `osal_valloc_msg_wait`×13, `osal_free_msg`×11, `Backup_read_4Byte`×9, `osal_snd_sync_msg`×8, `scnprintf`×7 |
| `usb_shcd.ko` | 112 | `kfree`×16, `rt_spin_unlock`×9, `rt_spin_lock`×7, `dma_free_coherent`×6, `__aeabi_unwind_cpp_pr0`×6 |
| `usbcore.ko` | 1208 | `printk`×172, `dev_driver_string`×153, `kfree`×70, `rt_spin_unlock`×69, `rt_spin_lock`×61 |
| `usbg_buspower.ko` | 116 | `_mutex_unlock`×15, `osal_valloc_msg_wait`×8, `_mutex_lock`×8, `kfree`×8, `__memzero`×8 |
| `usbg_cmn.ko` | 39 | `kfree`×5, `__memzero`×4, `osal_dynamic_id`×4, `__kmalloc`×3, `__copy_from_user`×3 |
| `usbg_sen.ko` | 375 | `printk`×31, `_mutex_unlock`×25, `_mutex_lock`×23, `_set_bit_le`×22, `_clear_bit_le`×22 |
| `usbg_stillimage.ko` | 196 | `_mutex_unlock`×49, `printk`×39, `_mutex_lock`×26, `__memzero`×11, `kfree`×8 |
| `usbg_storage.ko` | 390 | `kfree`×84, `__memzero`×39, `rt_spin_unlock`×30, `rt_spin_lock`×25, `kmem_cache_alloc`×23 |
