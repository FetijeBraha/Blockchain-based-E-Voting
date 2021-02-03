# Blockchain-based E-voting Simulation

## Përshkrimi

Ky është një projekt i bazuar në Python Django për të simuluar një koncept të protokollit të votimit elektronik të bazuar në blockchain. Ky projekt duhet të ekzekutohet vetëm në serverin e zhvillimit me mënyrën Debug të aktivizuar. Simulimi përfshin dy seksione:  __"Block"__ dhe __"Chain"__.
![block and chain](https://user-images.githubusercontent.com/76743818/106743346-8c126580-661e-11eb-87e3-e274f663f98e.png)


### "Block"

Skenari: jë votues potencial duhet të paraqitet në organizatorin e votimit, duke treguar ID e tij dhe dokumente të tjera ligjore. Më në fund, ai duhet të paraqesë një çelës publik d.m.th., ECC. Supozojmë se ai e ka regjistruar me sukses çelësin publik.

Përmes faqes së votimit (si më poshtë), votuesi duhet të shkruajë pseudonimin e tij (UUID 4) dhe numrin e kandidatit të cilin dëshiron ta votojë. Më pas, kjo fletë e votimit nënshkruhet duke përdorur një çelës privat. Nëse fleta e paraqitur e votimit vërtetohet se është e vlefshme, ajo do të vuloset (minohet). Në këtë pjesë një bllok përmban vetëm fletën e votimit. Procesi mund të shqyrtohet i tëri duke përdorur konsolën.


(Çifti i çelësave publik-privat është i koduar në mënyrë të vështirë dhe gjenerohet nga jashtë. Shihni detajet teknike më poshtë.)

![Ballot page](https://user-images.githubusercontent.com/76743818/106745563-91bd7a80-6621-11eb-9c56-c559cc19ee59.png)

### "Chain"

Në këtë seksion, do të gjenerohen transaksione (fletëvotime) me të dhëna të vlefshme. Më pas ato mbyllen në blloqe. Pas kësaj, ju mund të eksploroni transaksionet dhe blloqet, si dhe të përpiqeni të manipuloni të dhënat dhe t'i verifikoni ato. 

![Sealed ballot](https://user-images.githubusercontent.com/GottfriedCP/Blockchain-based-E-Voting-Simulation/master/screenshots/Screenshot_3.jpg)

![Block](https://user-images.githubusercontent.com/GottfriedCP/Blockchain-based-E-Voting-Simulation/master/screenshots/Screenshot_4.jpg)

<!-- _The screenshot above shows that a node's database (i.e., your node) has been tampered. You will not see this in real blockchain explorer, but this should give you a glimpse of why tampering immutable ledger is futile._ -->

## Si ta ekzekutojmë

1. Bëni gati mjedisin tuaj virtual (rekomandohet). 
2. Vendosni 'requirements.txt' file. Instaloni paketat e nevojshme: `pip install -r requirements.txt`.
3. Vendosni 'manage.py' file. Ekzekutoni `python manage.py runserver`. Pastaj qasuni në linkun http://localhost:8000.
4. Nga faqja kryesore, gjithashtu ekzekutoni 'Block' ose 'Chain' duke klikuar 'Start'.

## Detajet teknike

Çelësi privat i përdorur në këtë demonstrim ndodhet në folder-in 'bbevoting_project' ('demo_private.pem' file), ndërsa çelësi përkatës publik është i koduar në mënyrë të vështirë  'settings.py' (look for `PUBLIC_KEY`). gjithashtu mund të vendosni disa karakteristika të konfigurimit si p.sh. `N_TRANSACTIONS`, `N_TX_PER_BLOCK`, dhe vështirësia e enigmës  (`PUZZLE` dhe `PLENGTH`).

## Fotografitë

Folderi 'screenshots' përmban fotografitë që janë nxjerrë nga projekti.

## Mirënjohjet

Ky projekt përdor një version të modifikuar të  "pymerkletools" nga Tierion për krijimin e merkle root duke përdorur SHA3.

## Licensa

Shikoni MIT licencën e përfshirë.
