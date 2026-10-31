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

## Внутренняя структура (ФАКТ: символы не удалены)

Символов функций: **5 265**. Видны классы:

- `WebApiAddonUipc` — IPC-клиент: `sendMsgToServer`, `recvMsg`,
  `setEvtParamId`, `finalizeClient`;
- `WebApiAddonUtils` — преобразование ID: `convIdToString`,
  `convStringToId`, `convIdToInteger`, таблицы
  `getParamConvIdStringTbl`, `getParamConvIdIntegerTbl`,
  `getMethodParameterResultTypes`, `getParamTypeRangeForReceiveEvent`.

То есть `orb-server` — это **аддон WebApi**, который по IPC общается с
сервером и конвертирует строковые ID методов/параметров в целые по
таблицам.

JSON-поля: `result`, `error`, `statusCode`, `jsonizer`.

## Ограничения

Порты, SSDP-обнаружение и точные URL не подтверждены: строк нет.
