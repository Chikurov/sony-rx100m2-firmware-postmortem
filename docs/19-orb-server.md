# `orb-server`: Camera Remote API (наблюдения)

`/usr/bin/orb-server` (1,6 МБ) — HTTP/JSON-сервер управления камерой.

## ФАКТЫ (строки)

- формат запроса: `{"method":"…","params":[…]}`;
- заголовок `Content-Type: application/json`;
- методы (суффикс `_invoke_cmd`):

```
ActTakePicture ActZoom GetApplicationInfo GetAvailableApiList
GetAvailableFlashMode GetAvailableMovieQuality GetAvailableSelfTimer
GetAvailableShootMode GetAvailableSteadyMode GetAvailableViewAngle
GetFlashMode GetMethodTypes GetMovieQuality GetSelfTimer GetShootMode
GetSteadyMode GetSupportedFlashMode GetSupportedMovieQuality
GetSupportedSelfTimer GetSupportedShootMode GetSupportedSteadyMode
GetSupportedViewAngle GetVersions GetViewAngle ReceiveEvent
SetFlashMode SetMovieQuality SetSelfTimer SetShootMode SetSteadyMode
SetViewAngle StartIntervalStillRec StartLiveview StartMovieRec
StopIntervalStillRec StopLiveview StopMovieRec
```

Это набор методов **Sony Camera Remote API** (Wi-Fi/HTTP JSON-RPC):
съёмка, зум, режимы, liveview, интервальная съёмка, события.

## ПРЕДПОЛОЖЕНИЕ

- Эндпоинт вида `/sony/camera` (строка в бинарнике не найдена —
  собирается из частей).
- Транспорт — `libmpr`/`libNetCommon`.

## Ограничения

Порты, SSDP-обнаружение и точные URL не подтверждены: строк нет.
