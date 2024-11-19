# Transmisja w systemie FEC (Forward Error Correction)
## Spis Treści
- [Wprowadzenie](#wprowadzenie)
- [Teoria](#teoria)
  - [Kanały](#kanały)
    - [BSC](#kanał-bsc)
    - [Gilberta-Elliotta](#kanał-gilberta-elliotta)
  - [Kody korekcyjne](#kody-korekcyjne)
    - [Kod Hamminga](#kod-hamminga)
    - [ReedSolomon](#reedsolomon)
- [Przegląd Plików](#przegląd-plików)
  - [b2b](#b2b)
  - [binary](#binary)
  - [BSCchannel](#bscchannel)
  - [GEchannel](#gechannel)
  - [generator](#generator)
  - [HammingFunction](#hammingfunction)
- [Biblioteki](#biblioteki)


---
## Wprowadzenie
Niezawodność i diagnostyka – projekt
- Zadanie polega na implementacji 
  - kanału komunikacyjnego modele 
    - **BSC**
    - **Gilberta-Elliotta**
  - systemu transmisji **FEC** z kodami korekcyjnymi 
    - **RS**
    - **Kod Hamminga**
- Symulacyjne badanie skuteczności transmisji dla parametrów 
  - **BER**
  - błędy niezależne
---
## Teoria

### Kanały

- #### BSC

  - wejście oraz wyjście z tego kanału zapisuje się za pomocą alfabetu *X* = *Y* = {0,1}
  - parametr `p` = [0,1] symbolizuje prawdopodobieństwo że bit na wyjściu będzie zamieniony

- #### Gilberta-Elliotta

### Kody korekcyjne

#### Kod Hamminga
- ##### właściwości
  - Potrafi wykrywać i naprawiać 1 błąd w zakodowanym ciągu
  - Kod Hamminga przyjmuje parametr `μ` odpowiadający za wygląd kodu
  - aby kod zadziałał `μ` >= 3
  - *redundancy*: `m` = `μ` informuje program na ilu bitach ma zostać zakodowana wiadomość
  - *Dimension*: `k` = 2^μ -1 -μ jest to parametr odpowiadający za długość wiadomości w bitach
  - *Length*: `n` = 2^μ -1 czyli całkowita długość zakodowanej wiadomości
- ##### Działanie kodu Hamminga
##### Kodowanie
  - podczas kodowania kod najpierw tworzy listę o długości `n` i numeruję ją od 1 do `n`+1 numery będącę potęgą 2 zostają zarezerwowane dla bitów korekcyjnych reszta pozycji jest wypełniona bitami informacji numery pozycji są zamieniane na ich binarną reprezentację, każdy bit korekcyjny sprawdza czy na miejscach w których binarna reprezentacja liczby ma 1 na tej samej pozycji na której ma bit korekcyjny i sprawdza czy liczba jedynek na tych miejscach jest parzysta czy nieparzysta 0/1\
##### Dekodowanie
  - podczas dekodowania kod sprawdza każdy numer pozycji z jedynką wykonując na ich binarnych reprezentacjach operację XOR po wykonaniu tej operacji ze wszystkimi numerami pozycji powinno wyjść 0 jeżeli zamiast zera wyszedł jakiś numer pozycji to znaczy że na tym numerze pozycji jest błąd i bit który tam się znajduję musi być zamieniony

#### ReedSolomon



---
## Przegląd Plików

### b2b
- bytearray_to_bits(`byte_array`) funkcja przyjmuje argument `byte_array` który jest listą bajtów i zamienia ją na listę bitów
- bits_to_bytearray(`bits`) funkcja przyjmuje argument `bits`który jest listą bitów i zamienia ją na listę bajtów

### binary
- binaryToBinaryList(`string`,`howLong`) funkcja przyjmuje `string` czyli wyraz zapisany za pomocą 1 lub 0 i zamienia go na listy o długości podstawowo `howLong` = 8, argumentem zwrotnym tej funkcji jest tablica 2d z tablicami o odpowiedniej długości, gdy `string`%`howLong`!= 0 wypełnia pozostałe miejsca 0
- binaryListToBinary(`list`) funkcja jest przeciwieństwem funkcji *binaryToBinaryList(`string`,`howLong`)*
- d2StrListTod2intList(`stringList`) funkcja przyjmuje `stringList`czyli argument który jest listą 2d złożoną z innych list złożonych z 0 1 zapisanych jako słowa, zwraca taką samą listę ale argumenty 0 1 są zapisane jako liczby całkowite
- intListToStrList(`intList`) funkcja przyjmuje `intList` czyli listę z 0 1 zapisanymi jako liczby całkowite i zwraca taką samą listę w której 0 1 są zapisane jako słowa

### BSCchannel


### GEchannel


### generator


### HammingFunction
- HammingFunction(`byte_array`,`redundancy`) funkcja przyjmuje `byte_array` czyli listę bajtów oraz argument `redundancy` czyli liczbę całkowitą, funkcja zwraca tablicę 2d w której są zakodowane bity z tablicy bajtów za pomocą tylu bitów ile jest zapisane w `redundancy` oraz o odpowiedniej długości także wynikającej z tego parametru

---
## Biblioteki
- komm
- reedsolo