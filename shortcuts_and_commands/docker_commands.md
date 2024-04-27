# **PODSTAWOWE KOMENDY DOCKERA**

## **OBRAZY**

**1. Szukanie obrazów Dockera:**

```bash
docker search <IMAGE>
```

**2. Wyświetlenie obrazów dostępnych na obecnej maszynie:**

```bash
docker image ls
```

**3. Pobranie obrazu z Docker Hub:**

```bash
# Jeśli nie podamy tagu, to Docker automatycznie pobierze obraz
# z tagiem `latest`.

docker pull <IMAGE>:<TAG>
```

**4. Usuwanie pobranego obrazu:**

```bash
docker image rm <IMAGE>:<TAG>
docker rmi <IMAGE>:<TAG>
```

**5. Wyświetlanie informacji nt. obrazu - inspekcja obrazu:**

```bash
docker inspect <IMAGE>:<TAG>
```

**6. Wyświetlanie historii obrazu:**

```bash
docker history <IMAGE>:<TAG>
```

## **URUCHAMIANIE KONTENERÓW**

**1. Uruchamianie kontenera:**

```bash
# Jeżeli obraz nie jest pobrany to Docker automatycznie zacznie jego
# pobieranie. Ponadto, jeśli nie podamy tagu to zostanie wybrany 
# automatyczny tag czyli `latest`.

docker run [OPTIONS] <IMAGE>:<TAG> [COMMAND]

OPTIONS:
  -i, --interactive        # Tryb interaktywny, możliwość wysyłania/odbierania informacji.
  -t, --tty                # Emulowanie terminala.
  -d, --detach             # Uruchomienie kontenera jako procesu w tle.
  -e, --env <KEY>=<VALUE>  # Ustawienie zmiennej środowiskowej.
  -m, --memory <BYTES>     # Limit zużywanej pamięci RAM.
  --name <NAME>            # Nadanie nazwy kontenerowi. 
  --cpus <DECIMAL>         # Limit użycia CPU w % (np. 0.2 oznacza maks. 20%).

COMMAND:    # Kontener działa dopóki polecenie jest aktywne. Przykłady poleceń.
  bash      # Uruchomienie terminala.
  ./hello   # Uruchomienie skryptu o nazwie `hello`.
            # Odłączenie się od polecenia (kontener nadal będzie aktywny): CTRL + P, Q
```

**2. Wyświetlanie kontenerów:**

```bash
docker ps [OPTIONS]
docker container ls [OPTIONS]

OPTIONS:
  -a, --all     # Pokaż wszystkie kontenery.
  -l, --latest  # Pokaż ostatni utworzony kontener.
```

**3. Wyświetlanie logów kontenera (logów uruchomionego polecenia):**

```bash
docker logs <CONTAINER_ID>|<NAME>
```

**4. Usuwanie kontenera:**

```bash
docker rm [OPTIONS] <CONTAINER_ID>|<NAME>

OPTIONS:
  -f, --force  # Usunięcie kontenera na siłę, nawet jeśli jest uruchomiony.
```

**5. Usuwanie wszystkich zatrzymanych kontenerów:**

```bash
docker container prune
```

**6. Wyświetlanie procesów kontenera:**

```bash
docker top <CONTAINER_ID>|<NAME>
```

**7. Inspekcja kontenera (również takiego który zakończył działanie):**

```bash
docker inspect <CONTAINER_ID>|<NAME>
```

## **ZARZĄDZANIE KONTENEREM**

**1. Uruchomienie zatrzymanego kontenera:**

```bash
docker start <CONTAINER_ID>|<NAME>
```

**2. Zatrzymanie kontenera:**

```bash
docker stop [OPTIONS] <CONTAINER_ID>|<NAME>

OPTIONS:
  -t, --time <INT>  # Czas w sekundach zanim kontener zostanie ubity.
```

**3. Natychmiastowe ubicie kontenera:**

```bash
docker kill <CONTAINER_ID>|<NAME>
```

**4. Podpięcie się pod proces (polecenie) uruchomionego kontenera:**

```bash
docker attach <CONTAINER_ID>|<NAME>
```

**5. Wykonanie polecenia w uruchomionym kontenerze:**

```bash
docker exec [OPTIONS] <CONTAINER_ID>|<NAME> [COMMAND]

OPTIONS:
  -i, --interactive        # Tryb interaktywny.
  -t, --tty                # Emulowanie terminala.
  -d, --detach             # Uruchomienie polecenia w tle.
  -e, --env <KEY>=<VALUE>  # Ustawienie zmiennej środowiskowej.
```

**6. Aktualizowanie kontenera:**

```bash
docker update [OPTIONS] <CONTAINER_ID>|<NAME>

OPTIONS:
  --cpus <DECIMAL>  # Limit użycia CPU w % (np. 0.2 oznacza maks. 20%).
  --memory <BYTES>  # Limit użycia pamięci RAM.
```

## **ZARZĄDZANIE ZASOBAMI**

**1. Wyświetlanie zasobów zużywanych przez kontener na danej maszynie:**

```bash
docker stats [OPTIONS] [<CONTAINER_ID>|<NAME>]

OPTIONS:
  -a, --all  # Pokaż wszystkie kontenery.
```

**2. Czyszczenie pamięci hosta (usuwanie nieużywanych obrazów, kontenerów, etc.):**

```bash
docker system prune [OPTIONS]

OPTIONS:
  -a, --all          # Usuń wszystkie nieużywane zasoby.
  -f, --force        # Nie pytaj o potwierdzenie.
  --filter <FILTER>  # Filtr, np. "until=24h".
```

## **WOLUMENY**

**1. Kopiowanie plików między kontenerem a hostem:**

```bash
docker cp [OPTIONS] <PATH> <CONTAINER_ID>|<NAME>:<PATH>  # Z hosta na kontenera.
docker cp [OPTIONS] <CONTAINER_ID>|<NAME>:<PATH> <PATH>  # Z kontenera na host.

OPTIONS:
  -a, --archive  # Tryb archiwum.
```

**2. Montowanie katalogu w kontenerze:**

```bash
docker run [...] -v <HOST_PATH>:<CONTAINER_PATH> [...]

# Przykład uruchamiania kontenera Ubuntu z zamontowanym katalogiem 'data'.
docker run -it -v /home/mateusz/data:/data ubuntu:22.04 bash
```

**3. Wyświetlanie wolumenów:**

```bash
docker volume ls

# Wolumen to obiekt służący do przechowywania plików i katalogów. Wybrany wolumen
# można podpinać do kilku kontenerów jednocześnie. Wolumen przechowuje informacje 
# nawet wtedy gdy kontener jest nieaktywny (informacje w kontenerach nie są w żaden
# sposób trwałe). Dlatego podpinamy wolumeny w celu utrwalenia danych. Przykładem 
# może być np. kontener działający jako baza danych.
```

**4. Tworzenie wolumenu:**

```bash
docker volume create <VOLUME>
```

**5. Inspekcja wolumenu:**

```bash
docker volume inspect <VOLUME>
```

**6. Usuwanie wolumenu:**

```bash
docker volume rm <VOLUME>
```

**7. Usuwanie nieużywanych wolumenów:**

```bash
docker volume prune [OPTIONS]

OPTIONS:
  -a, --all    # Usuń wszystkie nieużywane wolumeny.
  -f, --force  # Nie pytaj o potwierdzenie.
```

**8. Montowanie wolumenu w kontenerze:**

```bash
docker run [...] -v <VOLUME>:<CONTAINER_PATH> [...]

# Przykład uruchamiania kontenera Ubuntu z zamontowanym wolumenem 'data'.
docker run -it -v data:/data ubuntu:22.04 bash
```

## **SIECI**

**1. Wyświetlanie dostępnych sieci:**

```bash
docker network ls
```

**2. Tworzenie sieci:**

```bash
# Domyślnie utworzona sieć posiada sterownik bridge i zasięg local.
docker network create [OPTIONS] <NETWORK>

OPTIONS:
  --driver <STRING>   # Sterownik sieci, domyślnie bridge.
  --gateway <STRING>  # Adres IPv4 lub IPv6 bramki.
  --subnet <STRING>   # Adres podsieci w formacie CIDR.
```

**3. Podpinanie sieci do kontenera:**

```bash
docker run [...] --net <NETWORK> [...]
```

**4. Podłączenie danego kontenera do wybranej sieci:**

```bash
docker network connect [OPTIONS] <NETWORK> <CONTAINER_ID>|<NAME>

OPTIONS:
  --ip <STRING>  # Adres IPv4.
```

**5. Odłączenie danego kontenera od wybranej sieci:**

```bash
docker network disconnect [OPTIONS] <NETWORK> <CONTAINER_ID>|<NAME>

OPTIONS:
  -f, --force  # Odłączenie sieci na siłę.
```

**6. Przekierowanie portu podczas uruchamiania kontenera:**

```bash
docker run [...] -p <HOST_PORT>:<CONTAINER_PORT> [...]
```

**7. Usuwanie sieci:**

```bash
docker network rm <NETWORK>
```

**8. Usuwanie wszystkich nieużywanych sieci:**

```bash
docker network prune [OPTIONS]

OPTIONS:
  -f, --force  # Nie pytaj o potwierdzenie.
```

## **BUDOWANIE OBRAZÓW**

**1. Tworzenie obrazu z kontenera:**

```bash
docker commit [OPTIONS] <CONTAINER_ID>|<NAME> <REPOSITORY>:<TAG>

OPTIONS:
  -a, --author <STRING>   # Autor.
  -m, --message <STRING>  # Wiadomość.
  -p, --pause             # Zatrzymaj kontener, domyślnie true.
```

**2. Zmiana nazwy obrazu i jego tagu:**

```bash
docker tag <SOURCE_IMAGE>:<TAG> <TARGET_IMAGE>:<TAG>
```

**3. Budowanie obrazu z pliku Dockerfile:**

```bash
docker build [OPTIONS] <CONTEXT_PATH>

OPTIONS:
  -t, --tag <NAME>:<TAG>      # Nazwa i opcjonalny tag obrazu.
  -f, --file <STRING>         # Nazwa Dockerfile, domyślnie Dockerfile.
  -q, --quiet                 # Wycisz output podczas budowania obrazu.
  --build-arg <STRING_ARRAY>  # Zmienne do zbudowania obrazu.
  --no-cache                  # Nie używaj cache budując obraz.
```

**4. Przykładowy Dockerfile:**

```dockerfile
# Definiowanie zmiennej którą można przekazać podczas budowy obrazu.
# Jeśli nie zostanie przekazana wartość dla zmiennej to zostanie
# użyta wartość domyślna.
ARG UBUNTU_VERSION=22.04

# Na podstawie jakiego obrazu ma zostać zbudowany obraz.
FROM ubuntu:${UBUNTU_VERSION}

# Ustawienie ścieżki do katalogu roboczego. Wszystkie komendy będą 
# wykonywane w odniesieniu do tego katalogu. W przypadku jego braku 
# zostanie on utworzony.
WORKDIR /app

# Ustawienie zmiennej środowiskowej. Można stosować pary <KEY> <VALUE>.
# Jednakże zaleca się stosowanie par <KEY>=<VALUE>.
# Można zdefiniować wiele zmiennych środowiskowych.
ENV AUTHOR="John Doe" \ 
    VERSION=1.0

# Kopiowanie pliku z hosta do kontenera. Instrukcja COPY przyjmuje 
# dwa argumenty - lokalizację pliku na hoście oraz lokalizację do 
# jakiej przekopiować plik w kontenerze. Domyślnie COPY szuka plików
# które kopiujemy w lokalizacji w której znajduje się Dockerfile.
COPY script.sh /app/

# Instrukcja ADD działa podobnie jak COPY, ale dodatkowo pozwala na
# pobieranie plików z adresu URL. W przypadku ADD można stosować
# adresy URL, pliki z archiwami oraz pliki z adresami URL.
# Instrukcja ADD automatycznie rozpakowuje archiwa w kontenerze.
# Instrukcja ADD jest bardziej obciążająca dla systemu niż COPY.
ADD https://github.com/mateuszk098/argon-molecular-dynamics.git /app/core/

# Wykonanie komendy w kontenerze. Można stosować wiele komend.
# Flaga -y oznacza automatyczne potwierdzanie instalacji.
RUN apt-get update && apt-get install -y curl

# Instrukcja VOLUME służy do definiowania ścieżki w obrazie, która będzie
# wymagała podpiętego wolumenu. Przyjmuje jeden argument w postaci ścieżki
# do której będziemy podpinać wolumen. Instrukcja wymusza aby wolumen istniał
# podczas uruchamiania kontenera. Jeżeli takowy nie istnieje to Docker utworzy
# anonimowy wolumen.
VOLUME /app

# Instrukcja EXPOSE wystawia wskazany port na zewnątrz kontenera.
EXPOSE 7000

# Ustawienie domyślnego polecenia, które zostanie wykonane po uruchomieniu
# kontenera. Można zdefiniować tylko jedno polecenie CMD. Polecenie można 
# nadpisć w momencie uruchamiania kontenera.
CMD ./script.sh

# Instrukcja ENTRYPOINT podobnie jak CMD ustawia domyślne polecenie dla 
# obrazu. Różnicą jest, że ENTRYPOINT nie może zostać nadpisany w momencie
# uruchamiania kontenera. Argumenty jakie podamy za nazwą obrazu podczas 
# uruchamiania kontenera staną się argumentami dla polecenia ENTRYPOINT.
# Podczas budowania obrazu zaleca się umieścić tylko polecenie CMD lub 
# tylko polecenie ENTRYPOINT. Należy unikać obu poleceń jednocześnie.
ENTRYPOINT echo Docker
```

## **OPTYMALIZACJA DOCKERFILE**

**1. Kolejność instrukcji:**

```dockerfile
# Umieszczaj instrukcje, które rzadko lub w ogóle się nie zmieniają 
# na początku Dockerfile. Przykładowo instrukcje ENV lub RUN. Z kolei
# instrukcje takie jak COPY umieszczaj możliwie pod koniec Dockerfile.
# Powód: cache. Kiedy zmieniamy coś w plikach które kopiujemy, Docker
# musi ponownie zbudować warstwę która dotyczy kopiowania tych plików
# oraz warstwy występujące po niej. 

# Zamiast tego...
COPY script.sh /app/
RUN apt-get update && apt-get install -y curl

# Stosuj to.
RUN apt-get update && apt-get install -y curl
COPY script.sh /app/
```

**2. Instrukcja USER:**

```dockerfile
# Domyślnym użytkownikiem w kontenerze jest root, który posiada 
# nieograniczone uprawnienia. Dlatego dobrą praktyką jest tworzenie
# obrazów, gdzie domyślnym użytkowniekiem jest tzw. non-root. 

# Dodaj użytkownika 'user' z id 1000, katalogiem domowym /app oraz 
# domyślną powłoką bash. Następnie zmień właściciela /app na user.
RUN useradd -u 1000 -d /app -s /bin/bash user && \
    chown -R user:user /app

# Od tej pory instrukcje takie jak RUN, CMD, ENTRYPOINT są wykonywane
# przez użytkownika 'user'.
USER user

# Kopiując pliki z hosta, zmień ich właściciela na 'user'.
COPY --chown=user:user script.sh /app/ 
```

**3. Instrukcja HEALTHCHECK:**

```dockerfile
# Instrukcja HEALTHCHECK sprawdza, czy aplikacja działa poprawnie. W tym
# przypadku sprawdzamy, czy serwer pogodowy wttr.in odpowiada na zapytania.
# W przypadku, gdy serwer nie odpowiada, kontener zostanie zatrzymany
# z kodem błędu 1.

# --interval=30s - Określa, co ile czasu ma być wykonywane sprawdzenie.
# --timeout=10s - Określa, po jakim czasie sprawdzenie zostanie zakończone.
# --start-period=10s - Określa, po jakim czasie od uruchomienia kontenera 
#                      ma zostać wykonane pierwsze sprawdzenie.
# --retries=3 - Określa liczbę sukcesywnych porażek zanim kontener zostanie
#               uznany za niezdrowy.

HEALTHCHECK --interval=30s \ 
    --timeout=10s \
    --start-period=10s \
    --retries=3 \
    CMD curl https://wttr.in/Warsaw || exit 1
```

**4. Czyszczenie cache:**

```dockerfile
# Czyszczenie cache po instalacji pakietów pozwala na zmniejszenie rozmiaru obrazu.
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*
```

**5. Montowanie w instrukcji RUN:**

```dockerfile
# Montowanie w instrukcji RUN pozwala na wykonanie kroków COPY i RUN w jednym
# kroku RUN. Pozwala ono na skopiowania np. pliku configuracyjnego, uruchomieniu
# go i usunięciu w jednej instrukcji. Dzięki temu zmniejszamy liczbę warstw
# obrazu jak i zwiększamy bezpieczeństwo, ponieważ pliki konfiguracyjne zostają
# usunięte po zainstalowaniu.

# Przykład montowania pliku init.sh, który eksportuje dwie zmienne środowiskowe.
# Następnie w celu testu przekazujemy wartości tych zmiennych do pliku info.log.
# Na koniec plik init.sh jest usuwany i nie znajduje się w kontenerze.

RUN --mount=type=bind,source=init.sh,target=/app/init.sh \
    . /app/init.sh && echo $APP $APP_NAME > info.log
```

**6. Używaj hadolint do inspekcji Dockerfile:**

```dockerfile
# Biblioteka Haskell Dockerfile Linter (hadolint) pozwala na walidację
# plików Dockerfile pod kątem stosowania najlepszych praktyk związanych
# z budowaniem obrazów.

# Link: https://github.com/hadolint/hadolint
```

**7. Używaj trivy do inspekcji obrazów:**

```dockerfile
# Narzędzie trivy znajduje luki w zabezpieczeniach, błędne konfiguracje, 
# sekrety, SBOM w kontenerach, repozytoriach kodu, chmurach i nie tylko. 

# Link: https://github.com/aquasecurity/trivy
```

## **DOCKER COMPOSE**

**1. Polecenie docker compose:**

```bash
docker compose [OPTIONS] COMMAND

OPTIONS:
  --dry-run                    # Suchy start.
  --progress <STRING>          # Progres output (auto, tty, plain, quiet).
  -p, --project-name <STRING>  # Nazwa projektu.
  -f, --file <STRING_ARRAY>    # Pliki konfiguracyjne compose.

COMMAND:
  build       # Zbuduj lub przebuduj serwisy.
  config      # Parsuj plik compose do kanonicznego formatu.
  create      # Utwórz kontenery dla serwisów. 
  down        # Ztrzymaj i usuń kontenery/sieci.
  images      # Wylistuj obrazy.
  kill        # Wymuś zatrzymanie kontenerów.
  pause       # Zatrzymaj serwisy.
  ps          # Wylistuj kontenery.
  restart     # Zresetuj kontenery.
  start       # Uruchom serwisy.
  stats       # Wyświetl statystyki zużycia dla uruchomionych kontenerów.
  stop        # Zatrzymaj serwisy.
  up          # Utwórz i uruchom serwisy.
```

**2. Przykładowy plik compose:**

```yaml
# Słowo kluczowe `services` definiuje listę obrazów i ich konfiguracji.
services:
  # Każdy serwis jest definiowany jako osobny blok.
  # W tym przypadku serwis nazywa się ubuntu.
  ubuntu:
    # Argumenty związane z budowaniem obrazu.
    build:
      # Ścieżka względem której budowany jest obraz z Dockerfile.
      context: .
      # Ścieżka do pliku Dockerfile.
      dockerfile: ./docker/Dockerfile
      # Argumenty przekazywane do Dockerfile.
      args:
        # <KEY>: <VALUE>
        UBUNTU_VERSION: 20.04
    # Nazwa obrazu, która zostanie użyta do zbudowania obrazu.
    image: ubuntu-example
    # Nazwa kontenera.
    container_name: ubuntu
    # Ustawianie zmiennych środowiskowych.
    environment:
      # <KEY>=<VALUE>
      - ENVIRONMENT=development
      - VERSION=1.0.0
    # Montowanie wolumenów.
    volumes:
      # Montowanie katalogu /home/user/data z hosta do /app/data w kontenerze.
      # <HOST_PATH>:<CONTAINER_PATH>
      # - /home/user/data:/app/data
      # Montowanie wolumenu.
      # <VOLUME_NAME>:<CONTAINER_PATH>
      - my-volume:/app/logs
    networks:
      my-network:
        # Przypisanie adresu IP do kontenera.
        ipv4_address: 172.80.40.2
    # Serwisy od których zależy serwis ubuntu.
    depends_on:
      - nginx
    # Klucz `deploy` definiuje konfigurację związaną z wzdrażaniem kontenera.
    deploy:
      # Klucz `resources` definiuje zasoby, które będą dostępne dla kontenera.
      resources:
        # Górny limit zasobów.
        limits:
          cpus: "1.0"
          memory: 512M
        # Minimalne zapotrzebowanie na zasoby.
        reservations:
          cpus: "1.0"
          memory: 128M

  # Kolejny serwis.
  debian:
    image: debian:latest
    container_name: debian
    # Klucz `command` zachowuje się jak instrukcja CMD w Dockerfile.
    command: sleep inf
    # Możliwe jest również przekazanie polecenia jako kolejnych argumentów:
    # - sleep
    # - inf
    networks:
      my-network:
        ipv4_address: 172.80.40.3
    depends_on:
      - nginx

  # Kolejny serwis.
  nginx:
    image: nginx:latest
    container_name: nginx
    # Klucz `ports` definiuje mapowanie portów.
    ports:
      # <HOST_PORT>:<CONTAINER_PORT>
      - 8080:80
    # Klucz `expose` definiuje porty, które będą dostępne dla innych kontenerów.
    expose:
      - 80
    # Klucz `networks` definiuje sieć, do której ma być podłączony serwis.
    networks:
      - my-network

# Definicja wolumenów.
volumes:
  my-volume:
    name: my-volume
    driver: local
    driver_opts:
      o: bind
      # Bez żadnego typu systemu plików.
      type: none
      # Ścieżka do katalogu na hoście względem pliku compose.
      device: ./logs

# Definicja sieci.
networks:
  my-network:
    name: my-network
    ipam:
      # Domyśly sterownik, w tym przypadku 'bridge'.
      driver: default
      # Konfiguracja adresu IP i jej rozmiaru.
      config:
        - subnet: 172.80.40.0/24
```
