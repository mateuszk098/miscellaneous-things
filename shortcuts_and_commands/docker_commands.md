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
```

```bash
docker rmi <obraz>:tag>
```

**5. Wyświetlanie informacji nt. obrazu - inspekc`ja obrazu:**

```bash
docker inspect <obraz>:<tag>
```

## **URUCHAMIANIE KONTENERÓW**
