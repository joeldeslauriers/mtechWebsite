# Prompt Claude Code — Site Web Multi-Page Groupe Mtech Inc.

## CONTEXTE

Tu vas construire un site web **multi-page** complet, moderne et fluide pour **Groupe Mtech Inc. — Division Toiture**, une entreprise de couverture basée à Saint-Hippolyte (Québec). Le site remplace leur Wix actuel (groupemtech.ca). Tout le contenu est défini ci-dessous — ne l'invente pas.

---

## ASSETS DISPONIBLES

- **Logo** : `Assets/Logo/Logo Transparent.png` (monochrome, fond transparent)
- **Vidéo hero** : `Assets/Video/MTech - Background.mp4`
- Tous les fichiers vont dans `C:\MTech WebSite\`

---

## ARCHITECTURE DES FICHIERS

```
index.html          → Accueil
a-propos.html       → À propos
services.html       → Services (liste complète)
materiaux.html      → Matériaux (BP, GAF, IKO)
emploi.html         → Emploi / Carrières
soumission.html     → Soumission gratuite
zones.html          → Zones desservies (SEO local)
css/style.css       → Feuille de style globale partagée
js/main.js          → JS global partagé (navbar, animations, etc.)
```

Chaque page HTML inclut le même `<head>` de base, le même `<nav>` et le même `<footer>`, mais avec un `<title>` et une `<meta description>` **uniques et optimisés SEO**.

---

## THÈME & DESIGN SYSTEM

### Couleurs (dans `css/style.css` via CSS custom properties)
```css
:root {
  --black:      #111111;
  --charcoal:   #1C1C1C;
  --red:        #D62828;
  --red-dark:   #A61E1E;
  --offwhite:   #F5F5F0;
  --midgray:    #6B7280;
  --lightgray:  #D1D5DB;
  --white:      #FFFFFF;
}
```

### Typographie (Google Fonts)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```
- **Montserrat 700–900** → H1, H2, H3, nav, boutons
- **Inter 400–600** → corps de texte, descriptions, labels

### Layout
- Max-width : `1280px`, centré avec `margin: 0 auto`
- Sections padding : `96px` vertical desktop / `64px` mobile
- Breakpoints : `768px` et `1024px`
- Icônes : SVG inline uniquement (pas FontAwesome)

---

## COMPOSANTS PARTAGÉS (navbar + footer)

### NAVBAR (fixe, identique sur toutes les pages)
- Fond `--black` + `backdrop-filter: blur(12px)` après scroll
- Logo gauche : `Assets/Logo/Logo Transparent.png` (height 48px)
- Liens : Accueil · Services · À propos · Matériaux · Emploi
- Bouton CTA rouge : **"SOUMISSION GRATUITE"** → `soumission.html`
- Lien actif mis en rouge selon la page courante (classe `.active` sur `<a>`)
- Mobile : hamburger → menu plein écran noir animé

### FOOTER (identique sur toutes les pages)
- Bande rouge 4px en haut
- Logo + slogan : *"Votre couvreur de confiance dans les Laurentides"*
- Liens rapides, coordonnées, réseaux sociaux
- **Coordonnées** :
  - 📞 514-247-3491
  - 🚨 514-605-7114 (Urgence 24/7)
  - ✉ info@groupemtech.ca
  - 📍 40 rue Belvédère, Saint-Hippolyte, QC J8A 0N1
  - Licence RBQ : 5868-4754-01
- Barre bas : `© 2025 Groupe Mtech Inc. | Tous droits réservés`

---

## BALISE `<HEAD>` SEO — TEMPLATE PAR PAGE

Chaque page doit avoir ces balises (valeurs uniques par page) :

```html
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[TITRE PAGE] | Groupe Mtech Inc. — Couvreur Laurentides</title>
  <meta name="description" content="[DESCRIPTION 150-160 caractères avec mots-clés locaux]">
  <meta name="keywords" content="couvreur, toiture, Laurentides, Montréal, [ville spécifique]">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.groupemtech.ca/[page]">

  <!-- Open Graph -->
  <meta property="og:title" content="[TITRE]">
  <meta property="og:description" content="[DESCRIPTION]">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.groupemtech.ca/[page]">
  <meta property="og:site_name" content="Groupe Mtech Inc.">
  <meta property="og:locale" content="fr_CA">

  <!-- Schema.org LocalBusiness (sur toutes les pages) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "RoofingContractor",
    "name": "Groupe Mtech Inc.",
    "description": "Couvreurs experts à Montréal, Laurentides et Lanaudière. Installation et réfection de toitures en bardeaux d'asphalte.",
    "url": "https://www.groupemtech.ca",
    "telephone": "+1-514-247-3491",
    "email": "info@groupemtech.ca",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "40 rue Belvédère",
      "addressLocality": "Saint-Hippolyte",
      "addressRegion": "QC",
      "postalCode": "J8A 0N1",
      "addressCountry": "CA"
    },
    "areaServed": [
      "Saint-Hippolyte", "Saint-Jérôme", "Mirabel", "Saint-Eustache",
      "Sainte-Thérèse", "Blainville", "Boisbriand", "Rosemère",
      "Lorraine", "Bois-des-Filion", "Terrebonne", "Mascouche",
      "Sainte-Marthe-sur-le-Lac", "Deux-Montagnes", "Saint-Joseph-du-Lac",
      "Oka", "Lachute", "Mont-Laurier", "Sainte-Agathe-des-Monts",
      "Saint-Sauveur", "Morin-Heights", "Saint-Lin-Laurentides",
      "Repentigny", "Montréal", "Laval", "Saint-Canut"
    ],
    "openingHours": "Mo-Fr 07:00-18:00",
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Services de toiture"
    },
    "sameAs": ["https://www.facebook.com/profile.php?id=61579399678321"],
    "identifier": {
      "@type": "PropertyValue",
      "name": "Licence RBQ",
      "value": "5868-4754-01"
    }
  }
  </script>
</head>
```

---

## PAGES — CONTENU DÉTAILLÉ

---

### PAGE 1 — `index.html` (Accueil)

**`<title>`** : `Couvreur Laurentides & Montréal | Groupe Mtech Inc. — Toiture Durable`
**`<meta description>`** : `Couvreurs experts à Saint-Jérôme, Mirabel, Saint-Eustache, Blainville et Montréal. Réfection, toiture neuve, réparation. Soumission gratuite. Licence RBQ 5868-4754-01.`

#### Section HERO
- Vidéo `Assets/Video/MTech - Background.mp4` plein écran (`object-fit: cover`, autoplay, muted, loop, playsinline)
- Overlay gradient : `rgba(0,0,0,0.65)` → `rgba(0,0,0,0.35)`
- Hauteur : `100vh`
- Contenu centré :
  - Badge pill rouge : `✓ Licence RBQ 5868-4754-01`
  - **H1** (Montserrat 900, 72px desktop / 42px mobile, blanc) :
    ```
    Votre Toiture.
    Notre Expertise.
    ```
  - Sous-titre (Inter 400, 20px, `rgba(255,255,255,0.85)`) :
    ```
    Couvreurs experts dans les Laurentides, Montréal et Lanaudière.
    Installations durables, prix compétitifs, équipe de confiance.
    ```
  - Boutons :
    - Rouge : **"SOUMISSION GRATUITE →"** → `soumission.html`
    - Outline blanc : **"NOS SERVICES"** → `services.html`
  - Scroll indicator animé (chevron qui bounce) en bas

#### Section STATS (fond noir, bande entre hero et services)
4 compteurs animés (IntersectionObserver + JS counter de 0 à valeur) :
- **27+** — Années d'expérience combinée
- **500+** — Toitures réalisées
- **3** — Régions desservies
- **24/7** — Service d'urgence

#### Section SERVICES (fond `--offwhite`)
- H2 : "NOS SERVICES"
- Sous-titre : "Solutions complètes pour tous vos besoins de toiture"
- Grille 3×2, cartes hover animées :
  1. Réfection de toiture
  2. Toiture neuve résidentiel & commercial
  3. Réparation
  4. Inspection
  5. Déneigement
  6. Urgence 24/7 ← carte fond noir, texte blanc, se démarque
- Bouton centré dessous : **"VOIR TOUS NOS SERVICES →"** → `services.html`

#### Section À PROPOS (fond noir)
- H2 blanc : "Bâtis sur l'expérience, guidés par la qualité"
- Texte : 27 ans d'expérience combinée, Mike & Anthony, bardeaux d'asphalte
- 3 engagements avec ✓ rouge
- Stat visuelle côté droit

#### Section ZONES DESSERVIES (fond `--offwhite`)
- H2 : "NOS ZONES DESSERVIES"
- Sous-titre : "Nous intervenons sur la Rive-Nord de Montréal et dans les Laurentides"
- Grille de pills/badges gris avec hover rouge pour chaque ville (voir liste complète ci-dessous)
- CTA : **"VOIR TOUTES NOS ZONES →"** → `zones.html`

#### Section MATÉRIAUX — aperçu (fond blanc)
- H2 : "LES MEILLEURS MATÉRIAUX"
- 3 logos/cartes : BP · GAF · IKO
- CTA → `materiaux.html`

#### Section CTA FINAL (fond rouge `--red`)
- Grand texte blanc : "Prêt à refaire votre toiture ?"
- Sous-texte : "Réponse garantie en moins de 24h. Soumission 100% gratuite et sans engagement."
- Bouton noir : **"OBTENIR MA SOUMISSION GRATUITE"** → `soumission.html`
- Téléphone cliquable : 514-247-3491

---

### PAGE 2 — `services.html`

**`<title>`** : `Services de Toiture Laurentides | Réfection, Réparation, Urgence | Groupe Mtech`
**`<meta description>`** : `Réfection de toiture, installation neuve, réparation, inspection, déneigement et urgence 24/7 à Saint-Jérôme, Mirabel, Blainville, Saint-Eustache. Soumission gratuite.`

#### Contenu
- Hero section sobre : fond noir, H1 "NOS SERVICES", breadcrumb
- **6 sections de service détaillées** (une par service, alternance fond blanc / fond `--offwhite`) :

**1. RÉFECTION DE TOITURE**
- H2, description longue : *"Nous redonnons vie à votre toiture grâce à une réfection complète et durable. Nos experts s'assurent que chaque détail est pris en charge pour protéger votre maison contre les intempéries québécoises."*
- Inclus : retrait ancien bardeau, inspection charpente, membrane, bardeaux neufs, nettoyage complet
- FAQ (3 questions) avec `<details>/<summary>` :
  - "Combien coûte une réfection de toiture dans les Laurentides ?"
  - "Combien de temps dure une réfection complète ?"
  - "Quelle garantie offrez-vous sur une réfection ?"

**2. TOITURE NEUVE — RÉSIDENTIEL & COMMERCIAL**
- Description : nouvelles constructions et projets commerciaux
- FAQ :
  - "Quel type de bardeaux recommandez-vous pour le climat québécois ?"
  - "Intervenez-vous sur les bâtiments commerciaux ?"

**3. RÉPARATION**
- Description : infiltrations, bardeaux abîmés, intervention rapide
- FAQ :
  - "Comment savoir si ma toiture a besoin d'une réparation ?"
  - "Intervenez-vous en hiver ?"

**4. INSPECTION**
- Description : détection préventive, rapport professionnel
- FAQ :
  - "À quelle fréquence devrait-on faire inspecter sa toiture ?"
  - "L'inspection est-elle incluse dans la soumission ?"

**5. DÉNEIGEMENT**
- Description : protection hivernale, équipe sécurisée
- FAQ :
  - "Quand faut-il faire déneiger sa toiture ?"

**6. URGENCE 24/7**
- Section visuellement distincte (fond noir, accent rouge vif)
- Texte : *"En cas de fuite ou de dommage imprévu, notre équipe est disponible rapidement pour intervenir et protéger votre maison ou votre commerce."*
- Numéro urgence bien visible : **514-605-7114**
- Bouton rouge : "APPELER MAINTENANT"

- Bas de page : CTA soumission

---

### PAGE 3 — `a-propos.html`

**`<title>`** : `À Propos | Couvreurs Experts depuis 27 ans | Groupe Mtech Inc. Laurentides`
**`<meta description>`** : `Groupe Mtech Inc., fondé par Mike et Anthony, 27 ans d'expérience combinée en toiture résidentielle et commerciale dans les Laurentides et Montréal. Licence RBQ 5868-4754-01.`

#### Contenu
- Hero : fond noir, H1 "À PROPOS DE NOUS"
- Section histoire : texte complet, 27 ans d'expérience, Mike & Anthony
- Section engagements : 3 cartes (Qualité · Satisfaction client · Professionnalisme)
- Section "Pourquoi nous choisir" : 4-5 points différenciateurs
- Licence RBQ mise en avant (badge)
- CTA soumission en bas

---

### PAGE 4 — `materiaux.html`

**`<title>`** : `Matériaux de Toiture — BP, GAF, IKO | Groupe Mtech Inc. Laurentides`
**`<meta description>`** : `Groupe Mtech utilise les meilleurs bardeaux d'asphalte : BP, GAF et IKO. Matériaux certifiés, durables et garantis pour toitures résidentielles et commerciales dans les Laurentides.`

#### Contenu
- Hero : fond noir, H1 "MATÉRIAUX & FABRICANTS"
- Intro : *"Nous utilisons exclusivement les meilleurs bardeaux d'asphalte de l'industrie : BP, GAF et IKO. Des matériaux durables, garantis et adaptés au climat québécois."*
- **3 sections fabricant** (une par marque, grandes cartes) :

**BP (Building Products)**
- Description, gammes disponibles, garantie
- Bouton : "Voir la brochure BP" (PDF — `#` pour l'instant)

**IKO**
- Dynasty et Cambridge mentionnés
- Bouton : "Brochure IKO Dynasty" + "Brochure IKO Cambridge"

**GAF**
- Description, réputation nord-américaine
- Bouton : "Voir la brochure GAF"

- Section "Pourquoi les bardeaux d'asphalte ?" : 4 avantages (durabilité, esthétique, coût, adaptation climat)
- CTA soumission

Les brochures sont ici C:\MTech WebSite\Assets\Brochures
--- 

### PAGE 5 — `emploi.html`

**`<title>`** : `Emploi — Couvreur Laurentides | Rejoignez Groupe Mtech Inc.`
**`<meta description>`** : `Groupe Mtech recrute : maître couvreur, chef d'équipe, apprenti couvreur et manœuvre dans les Laurentides. Rejoignez une équipe dynamique. Postulez maintenant.`

#### Contenu
- Hero : fond noir, H1 "JOIGNEZ-VOUS À NOTRE ÉQUIPE"
- Sous-titre : *"Nous sommes toujours à la recherche de personnes motivées et professionnelles pour agrandir notre équipe."*
- **4 postes disponibles** (cartes) :
  - Maître couvreur
  - Chef d'équipe
  - Apprenti couvreur
  - Manœuvre
- Avantages de travailler chez Mtech : 4-5 points
- **Formulaire de candidature** :
  - Prénom · Nom · Email · Téléphone · Poste désiré (select) · Date d'entrée disponible · Message
  - Upload CV (optionnel) : `<input type="file" accept=".pdf,.doc,.docx">`
  - Bouton rouge : "ENVOYER MA CANDIDATURE"
  - `action="mailto:info@groupemtech.ca"` + `enctype` approprié

---

### PAGE 6 — `soumission.html`

**`<title>`** : `Soumission Gratuite — Toiture Laurentides | Groupe Mtech Inc.`
**`<meta description>`** : `Obtenez votre soumission gratuite pour tous vos travaux de toiture dans les Laurentides, Montréal et Lanaudière. Réponse garantie en moins de 24h. Licence RBQ 5868-4754-01.`

#### Contenu
- Hero sobre : fond noir + rouge, H1 "SOUMISSION GRATUITE"
- Badge : "Réponse garantie en moins de 24h"
- Layout 2 colonnes :
  - **Gauche** : 4-5 raisons de choisir Mtech + coordonnées complètes + badge RBQ
  - **Droite** : Formulaire complet :
    - Nom complet *
    - Téléphone *
    - Email *
    - Ville / Municipalité * (champ texte)
    - Type de service (select) : Réfection · Toiture neuve · Réparation · Inspection · Déneigement · Urgence · Autre
    - Description des travaux (textarea)
    - Bouton rouge : **"ENVOYER MA DEMANDE →"**
    - `action="mailto:info@groupemtech.ca"` method POST
- Numéro urgence rouge bien visible : 514-605-7114

---

### PAGE 7 — `zones.html` ← PAGE SEO DÉDIÉE

**`<title>`** : `Zones Desservies — Couvreur Rive-Nord & Laurentides | Groupe Mtech Inc.`
**`<meta description>`** : `Groupe Mtech intervient à Saint-Jérôme, Mirabel, Saint-Eustache, Sainte-Thérèse, Blainville, Boisbriand, Rosemère, Saint-Canut, Lachute et partout dans les Laurentides.`

#### Contenu
- Hero : fond noir, H1 "NOS ZONES DESSERVIES"
- Intro : *"Groupe Mtech intervient sur l'ensemble de la Rive-Nord de Montréal et dans les Laurentides. Voici les principales municipalités que nous desservons :"*

- **Section Rive-Nord de Montréal** (H2) :
  Blainville, Boisbriand, Bois-des-Filion, Deux-Montagnes, Laval, Lorraine, Mirabel, Oka, Rosemère, Saint-Eustache, Saint-Joseph-du-Lac, Sainte-Marthe-sur-le-Lac, Sainte-Thérèse, Terrebonne, Mascouche, Repentigny

- **Section Laurentides** (H2) :
  Saint-Hippolyte, Saint-Jérôme, Saint-Canut, Saint-Lin-Laurentides, Lachute, Sainte-Agathe-des-Monts, Saint-Sauveur, Morin-Heights, Mont-Tremblant, Val-David, Val-Morin, Prévost, Piedmont, Shawbridge, Brownsburg-Chatham, Gore, Wentworth-Nord

- **Section Montréal & périphérie** (H2) :
  Montréal (toutes arrondissements), Laval, Longueuil

- Pour chaque ville : petite carte avec nom + "Couvreur [Ville]" en sous-titre (bonne pour SEO)

- Texte SEO long (1 paragraphe par région) avec mention naturelle des villes :
  *"Notre équipe de couvreurs certifiés intervient dans toutes les municipalités de la MRC de La Rivière-du-Nord, incluant Saint-Jérôme, Saint-Canut, Mirabel et les environs..."*

- Note bas de page : *"Votre ville n'est pas dans la liste ? Contactez-nous — nous desservons un large territoire et pouvons souvent intervenir au-delà de nos zones habituelles."*

- CTA : **"OBTENIR UNE SOUMISSION POUR MA VILLE"** → `soumission.html`

---

## JS GLOBAL (`js/main.js`)

1. **Navbar scroll** : classe `.scrolled` au-delà de 80px → hauteur réduite, fond plein
2. **Menu mobile** : hamburger toggle, overlay plein écran, fermeture au clic d'un lien
3. **Active nav link** : comparaison `window.location.pathname` avec `href` de chaque lien
4. **IntersectionObserver animations** : fade-in + translateY(30px → 0) sur `.animate-in`, délais en cascade pour grilles (`.stagger-1`, `.stagger-2`, etc.)
5. **Compteurs animés** : uniquement sur `index.html`, ciblés via `[data-counter]`, comptent de 0 à la valeur cible quand visibles
6. **Smooth scroll** : `document.querySelectorAll('a[href^="#"]')` → `scrollIntoView({behavior:'smooth'})`
7. **Bouton urgence mobile fixe** : visible uniquement sous 768px, bas d'écran, rouge, `tel:514-605-7114`

---

## CSS (`css/style.css`)

- Reset CSS minimal (box-sizing, margin 0, padding 0)
- Custom properties `:root` (voir design system)
- Styles globaux : body, h1-h6, p, a, button
- Composants réutilisables : `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.section-label`, `.card`, `.grid-2`, `.grid-3`
- Navbar + footer styles
- Animations : `@keyframes fadeInUp`, `.animate-in`, `.stagger-*`
- Media queries : `@media (max-width: 1024px)` et `@media (max-width: 768px)`

---

## EXIGENCES TECHNIQUES

- HTML5 sémantique (`<header>`, `<nav>`, `<main>`, `<section id="...">`, `<footer>`)
- Pas de framework CSS externe, pas de jQuery
- Google Fonts via `<link rel="preconnect">` uniquement
- Icônes SVG inline
- Chemins assets relatifs (fonctionne depuis le disque local)
- `lang="fr"` sur `<html>` de toutes les pages
- Tous les `<img>` ont un attribut `alt` descriptif en français
- Les numéros de téléphone sont des liens `<a href="tel:+15142473491">`
- Performance : la vidéo hero doit avoir `preload="none"` et un `poster` fallback (image noire)
- Le formulaire soumission et emploi utilisent `action="mailto:info@groupemtech.ca"` + `method="post"` + `enctype="text/plain"` (simple, pas de backend)

---

## QUALITÉ ATTENDUE

- Design cohérent et professionnel sur toutes les pages
- Transitions fluides, animations `ease-out`
- SEO solide : balises uniques par page, Schema.org, mots-clés locaux naturellement intégrés dans le contenu
- Mobile parfaitement responsive
- Toutes les pages se lient entre elles correctement (liens relatifs)
- Le site doit donner l'impression d'un travail de $5,000+

---

## OUTPUT FINAL

Génère tous les fichiers dans cet ordre :
1. `css/style.css`
2. `js/main.js`
3. `index.html`
4. `services.html`
5. `a-propos.html`
6. `materiaux.html`
7. `emploi.html`
8. `soumission.html`
9. `zones.html`
