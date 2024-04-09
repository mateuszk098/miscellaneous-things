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
  --name <NAME>            # Nadanie nazwy kontenerowi. 

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
docker container rm [OPTIONS] <CONTAINER_ID>|<NAME>
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
