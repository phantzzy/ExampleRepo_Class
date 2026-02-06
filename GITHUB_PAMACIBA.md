# 📚 GitHub Pamācība Iesācējiem

> **Soli pa solim** – no nulles līdz pilnvērtīgam darbam ar Git un GitHub

---

## 📋 Saturs

- [0. Pirms sākam](#0-pirms-sākam)
- [1. daļa — Repo izveide un GitHub interfeiss](#1-daļa--repo-izveide-set-up-un-orientēšanās-github)
- [2. daļa — Git komandas: clone, commit, push, pull, merge](#2-daļa--darbs-ar-git-clone-commit-push-pull-merge-uc)
- [Mini "čītlapa"](#-mini-čītlapa)
- [Praktiskais vingrinājums](#-praktiskais-vingrinājums)

---

## 0. Pirms sākam

### Git vs GitHub – kāda ir atšķirība?

| | Git | GitHub |
|---|-----|--------|
| **Kas tas ir?** | Rīks tavā datorā | Vietne/mākonis |
| **Ko dara?** | Seko izmaiņām failos (versiju kontrole) | Glabā Git repozitorijus, ļauj strādāt komandā |
| **Kur strādā?** | Lokāli (tavā datorā) | Internetā (github.com) |

### Nepieciešams

- ✅ **GitHub konts**: [github.com](https://github.com)
- ✅ **Git** (ja strādāsi no datora): [git-scm.com](https://git-scm.com)
- 💡 *Iesācējiem:* [GitHub Desktop](https://desktop.github.com) – vienkāršāka programma nekā komandrinda

---

# 1. daļa — Repo izveide, set-up un orientēšanās GitHub

## 1) Izveido GitHub kontu un ieslēdz drošību

1. Reģistrējies: [github.com](https://github.com)
2. **Ieteicams:** `Settings` → `Password and authentication` → ieslēdz **Two-factor authentication (2FA)**

---

## 2) Izveido jaunu repozitoriju

1. GitHub augšējā labajā stūrī: **`+`** → **`New repository`**

2. Aizpildi:
   - **Repository name:** piemēram `mana-pirma-repo`
   - **Description:** īss apraksts (pēc izvēles)
   - **Public** vai **Private**

3. Atzīmē (iesācējiem ieteicams):
   - ✅ `Add a README file` – lai repo nav tukša
   - ✅ `Add .gitignore` – ja zini valodu (Python, Node, u.c.)
   - ✅ `Choose a license` – ja gribi publiski dalīties (piem. MIT)

4. Spied **`Create repository`**

---

## 3) Repo "set-up" pēc izveides

Repo sākumā paskaties uz šiem failiem:

| Fails | Kam domāts |
|-------|------------|
| `README.md` | Projekta "vizītkarte" – nosaukums, apraksts, kā lietot |
| `.gitignore` | Norāda, ko Git nedrīkst komitot (piem. `node_modules/`, `.env`) |
| `LICENSE` | Licences nosacījumi (ja repo ir publisks) |

> 💡 **Padoms:** Repo kvalitāte ļoti aug, ja README un .gitignore ir sakārtoti jau pirmajā dienā!

---

## 4) Kā orientēties GitHub repozitorija interfeisā

### 📁 Code (galvenā sadaļa)

- Failu un mapju saraksts
- **Branch izvēle** (piem. `main`, `feature/...`)
- **Commits skaits** (klikšķināms)
- 🟢 **`<> Code`** poga: clone URL, Open with GitHub Desktop, Download ZIP

**Biežākās darbības:**
- `Add file` → `Create new file` – izveido failu tieši webā
- `Add file` → `Upload files` – augšupielādē failus
- ✏️ ikona – labo failu tiešsaistē

### 🐛 Issues

- Uzdevumu/problēmu pierakstīšana
- Var pievienot etiķetes (labels), piešķirt cilvēkiem

### 🔀 Pull Requests (PR)

- Sadarbības centrs
- Izmaiņas no cita zara tiek "piedāvātas" apvienošanai ar `main`
- Ļauj komentēt, pārskatīt (review) un tad apvienot (merge)

### ⚡ Actions

- Automatizācija (CI/CD): testi, build, deploy
- *Iesācējiem nav obligāti, bet labi zināt*

### 📊 Citas sadaļas

| Sadaļa | Apraksts |
|--------|----------|
| Projects | Plānošana kā kanban dēlis |
| Wiki | Papildus dokumentācija |
| Security | Drošības brīdinājumi |
| Insights | Statistika: commits, contributors |
| Settings | Repo iestatījumi, līdzautori, branches noteikumi |

---

## 5) Kā ātri lejupielādēt repo (bez Git)

Ja gribi vienkārši lejupielādēt repo kā mapi:

1. Repo sadaļā `Code` spied zaļo **`<> Code`** pogu
2. Izvēlies **`Download ZIP`**
3. Izpako ZIP savā datorā

> ⚠️ Šis ir "bez Git" variants. Ja gribi komitot un pushot, labāk izmanto `git clone`.

---

# 2. daļa — Darbs ar Git: clone, commit, push, pull, merge u.c.

## 6) Git uzstādīšana

### A) Instalē Git

Lejupielādē: [git-scm.com](https://git-scm.com)

### B) Iestati vārdu un e-pastu (vienreiz)

Atver termināli:

```bash
git config --global user.name "Tavs Vārds"
git config --global user.email "tavs.epasts@example.com"
```

### C) Autentifikācija ar GitHub

**Vienkāršākais variants iesācējiem:**
- GitHub Desktop, vai
- HTTPS clone + Git Credential Manager

**Alternatīva:** SSH atslēga (ērti ilgtermiņā, bet sākumā vairāk soļu)

> ⚠️ GitHub vairs nelieto paroli HTTPS pieejai – jālieto "token" (PAT) vai GitHub Desktop/CLI

---

## 7) Repo klonēšana (clone) uz datoru

1. GitHub repo sadaļā `Code` → nokopē **HTTPS URL**
2. Terminālī:

```bash
git clone https://github.com/lietotajs/mana-pirma-repo.git
cd mana-pirma-repo
```

Tagad tev ir repo lokāli! 🎉

---

## 8) Pamatkomandas, ko lietosi visu laiku

```bash
# Pārbaudi, kas notiek
git status

# Paskaties izmaiņu vēsturi
git log --oneline

# Paskaties atšķirības (pirms komita)
git diff
```

---

## 9) Commit process (soli pa solim)

Pieņemsim, ka tu izmainīji failu `README.md`:

### 1. Pārbaudi statusu
```bash
git status
```

### 2. Pievieno izmaiņas "staging"
```bash
git add README.md
```
vai visu uzreiz:
```bash
git add .
```

### 3. Izveido commit ar skaidru ziņu
```bash
git commit -m "Atjaunina README ar projekta aprakstu"
```

> 💡 **Ieteikums commit ziņām:**
> - Sāc ar darbības vārdu: "Pievieno…", "Salabo…", "Atjauno…"
> - Esi īss un konkrēts

---

## 10) Push (augšupielādē izmaiņas GitHub)

```bash
# Ja strādā main zarā
git push

# Ja tas ir jauns zars (pirmā reize)
git push -u origin mans-zars
```

---

## 11) Pull (paņem jaunākās izmaiņas no GitHub)

Pirms sāc strādāt, bieži ir laba ideja:

```bash
git pull
```

Tas apvieno (merge) attālinātās izmaiņas tavā lokālajā zarā.

---

## 12) Branch (zari) – kā strādāt pareizi komandā

Parasti komandas darbs notiek tā:
- `main` ir **stabils**
- Jaunas izmaiņas taisa **atsevišķā zarā**: `feature/...` vai `fix/...`

### Izveido jaunu zaru un pārslēdzies uz to

```bash
git checkout -b feature/jauna-sadala
```

vai jaunākā sintakse:
```bash
git switch -c feature/jauna-sadala
```

### Strādā, komito un push uz GitHub

```bash
git add .
git commit -m "Pievieno jaunu sadaļu"
git push -u origin feature/jauna-sadala
```

---

## 13) Pull Request (PR) un Merge GitHub pusē

1. Atver repo **GitHub**
2. Parādīsies poga **`Compare & pull request`** (vai ej uz `Pull requests` → `New pull request`)
3. PR aprakstā norādi:
   - Ko izdarīji
   - Kā pārbaudīt
4. Ja viss ok, spied **`Merge pull request`**

### Merge veidi

| Metode | Apraksts |
|--------|----------|
| **Merge commit** | Saglabā visu vēsturi ar merge komitu |
| **Squash and merge** | Salīmē vairākus commits vienā (glītāk) |
| **Rebase and merge** | Pārkārto vēsturi (iesācējiem nav obligāti) |

---

## 14) Merge lokāli (no komandrindas)

Pieņemsim, ka gribi apvienot `feature/jauna-sadala` ar `main`:

```bash
# Pārslēdzies uz main un atjaunini
git checkout main
git pull

# Apvieno zaru
git merge feature/jauna-sadala

# Aizsūti uz GitHub
git push
```

---

## 15) Konflikts (conflict) – ko darīt?

Konflikts rodas, ja 2 cilvēki izmaina vienu un to pašu vietu failā.

### Kā atrisināt:

1. Git paziņos konfliktu un norādīs failus
2. Atver failu – tur būs marķieri:

```
<<<<<<< HEAD
tavs teksts
=======
cita teksta variants
>>>>>>> feature/...
```

3. Izlem, kuru versiju atstāt (vai apvieno abus)
4. Izdzēs marķierus
5. Tad:

```bash
git add konflikts-fails.txt
git commit -m "Atrisina merge konfliktu"
git push
```

---

## 16) Kā "atcelt" kļūdas

### A) Atmest nekomitotas izmaiņas failā
```bash
git checkout -- fails.txt
```

### B) Izņemt failu no staging
```bash
git reset fails.txt
```

> ⚠️ Ja neesi drošs – pajautā vai izmanto GitHub Desktop!

---

## 17) GitHub Desktop (bez komandrindas)

1. Instalē [GitHub Desktop](https://desktop.github.com)
2. `File` → `Clone repository`
3. Veic izmaiņas (ar VS Code vai citu redaktoru)
4. Desktop parādīs difus → ieraksti commit ziņu → `Commit to ...`
5. `Push origin`
6. PR var izveidot no Desktop vai GitHub lapā

---

# 📋 Mini "čītlapa"

```bash
git clone <url>           # Lejupielādē repo uz datoru
git status                # Rāda izmaiņas
git add .                 # Sagatavo komitam
git commit -m "..."       # Saglabā izmaiņas lokāli
git push                  # Aizsūta uz GitHub
git pull                  # Paņem jaunākās izmaiņas
git checkout -b <zars>    # Izveido jaunu zaru
git merge <zars>          # Apvieno zaru ar pašreizējo
```

---

# 🏋️ Praktiskais vingrinājums (20–30 min)

1. ✅ Izveido repo GitHub ar README
2. ✅ Klonē repo lokāli
3. ✅ Izveido zaru `feature/intro`
4. ✅ Pievieno README sadaļu "Par mani"
5. ✅ Commit + push
6. ✅ Izveido PR un merge
7. ✅ `git pull` lokāli, lai redzi apvienoto rezultātu

---

## 📝 Autori un licence

Šī pamācība ir brīvi pieejama mācību nolūkiem.

---

> 💬 **Jautājumi?** Jautā skolotājam vai atver Issue šajā repozitorijā!
