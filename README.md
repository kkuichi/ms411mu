## Riešenie reálnej úlohy analýzy dát v medicíne 

### Použité datasety:
* [heart_2022_with_nans.csv.zip](/heart_2022_with_nans.csv.zip) - hlavný dataset
* [df_test.csv](/df_test.csv) - testovacia množina vytvorená z hlavného datasetu
* [df_testEDIT.csv](/df_testEDIT.csv) - upravená testovacia množina po spracovaní dát
* [df_train.csv](/df_train.csv) - trénovacia množina vytvorená z hlavného datasetu
* [df_trainEDIT.csv](/df_trainEDIT.csv) - upravená trénovacia množina po spracovaní dát
---

Súbor [notebook.ipynb](/notebook.ipynb) obsahuje kód pre predikciu srdcového ochorenia na základe datasetu [heart_2022_with_nans.csv](/heart_2022_with_nans.csv.zip). Cieľom je určiť, či má osoba vysoké riziko výskytu srdcového ochorenia na základe rôznych faktorov, ako sú fyzické a duševné zdravie, lekárska anamnéza a iné.
Súbor zahŕňa rôzne kroky metodológie CRISP-DM, vrátane načítania dát, analýza dát, spracovania dát, modelovania a vyhodnocovania výsledkov.
### Požadované knižnice:
* optuna
* pandas
* numpy
* matplotlib.pyplot
* seaborn
* scipy.stats
* joblib
* imblearn.under_sampling
* sklearn.linear_model
* sklearn.svm
* sklearn.ensemble
* sklearn.preprocessing
* sklearn.metrics
* scipy.stats
* imblearn.over_sampling
* imblearn.combine

### Obsah súboru:
1. Definícia potrebných knižníc a importovanie datasetu;
2. Analýza datasetu, vrátane základných informácií, korelácií medzi stĺpcami a analýzy chýbajúcich hodnôt;
3. Príprava dát, vrátane odstránenia duplicitných a chýbajúcich hodnôt, rozdelenia datasetu na trénovacie a testovacie množiny a spracovania kategorických stĺpcov;
4. Modelovanie pomocou rôznych modelov strojového učenia, vrátane RandomForestClassifier, LogisticRegression a SVC;
5. Vyhľadávanie optimálnych parametrov pre modely pomocou optuna.
---
Súbor [model.pkl](/model.pkl) obsahuje najlepšie natrénovaný model s najvyšším výkonom. V tomto súbore je uložená verzia modelu SVC (Support Vector Classification).

---

Súbor [predict_app.py](/app/predict_app.py) obsahuje grafické používateľské rozhranie (GUI) vytvorené pomocou knižnice Tkinter a jej rozšírenia customtkinter. GUI slúži ako aplikácia pre predikciu rizika srdcového ochorenia na základe rôznych vstupných údajov.

Potrebné knižnice pre spustenie tohto súboru sú:
- pathlib
- pandas
- joblib
- tkinter
- customtkinter
- PIL

Súbor importuje [model.pkl](/app/model.pkl), ktorý obsahuje natrénovaný model strojového učenia pre predikciu srdcového ochorenia. Funkcia "left()," center() a "right() slúžia na prechod medzi obrazovkami v aplikácii. Funkcia "predict() vykonáva predikciu na základe vstupných údajov a zobrazí výsledok v aplikácii.
