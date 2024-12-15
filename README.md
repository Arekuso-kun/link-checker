# Verificator de Link-uri

Un script Python pentru analizarea repository-urilor GitHub. Extrage numarul de stele, fork-uri, descrierile si limbajele. Verifica link-urile din fisierul `README.md` si creeaza un log cu link-urile invalide pentru revizuire.

## Instalare

1. Cloneaza acest repository:

   ```bash
   git clone https://github.com/Arekuso-kun/link-checker.git
   cd link-checker
   ```

2. Instaleaza dependentele:

   ```bash
   pip install -r requirements.txt
   ```

## Utilizare

Ruleaza scriptul din linia de comanda:

```bash
python main.py <nume-utilizator-github>
```

De exemplu:

```bash
python main.py Arekuso-kun
```

Alternativ, poti rula scriptul fara niciun argument, iar acesta va solicita sa introduci un nume de utilizator GitHub.

### Intrare

- **Nume utilizator GitHub**: Specifica numele utilizatorului GitHub ale carui repository-uri doresti sa le analizezi.

### Iesire

- **Detalii despre depozite**: Numarul de tele, fork-uri, descrierea si limbajele.
- **Link-uri din README**: Verifica toate link-urile din fisierul `README.md` pentru toate depozitele acelui utilizator.
- **Fisier de log**: Salveaza link-urile invalide in directorul `logs`.

## Cerinte

- Python
- Module: `requests`, `colorama`

Instaleaza dependentele folosind:

```bash
pip install -r requirements.txt
```
