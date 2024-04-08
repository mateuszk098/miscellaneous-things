# **PODSTAWOWE KOMENDY DOCKERA**

## **OBRAZY**

**1. Szukanie obrazów Dockera:**

```bash
docker search <obraz>
```

**2. Wyświetlenie obrazów dostępnych na obecnej maszynie:**

```bash
docker image ls
```

**3. Pobranie obrazu z Docker Hub:**

```bash
# Jeśli nie podamy tagu, to Docker automatycznie pobierze obraz
# z tagiem `latest`.

docker pull <obraz>:<tag>
```

**4. Usuwanie pobranego obrazu:**

```bash
docker image rm <obraz>:<tag>
docker rmi <obraz>:tag>
```

**5. Wyświetlanie informacji nt. obrazu - inspekcja obrazu:**

```bash
docker inspect <obraz>:<tag>
```

**6. Wyświetlanie historii obrazu:**

```bash
docker history <obraz>:<tag>
```

## **URUCHAMIANIE KONTENERÓW**

**1. Uruchamianie kontenera:**

```bash
# Jeżeli obraz nie jest pobrany to Docker automatycznie zacznie jego
# pobieranie. Ponadto, jeśli nie podamy tagu to zostanie wybrany 
# automatyczny tag czyli `latest`.

docker run [OPCJE] <obraz>:<tag> [POLECENIE]

OPCJE:
  -i, --interactive  # Tryb interaktywny, możliwość wysyłania/odbierania informacji.
  -t, --tty          # Emulowanie terminala.

POLECENIE:  # Kontener działa dopóki polecenie jest aktywne. Przykłady poleceń.
  bash      # Uruchomienie terminala.
  ./hello   # Uruchomienie skryptu o nazwie `hello`.
            # Odłączenie się od polecenia (kontener nadal będzie aktywny): CTRL + P, Q
```

**2. Wyświetlanie kontenerów:**

```bash
docker ps [OPCJE]
docker container ls [OPCJE]

OPCJE:
  -a, --all     # Pokaż wszystkie kontenery.
  -l, --latest  # Pokaż ostatni utworzony kontener.
```

```bash

```
