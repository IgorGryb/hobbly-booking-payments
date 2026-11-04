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

## Rdzeń biznesowy i standard architektury

**Wizja ze źródła (koncepcja historyczna):** A two-sided activity marketplace joined to organizer scheduling, customer management, booking and payment tools.

**Pierwsze ograniczone zastosowanie:** One organizer segment: verify availability, booking, payment, cancellation and reconciliation under normal and failed transactions.

**Model komercyjny (hipoteza):** Organizer software subscription plus a transaction-fee option; take rate, willingness to pay and two-sided growth are unvalidated.

**Jednostki i czynniki ekonomiczne:** subscription fee hypothesis; fee revenue per completed booking; processor and support cost; refund and dispute loss; customer acquisition and retention; payout timing and working capital.

**Wykonany zakres:** A local Python/SQLite transaction-state prototype using synthetic bookings and unit economics; no payment provider connection.

**Architektura referencyjna (projekt, bez wdrożenia):** Relational transaction records, capacity and booking states, payment-provider interfaces, idempotent callbacks, reconciliation, access control and observability.

**Opcje odroczone:** Live PSP integration, wallet or card issuance, escrow services, white-label embedding and broad marketplace rollout.

| Model | Zastosowanie w tym przypadku |
|---|---|
| Techniczny | Consistent booking/payment states and auditable transaction records. |
| Biznesowy i produktowy | Organizer SaaS and transaction-fee hypothesis inside a staged two-sided marketplace. |
| Operacyjny | Organizer, customer support and payment partner own booking and exception handoffs. |
| Finansowy | Contribution per completed booking after processor, refund, dispute and support costs. |
| Ryzyko i governance | Test duplicate callbacks, timeouts, mismatches and payment/legal boundaries. |

**Źródła rozwoju:** University of Pennsylvania (Wharton) — Fintech: Foundations & Applications of Financial Technology (`recorded_completed`); IBM — IBM Systems Analyst (`recorded_completed`); IBM — IBM AI Product Manager (`recorded_completed`); Stanford Online — Product Marketing & Go-to-Market Strategy (`recorded_completed`); University of Pennsylvania (Wharton) — Business and Financial Modeling (`recorded_completed`). Są to odnotowane ukończenia programów i kandydackie połączenia zastosowań; nie stanowią samodzielnego dowodu wdrożenia lub biegłości. **Metody z zapisanym zakresem odczytu:** `M-SIPOC`, `M-RACI`, `M-MOSCOW`, `M-FURPS`, `M-FEASIBILITY`, `M-SCENARIO`, `M-MEASURE`.

## Granice i źródła

Nie deklarować live PSP, produkcyjnej współbieżności, zgodności regulacyjnej ani
wyniku komercyjnego. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[validation memo](MODEL-VALIDATION-MEMO.md), [model card](MODEL-CARD.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
