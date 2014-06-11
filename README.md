SIG
===
Wymogi
------
* **moduł "Towary"**  
  lista towarów z możliwością dodawania, edycji i usuwania rekordów (lista pól jest dowolna)
* **moduł "Kontrahenci"**  
  lista kontrahentów z możliwością dodawania, edycji i usuwania rekordów (lista pól jest dowolna)
* **moduł "Dokumenty handlowe"**  
  możliwość wystawiania dokumentów: sprzedaży i zakupu.  
  **Funkcjonalność**  
  lista dokumentów handlowych z możliwością dodawania, edycji i usuwania rekordów.  
  **Obowiązkowe**  
  kontrahent odbiorca (faktura sprzedaży), kontrahent dostawca (faktura zakupu), lista towarów sprzedawanych (kupowanych). Pozycja towaru na fakturze powinna zawierać: kod towaru, nazwę towaru, ilość towaru na pozycji, cenę jednostkową po której sprzedajemy (lub kupujemy), jeżeli kontrahent ma przypisaną cenę z cennika, automatycznie cena towaru jest pobierana na pozycję. Wyliczamy na pozycji: wartość netto (cena jednostkowa * ilość), wartość vat (wartość podatku 23% z wartości netto), wartość brutto (wartość netto + wartość vat). Nagłówek dokumentu zawiera: datę sprzedaży, datę transakcji, formę płatności, datę płatności. Podsumowanie: wartość netto (suma pozycji wartości netto), wartość vat (suma pozycji wartość vat), wartość brutto (suma pozycji wartość brutto).
* Dodatkowe funkcjonalności w systemie mogą poprawić jego ocenę

TODO
----

* Ładne wyświetlanie towarów w article_list (tabelka)
* Uzależnienie wyświetlania od typu użytkownika (gość/niezalogowany, klient, pracownik) - Zrobić faktury jak będą skończone, i zrobić index jako view, bo bez tego nie można przekazać parametru isWorker
  * Gość - widzi tylko dostępne towary, reszta jest niewidoczna
  * Klient - widzi dostępne towary z możliwością "dodania do koszyka", czyli złożenia zamówienia, czyli zrobienia faktury z tymi towarami.
kontahentów niech nie widzi, a faktury na pewno niech widzi własne
  * Pracownik -  natomiast widzi wszystko
* Kontrahenci
* Dokończyć faktury
  * Automatyczne przeliczanie
  * Wyświetlanie w zależności od uprawnień użytkownika
  * w ArticleGatherer na pewno jeszcze musi być foreignkey do Invoice
   https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
* Posprzątać wyświetlanie parametru info na stronach (usunąć z html albo z views)
