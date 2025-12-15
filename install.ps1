Write-Output "Création du .venv"
python -m venv .venv

Write-Output "Activation du .venv"
.venv\Scripts\Activate.ps1

Write-Output "Mise à jour de pip"
pip install --upgrade pip

Write-Output "Installation du projet"
pip install .

Write-Output "Installation terminée"
Write-Output "Lancez : demo-app"
