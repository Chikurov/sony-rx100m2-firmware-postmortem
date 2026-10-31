# DSP: инвентарь сигнатур

Из `av-cam.bin` извлечено **256** уникальных отладочных сигнатур функций.

Распределение по подсистемам: Capture (86), HAPI (49), FC (37), YC (33), SaFuncDrv (31), Function (18), CaptureManager (1), Sync (1)

## Camera::HAPI (примеры)

- `Camera::HAPI::Apollo4_Addition_NR_Init`
- `Camera::HAPI::Apollo4_Addition_NR_Main`
- `Camera::HAPI::CheckDMMforClone`
- `Camera::HAPI::CheckMemory`
- `Camera::HAPI::ContrastPlus_Main`
- `Camera::HAPI::End_ArtEffect_Sequence`
- `Camera::HAPI::End_HDR_Sequence`
- `Camera::HAPI::End_RichtoneMono_Sequence`
- `Camera::HAPI::FaceMiniImageAndDetect`
- `Camera::HAPI::Face_Nr_Main`
- `Camera::HAPI::HapiCONTP`
- `Camera::HAPI::HapiKKNR`
- `Camera::HAPI::HapiMiniImageContrastPlus`
- `Camera::HAPI::HapiSFTFCS`
- `Camera::HAPI::HapiTBOX`
- `Camera::HAPI::Image_Clone`
- `Camera::HAPI::Image_Destruct`
- `Camera::HAPI::LoadBinary`
- `Camera::HAPI::LoadDictionary`
- `Camera::HAPI::MakeMappingParam`
- `Camera::HAPI::Miniature_Main`
- `Camera::HAPI::SPICA_Main`
- `Camera::HAPI::SetSpecialSequence`
- `Camera::HAPI::ShareDMMforClone`
- `Camera::HAPI::SoftFocus_Main`

Полный список: `data/dsp_signatures.txt`.
