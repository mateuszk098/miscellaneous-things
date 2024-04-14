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
  -a, --all    # Usuń wszystkie nieużywane zasoby.
  -f, --force  # Nie pytaj o potwierdzenie.
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

**7. Montowanie wolumenu w kontenerze:**

```bash
docker run [...] -v <VOLUME>:<CONTAINER_PATH> [...]

# Przykład uruchamiania kontenera Ubuntu z zamontowanym wolumenem 'data'.
docker run -it -v data:/data ubuntu:22.04 bash
```
