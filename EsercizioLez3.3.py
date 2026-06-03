import pandas as pd
import matplotlib.pyplot as plt

# Caricamento del dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1. Grafico a barre: uomini e donne a bordo
conteggio_sesso = df["Sex"].value_counts()
plt.figure(figsize=(6, 4))
conteggio_sesso.plot(kind="bar", color=["steelblue", "salmon"])
plt.title("Passeggeri per sesso")
plt.xlabel("Sesso")
plt.ylabel("Numero di passeggeri")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Istogramma: distribuzione delle età
plt.figure(figsize=(6, 4))
plt.hist(df["Age"].dropna(), bins=20, color="seagreen", edgecolor="black")
plt.title("Distribuzione delle età")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.tight_layout()
plt.show()

# 3. Grafico a barre: passeggeri per classe
conteggio_classe = df["Pclass"].value_counts().sort_index()
plt.figure(figsize=(6, 4))
conteggio_classe.plot(kind="bar", color=["gold", "orange", "firebrick"])
plt.title("Passeggeri per classe")
plt.xlabel("Classe")
plt.ylabel("Numero di passeggeri")
plt.xticks(ticks=[0, 1, 2], labels=["Prima", "Seconda", "Terza"], rotation=0)
plt.tight_layout()
plt.show()

# 4. Grafico a torta: sopravvissuti vs non sopravvissuti

conteggio_sopravvissuti = df["Survived"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    conteggio_sopravvissuti,
    labels=["Non sopravvissuti", "Sopravvissuti"],
    autopct="%1.1f%%",
    colors=["lightcoral", "lightgreen"],
    startangle=90,
)
plt.title("Sopravvissuti vs Non sopravvissuti")
plt.tight_layout()
plt.show()

#Creare un grafico scatter che confronti: Età (Age) /Prezzo del biglietto (Fare)
plt.scatter(df["Age"], df["Fare"])

plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

dfscatter = df [["Fare", "Pclass"]]
pd.plotting.scatter_matrix(dfscatter,figsize =(20,25),  color='k', alpha=0.3)
plt.show()


#sopravvisuti per classe
survival_by_class = df.groupby(["Pclass", "Survived"]).size().unstack()
print(survival_by_class)
survival_by_class.plot(
    kind="bar",
    stacked=True
)

plt.title("Titanic Survival by Passenger Class")
plt.show()



#prima donne e bambini ?

# Bambino se età < 18
df["Category"] = "Men"

df.loc[(df["Sex"] == "female"), "Category"] = "Women"
df.loc[(df["Age"] < 18), "Category"] = "Children"

survival_rate = (
    df.groupby(["Pclass", "Category"])["Survived"]
      .mean()
      .unstack()
      * 100
)
print("survival_rate")
print(survival_rate)

survival_rate.plot(kind="bar")

plt.title("Survival Rate by Class and Category")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)

plt.show()