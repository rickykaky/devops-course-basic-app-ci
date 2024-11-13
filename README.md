* Clonez ce repo et créez un repo privé avec son code (changez le remote et push).
* Définir un workflow GitHub Actions pour
  * Build l’application (pip) avec Python 3.9
  * Lint avec Flake8
  * Tests avec nose (nosetests)
* Définir un workflow CodeBuild 
* Faire un buildspec équivalent et créer un build dans CodeBuild
* Enrichir ce workflow pour générer un rapport JUnit avec nosetests et le stocker dans CodeBuild
