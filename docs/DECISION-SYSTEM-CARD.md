# Hobbly — karta systemu decyzyjnego

ID: `PXP-PRJ-HOBBLY`  
Status: prywatne studium vertical slice z danymi syntetycznymi/testowymi; nie usługa płatnicza ani deklaracja zgodności regulacyjnej.

## Znaczenie dla decyzji

Hobbly sprawdza, czy obietnica usługi rezerwacyjnej pozostaje operacyjnie i
ekonomicznie spójna po uwzględnieniu stanów płatności, wyjątków, zwrotów,
reconciliation i kosztu obsługi. Główny wektor: model biznesowy, produkt i
operacje; wzmacniające: kapitał/ryzyko oraz dane/dowód.

## Mapa systemu

`listing → slot → booking state → payment state → wyjątek/refund →
reconciliation i support → contribution logic → decyzja produktowa`.

## Dowód i wkład

Pakiet dokumentuje role, model stanów, idempotency, obsługę błędów, ekonomię i
scenariusze negatywne. Wkład polega na powiązaniu wymagań produktu z kosztami
wyjątków; nie potwierdza wolumenu rynku, PSP ani działania na danych klientów.

## Model i hipoteza integracji

Mechanizm wiąże customer promise, integrity stanów transakcji i unit economics.
Hipoteza: model obejmujący pełne exception costs może ujawnić, czy happy-path
pricing pozornie zawyża trwałość usługi. Porównanie obejmuje wspólne koszty,
awarie callbacków i przypadki anulowania.

## Test i następna opcja

Najtańszy test porównuje happy-path pricing z pełnym modelem kosztów wyjątków
przy duplicate callback, cancellation i booking/payment mismatch. Następny krok
to ograniczony segment dopiero po doprecyzowaniu support burden i partnera
płatniczego.

## Granice i źródła

Nie deklarować live PSP, produkcyjnej współbieżności, zgodności regulacyjnej ani
wyniku komercyjnego. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[validation memo](MODEL-VALIDATION-MEMO.md), [model card](MODEL-CARD.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
