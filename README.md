# Verificator de Link-uri

Un script Python pentru analizarea repository-urilor GitHub. Extrage numarul de stele, fork-uri, descrierile si limbajele. Verifica link-urile din fisierul `README.md` si creeaza un log cu link-urile invalide.

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

## Expresii Regulate Utilizate

Scriptul foloseste mai multe expresii regulate pentru diverse scopuri:

1. **Extrage URL-ul fisierului `README.md` din pagina repository-ului**:

   ```regex
   <a .*?href=\"(/[^/]+/[^/]+/blob/[^/]+/README\.md)\">
   ```

2. **Extrage toate link-urile din fisierul `README.md`**:

   ```regex
   https?://[^\s<>`\"()\[\]]+
   ```

3. **Extrage numarul de stele ale repository-ului**:

   ```regex
   <span .*?id=\"repo-stars-counter-star\" .*?title=\"([0-9,]+)\".*?>.*?</span>
   ```

4. **Extrage numarul de fork-uri ale repository-ului**:

   ```regex
   <span .*?id=\"repo-network-counter\" .*?title=\"([0-9,]+)\".*?>.*?</span>
   ```

5. **Extrage descrierea repository-ului**:

   ```regex
   <p .*?class=\"f4 my-3\".*?>(.*?)</p>
   ```

6. **Extrage limbajele de programare utilizate**:

   ```regex
   <span .*?aria-label=\"([^\"]+ [0-9\.]+)\".*?>.*?</span>
   ```

7. **Extrage repository-urile utilizatorului**:

   ```regex
   <a .*?href=\"/([^/]+/[^"]+)\" .*?itemprop=\"name codeRepository\".*?>
   ```

## Cerinte

- Python
- Module: `requests`, `colorama`

Instaleaza dependentele folosind:

```bash
pip install -r requirements.txt
```
