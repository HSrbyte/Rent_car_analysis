import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys

# Obtenir le chemin du répertoire de l'exécutable
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Charger un fichier de donnéesw
chemin_fichier = os.path.join(base_path, "data", "cars_ML.xlsx")

# Chargement des données
cars = pd.read_excel(chemin_fichier)

# Transformation des données
# Suppression des espaces et 'km', puis conversion en valeurs numériques
cars['Mileage_clean'] = cars['Mileage'].str.replace(' km', '').str.replace(' ', '').astype(float)

# Création des catégories de kilométrage
def categorize_mileage(mileage):
    if pd.isna(mileage):
        return 'nan'
    elif mileage < 50000:
        return '< 50 000'
    elif 50000 <= mileage < 100000:
        return '50 000 - 100 000'
    elif 100000 <= mileage < 150000:
        return '100 000 - 150 000'
    else:
        return '> 150 000'

cars['Mileage_category'] = cars['Mileage_clean'].apply(categorize_mileage)

# Transformation des prix et rentabilité
cars['Compatibility'] = cars['Message'].apply(lambda x: 'oui' if isinstance(x, str) and x.startswith('Votre') else 'non')
cars['Loc_price'] = cars['Message'].str.extract('(\d+)').astype(float)
cars['Price'] = cars['Price'].replace('[€\s]', '', regex=True).astype(float)
cars['Annual_Rentability_Percent'] = (cars['Loc_price'] * 12 / cars['Price']) * 100  # Rentabilité en %

# Modifier "Make and Model" pour supprimer tout après " phase"
cars['Make and Model'] = cars['Make and Model'].str.split(' phase').str[0]

# Interface Streamlit
st.title("Analyse de Rentabilité des Modèles de Voitures")

# Filtrage par pays
country_options = cars['Country'].unique()
selected_countries = st.sidebar.multiselect(
    "Sélectionnez un ou plusieurs pays:",
    options=country_options,
    default=country_options
)
filtered_cars = cars[cars['Country'].isin(selected_countries)]


# Filtrage par type d'affaire
Deal_options = cars['Deal'].unique()
selected_deals = st.sidebar.multiselect(
    "Sélectionnez un ou plusieurs type d'affaire:",
    options=Deal_options,
    default=Deal_options
)
filtered_cars = cars[cars['Deal'].isin(selected_deals)]

# Filtrage par année
year_options = cars['Year'].unique()
selected_years = st.sidebar.multiselect(
    "Sélectionnez un ou plusieurs années:",
    options=year_options,
    default=year_options
)
filtered_cars = cars[cars['Year'].isin(selected_years)]

# Filtre sur le kilométrage
mileage_options = cars['Mileage_category'].unique()
selected_mileage = st.sidebar.multiselect(
    "Sélectionnez une catégorie de kilométrage:",
    options=mileage_options,
    default=mileage_options
)
filtered_cars = filtered_cars[filtered_cars['Mileage_category'].isin(selected_mileage)]

# Filtre sur le carburant
fuel_options = cars['Fuel Type'].unique()
selected_fuel = st.sidebar.multiselect(
    "Sélectionnez une catégorie de carburant:",
    options=fuel_options,
    default=fuel_options
)
filtered_cars = filtered_cars[filtered_cars['Fuel Type'].isin(selected_fuel)]

# Filtrage par score
min_score = st.sidebar.number_input("Score minimum", min_value=0.0, max_value=1.0, value=0.75, step=0.01)
max_score = st.sidebar.number_input("Score maximum", min_value=0.0, max_value=1.1, value=1.1, step=0.01)
filtered_cars = filtered_cars[(filtered_cars['Score'] >= min_score) & (filtered_cars['Score'] <= max_score)]

# Filtrage par prix d'achat
min_price = st.sidebar.number_input("Prix d'achat minimum (€)", min_value=0, max_value=int(cars['Price'].max()), value=2000, step=100)
max_price = st.sidebar.number_input("Prix d'achat maximum (€)", min_value=0, max_value=int(cars['Price'].max()), value=15000, step=100)
filtered_cars = filtered_cars[(filtered_cars['Price'] >= min_price) & (filtered_cars['Price'] <= max_price)]

# Création des onglets
tabs = st.tabs(["Aperçu des Données", "Statistiques des Prix après Filtrage", "Top Modèles Rentables", "Analyse Personnalisée"])

# Onglet 1 : Aperçu des Données
with tabs[0]:
    st.write("### Aperçu des Données Filtrées")
    st.write(filtered_cars.head())

    # Graphiques pour la colonne "Eligibility"
    st.write("#### Statistiques de la colonne 'Eligibility'")
    fig_eligibility_count = px.histogram(filtered_cars, x="Eligibility", title="Répartition des valeurs de 'Eligibility'")
    st.plotly_chart(fig_eligibility_count, use_container_width=True)
    
    fig_eligibility_country = px.histogram(filtered_cars, x="Eligibility", color="Country", title="Répartition des valeurs de 'Eligibility' par Pays")
    st.plotly_chart(fig_eligibility_country, use_container_width=True)

# Onglet 2 : Statistiques des Prix après Filtrage
with tabs[1]:
    
    # Création de deux colonnes
    col1, col2 = st.columns(2)

    # Résumé statistique du prix d'achat
    with col1:
        st.write("#### Résumé statistique du prix d'achat")
        st.write(filtered_cars['Price'].describe())

    # Résumé statistique du prix de location
    with col2:
        st.write("#### Résumé statistique du prix de location")
        st.write(filtered_cars['Loc_price'].describe())
    
    # Graphiques boxplot
    fig_price = px.box(filtered_cars, x="Price", title="Distribution du Prix d'Achat (Prix en €)", color="Deal", color_discrete_sequence=['red', 'orange', 'green', 'pink', 'white'])
    st.plotly_chart(fig_price, use_container_width=True)


# Onglet 3 : Top Modèles Rentables
with tabs[2]:
    st.write("### Top Modèles Rentables")
    top_50_cars = filtered_cars.nlargest(50, 'Annual_Rentability_Percent')
    
    # Graphique pour les modèles les plus rentables
    fig_top_models = px.bar(
        top_50_cars,
        y="Make and Model",
        x="Annual_Rentability_Percent",
        title="Top 50 Voitures les Plus Rentables",
        labels={"Annual_Rentability_Percent": "Rentabilité Annuelle (%)"},
        orientation="h",
        color="Annual_Rentability_Percent",
        color_continuous_scale='Inferno'
    )
    st.plotly_chart(fig_top_models, use_container_width=True)

    # Calcul de la rentabilité moyenne par modèle
    avg_rentability = filtered_cars.groupby('Make and Model')['Annual_Rentability_Percent'].mean().reset_index()

    # Supprimer les valeurs NaN dans la rentabilité
    avg_rentability = avg_rentability.dropna(subset=['Annual_Rentability_Percent'])

    # Graphique en nuage de points de la rentabilité moyenne
    fig_scatter_avg_rentability = px.scatter(
        avg_rentability,
        x="Make and Model",
        y="Annual_Rentability_Percent",
        title="Rentabilité Moyenne par Modèle",
        labels={"Annual_Rentability_Percent": "Rentabilité Annuelle Moyenne (%)", "Make and Model": "Modèle"},
        size="Annual_Rentability_Percent",
        size_max=30,
        color="Annual_Rentability_Percent",
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig_scatter_avg_rentability, use_container_width=True)

    # Graphique en barres de la rentabilité moyenne par modèle
    st.write("#### Graphique en Barres de la Rentabilité Moyenne par Modèle")
    fig_bar_avg_rentability = px.bar(
        avg_rentability,
        x="Make and Model",
        y="Annual_Rentability_Percent",
        title="Rentabilité Moyenne par Modèle",
        labels={"Annual_Rentability_Percent": "Rentabilité Moyenne (%)"},
        color="Annual_Rentability_Percent",
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig_bar_avg_rentability, use_container_width=True)

# Onglet 4 : Analyse Personnalisée
with tabs[3]:
    st.write("### Analyse Personnalisée")

    # Graphique en nuage de points Prix d'achat vs Prix de location
    st.write("#### Prix d'Achat vs Prix de Location")
    fig_scatter = px.scatter(
        filtered_cars,
        x="Price",
        y="Loc_price",
        color="Annual_Rentability_Percent",
        hover_data=["Make and Model", "Year"],
        title="Nuage de Points: Prix d'Achat vs Prix de Location",
        labels={"Price": "Prix d'Achat (€)", "Loc_price": "Prix de Location (€)"},
        color_continuous_scale='Plasma'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
