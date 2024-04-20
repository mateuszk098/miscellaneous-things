# **PODSTAWOWE KOMENDY GITA**

## **KONFIGURACJA NAZW**

**1. Ustawienie nazwy użytkownika dla wszystkich repozytoriów:**

```bash
git config --global user.name <USER>
```

**2. Ustawienie emaila dla wszystkich repozytoriów:**

```bash
git config --global user.email <EMAIL>
```

**3. Ustawienie nazwy użytkownika dla konkretnego repozytorium:**

```bash
git config --local user.name <USER>
```

**4. Wyświetlenie wszystkich ustawień:**

```bash
git config --global --list           
```

**5. Konfiguracja aliasu (skrótu polecenia do wykonania):**

```bash
git config --global alias.history "log --graph --oneline --all"
```

**6. Usunięcie aliasu (skrótu polecenia do wykonania):**

```bash
git config --global --unset alias.history
```

**7. Wykonanie aliasu:**

```bash
git history
```

**8. Wykonanie aliasu i przekazanie wyniku do pliku:**

```bash
git history > history.txt
```

## **PRACA Z REPOZYTORIUM**

**1. Tworzenie nowego repozytorium:**

```bash
git init
```

**2. Status - informacje na temat obecnej gałęzi, commity w local repository oraz stan staging area. Polecenie to nie mówi jednak jakie zmiany są w working tree:**

```bash
git status
```

**3. Dodanie określonego pliku do staging area:**

```bash
git add <FILE>
```

**4. Dodanie wszystkich plików z rozszerzeniem .txt:**

```bash
git add <*.txt>
```

**5. Dodanie wszystkich plików zaczynających się na abc (wielkość liter ma znaczenie):**

```bash
git add <abc_*>
```

**6. Usuwanie określonego pliku ze staging area:**

```bash
git restore --staged <FILE>
```
  
**7. Usuwanie wszystkich plików z rozszerzeniem .txt:**

```bash
git restore --staged <*.txt>
```

**8. Usuwanie wszystkich plików zaczynających się na abc:**

```bash
git restore --staged <abc_*>
```

## **COMMITY**

**1. Dodanie commitu do repozytorium lokalnego:**

```bash
git commit -m <MESSAGE>
```

**2. Informacje na temat najnowszego commitu:**

```bash
git show         
```

**3. Informacje na temat danego commitu np. d122a6a:**

```bash
git show <COMMIT>
```

**4. Historia commitów:**

```bash
git log
```

**5. Historia commitów w postaci grafu:**

```bash
git log --graph       
```

**6. Historia commitów w postaci grafu bez dodatkowych informacji:**

```bash
git log --graph --oneline**
```

**7. Historia commitów w postaci grafu we wszystkich gałęziach bez dodatkowych informacji:**

```bash
git log --graph --oneline --all**
```

**8. Historia commitów nawet tych usuniętych ale jedynie przez krótki czas:**

```bash
git reflog    
```

## **RÓŻNICE**

**1. Różnice między plikami w working tree oraz staging area:**

```bash
git diff
```

**2. Różnice między plikami w staging area oraz local repository:**

```bash
git diff --staged
```

**3. Różnice między plikami w working tree oraz commitem w local repository:**

```bash
git diff <COMMIT>>
```

**4. Różnice między plikami w working tree oraz najnowszym commitem w local repository:**

```bash
git diff HEAD
```

**5. Odrzucenie zmian:**

```bash
git restore <FILE>
```

**6. Wycofywanie zmian ze staging area:**

```bash
git reset <FILE>
```

**7. Przywracanie pliku do stanu w jakim był w ostatnim commicie:**

```bash
git checkout HEAD <FILE>
```

## **DODAWANIE ŁAT**

**Rozbijanie zmiany na kilka commitów. Prośba o wybranie danej opcji, najczęściej wybieramy e czyli edit, wtedy możemy edytować dany plik i usunąć z niego zmiany, których nie chcemy w danym commicie. Zapisujemy i mamy gotowy plik do commitu. Następnie dodajemy commit i mamy plik w working area z pozostałą zmianą, którą możemy dodać w nowym commicie.**

**1. Rozbijanie commitu na kilka commitów:**

```bash
git add --patch <FILE>>
```

## **CZYM JEST HEAD**

**HEAD to unikalny wskaźnik w projekcie, jest on tylko jeden i nie można zmienić jego nazwy. Wskaźnik ten może pokazywać na gałąź (branch) lub bezpośrednio na rewizję (commit). Wyznacza on położenie w projekcie, tzn. gdzie aktualnie się znajdujemy. Sytuacja w której HEAD pokazuje na gałąź jest sytuacją normalną. Z kolei jeśli HEAD pokazuje bezpośrednio na commit to jest to sytacja wyjątkowa. Wtedy mamy "detached HEAD". Jeżeli HEAD pokazuje na brancha np. master to wykonując commit, zarówno HEAD jak i master przesuną się na ten commit. Natomiast jeśli startujemy w punkcie kiedy mamy "detached HEAD" i wykonamy commit to przesuniemy HEAD na ten commit ale master pozostanie tam gdzie był. Taka sytuacja jest niebezpieczna, ponieważ zmieniając w tym momencie commit, przesuwamy HEAD a więc pozostawiamy przed chwilą wykonany commit jako sierotę (nic na niego nie pokazuje).**

## **BRANCHE I COMMITY**

**1. Stworzenie nowego brancha o danej nazwie:**

```bash
git branch <BRANCH>
```

**2. Przełączenie się na dany branch (HEAD będzie wskazywał na ten branch):**

```bash
git checkout <BRANCH>
```

**3. Stworzenie nowego brancha i przeskok na niego:**

```bash
git checkout -b <BRANCH>
```

**4. Stworzenie nowego brancha 2 commity przed branchem master:**

```bash
git checkout -b <BRANCH>  master~2
```

**5. Zmiana nazwy lokalnego (na którym się znajdujemy) brancha:**

```bash
git branch -m <BRANCH>
```

**6. Skok na dany commit, spowoduje to odłączenie wskaźnika HEAD od brancha:**

```bash
git checkout <COMMIT>
```

**7. Skok na dany commit na siłę (usunięcie aktualnie wprowadzonych zmian):**

```bash
git checkout --force <COMMIT>
```

**8. Skok dwa commity w tył względem HEAD:**

```bash
git checkout HEAD~2
```

**9. Skok jeden commit w tył względem HEAD:**

```bash
git checkout HEAD~
```

**Nie można jednak skakać do przodu bo commity mają indentyfikatory dla swoich rodziców a nie dzieci. To powoduje, że wskazują one zawsze na commit poprzedni. Możemy za to przeskoczyć na branch, który wskazuje na czubek, czyli najnowszy commit. Z perspektywy gita branch to tylko i wyłącznie wskaźnik na commit. Dlatego jest on bardzo lekki.**

**10. Wyświetlenie branchy w projekcie:**

```bash
git branch --list      
```

**11. Wyświetlenie branchy zaczynających się na feat:**

```bash
git branch --list feat*
```

**12. Wyświetlenie branchy domergowanych do master:**

```bash
git branch --merged master
```

**13. Wyświetlenie branchy, które nie są domergowane do master:**

```bash
git branch --no-merged master
```

**14. Wyświetlenie wszystkich branchy, zarówno zdalnych jak i lokalnych:**

```bash
git branch -a
```

**15. Wyświetlenie wszystkich branchy (zdalnych i lokalnych) ze wszystkimi informacjami:**

```bash
git branch -lavv
```

**16. Usuwanie brancha:**

```bash
git branch -d <BRANCH>
```

**17. Usunięcie brancha na siłę, nawet jeśli nie jest domergowany:**

```bash
git branch -D <BRANCH>
```

## **PLIKI NIEŚLEDZONE**

**1. Usunięcie plików nieśledzonych (checkout ich nie usuwa). Flaga n oznacza na niby (pokaże co się stanie jeśli to wykonasz), d - weź pod uwagę katalogi:**

```bash
git clean -nd
```

**2. Usunięcie plików nieśledzonych (f od force):**

```bash
git clean -fd      
```

## **MERGOWANIE ZMIAN:**

**1. Mergowanie zmian z brancha BRANCH do brancha na którym się znajdujemy:**

```bash
git merge <BRANCH>
```

**2. Mergowanie zmian typu no-fast-forward, czyli stworzy się nowy commit:**

```bash
git merge --no-ff <BRANCH>
```

**3. Przerwanie mergowania w stanie np. (master|MERGING):**

```bash
git merge --abort
```

**4. Kontynuwanie mergowania (po rozwiązaniu konfliktu i dodaniu zmiany do staging area):**

```bash
git merge --continue  
```

## **RESETOWANIE I ODWRACANIE ZMIAN**

**1. Usunięcie konkretnego pliku ze staging area:**

```bash
git reset <FILE>
```

**2. Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit. Polecenie działa podobnie jak git checkout ale git checkout przesuwa tylko wskaźnik HEAD:**

```bash
git reset <COMMIT>
```

**3. Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit.Propaguje zmiany do working tree i staging area, zastąpi wszystkie zmiany na te,które przychodzą z danego commita. Podobne do git checkout ale git checkout będzie próbował je dopisać:**

```bash
git reset --hard <COMMIT>
```

**4. Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit. Propaguje zmiany do staging area (jest to wariant domyślny):**

```bash
git reset --mixed <COMMIT>
```

**5. Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit. Nie propaguje zmian:**

```bash
git reset --soft <COMMIT>
```

**6. Wprowadzenie zmiany dokładnie przeciwnej jaka została wprowadzona w COMMIT. Tej komendy używamy gdy nie jesteśmy pewni czy ktoś nie pobierze danej gałęzi, ponieważ git reset spowoduje rozjechanie wszystkich zmian np. u kogoś kto pracował na danej gałęzi. Git revert może powodować konflikty jeśli wykonamy go na commicie ze środka historii. Polecenie to natychmiast commituje zmiany:**

```bash
git revert <COMMIT>
```

**7. Wprowadzenie zmiany dokładnie przeciwnej jaka została wprowadzona w COMMIT. To polecenie nie commituje zmian. Zmiany trafią do katalogu roboczego i będziemy mogli wykonać commit ręcznie:**

```bash
git revert -n <COMMIT>
```

**8. Odwracanie zmian z poprzednich 2 commitów, commity podajemy w odwrotnej kolejności niż w jakiej zostały one wprowadzone:**

```bash
git revert -n HEAD HEAD~
```

**9. Potwierdzenie rozwiązania konfliktów i dokończenie zmian odwracania commitu:**

```bash
git revert --continue
```

**10. Przerwanie odwracania zmian:**

```bash
git revert --abort
```

## **PRACA ZDALNA**

**1. Klonowanie repozytorium (utworzy folder o nazwie repozytorium):**

```bash
git clone <link_ssh_or_https
```

**2. Informacja na temat zdalnego repozytorium, najczęściej origin:**

```bash
git remote
```

**3. Informacje z jakiego zdalnego repozytorium pobieramy zmiany i do jakiego te zmiany wypychamy:**

```bash
git remote -v
```

**4. Wyświetlenie listy gałęzi zdalnych:**

```bash
git branch -r
```

**5. Usuwanie brancha zdalnego:**

```bash
git branch -d -r <origin/BRANCH
```

```bash
git push -d origin <BRANCH>
```

```bash
git push origin --delete <BRANCH>
```

**6. Wypychanie nowego lokalnego brancha na repozytorium zdalne:**

```bash
git push origin -u <BRANCH>
```

**7. Wypychanie zmian z brancha lokalnego do brancha zdalnego origin:**

```bash
git push origin <BRANCH>
```

**8. Wypychanie zmian z informacją o trackingu, w przyszłości wystarczy robić git push i git będzie wiedział o co chodzi:**

```bash
git push -u origin <BRANCH>
```

**9. Pobieranie zmian z brancha zdalnego origin (wszystkie branche zdalne):**

```bash
git fetch origin
```

**10. Domergowanie do brancha na którym jesteśmy, brancha zdalnego master (po wcześniejszym git fetch):**

```bash
git merge origin/master
```

**11. Stworzenie i przełączenie się na nowego brancha lokalnego, który został pobrany ze zdalnego repozytorium:**

```bash
git checkout -b <LOCAL_BRANCH> <REMOTE_BRANCH>
```

**12. Pobieranie zmian z repozytorium zdalnego. Polecenie git pull jest jednoczesnym poleceniem git fetch oraz git merge to znaczy, że powinniśmy być na odpowiedniej gałęzi kiedy wykonujemy to polecenie. Poniższe polecenie pobierze zmiany ze zdalnego repozytorium origin z gałęzi master i domerguje je do gałęzi na której się znajdujemy:**

```bash
git pull origin master
```

**13. Ustawienie aby git pull działało bezpośrednio tylko kiedy nie ma konfliktów:**

```bash
git config --global pull.ff only
```

**14. Śledzenie gałęzi. Ustawienie trackingu z remote origin na lokalny branch feature/zakupy:**

```bash
git branch -u origin/feature/zakupy feature/zakupy
```

**15. Usuwanie trackingu brancha feature/zakupy:**

```bash
git branch --unset-upstream feature/zakupy
```

**16. Stworzenie nowego lokalnego brancha z istniejącego brancha zdalnego, przełączenie się na niego i trackowanie:**

```bash
git checkout -t origin/feature/zakupy
```

## **POPRAWKI COMMITÓW I ZMIANA BAZY**

**1. Poprawka ostatniego commitu. Uwzględni zmiany w staging area i zastąpi ostatni commit:**

```bash
git commit --amend
```

**2. Poprawka ostatniego commitu. Uwzględni zmiany w staging area i zastąpi ostatni commit. Wersja z poprawieniem wiadomości:**

```bash
git commit --amend -m <MESSAGE>
```

**3. Zmiana bazy. Będąc na gałęzi, której bazę chcemy zmienić wywołujemy git rebase z parametrem, którym jest gałąź, która ma stać się naszą bazą, to polecenie modyfikuje historię brancha, którego bazę zmieniamy:**

```bash
git rebase <BRANCH>
```
