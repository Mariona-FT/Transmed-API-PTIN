# TransMed - API

## Visió General
Aquest repositori conté la component d'api de web i l'aplicació del projecte [TransMed](https://github.com/PTIN-2023), una solució avançada per a la gestió i distribució autònoma de medicaments. 
Aquest projecte de la API s'ha desenvolupat dins del marc de l'assignatura "PTIN" durant el semestre de primavera de 2023 pel grup A3.

## Característiques del Projecte TransMed

TransMed aprofita tecnologies punteres per desenvolupar un sistema de transport intel·ligent i segur, optimitzant el repartiment de medicaments essencials de manera eficient. El projecte integra diferents components, cadascun amb una funció clau dins del sistema global de distribució:

El repositori general del projecte és accessible a [TransMed Project](https://github.com/PTIN-2023).

- **Web Interface ([WEB](https://github.com/PTIN-2023/web))**: Interfície d'usuari per a la gestió i seguiment de comandes.
- **API de Serveis ([API](https://github.com/PTIN-2023/api))**: Gestiona la lògica de negoci i la comunicació entre la interfície web i les aplicacions.
- **Aplicació Mòbil ([APP](https://github.com/PTIN-2023/app))**: Permet als usuaris sol·licitar i seguir medicaments en moviment.
- **Sistema de Vehicles Autònoms ([VEHICLES](https://github.com/PTIN-2023/vehicles))**: Inclou tota la gestió i operativa dels vehicles i drons encarregats del repartiment.


### Funcionalitats Destacades
- **Seguiment en Temps Real**: Monitorització continua dels enviaments de medicaments.
- **Gestió d'Ordres**: Interfície web per crear, gestionar i revisar ordres.
- **Notificacions**: Alertes instantànies sobre actualitzacions d'ordres i canvis en les rutes.
- **Informes**: Generació d'informes detallats i anàlisis per millorar la presa de decisions.

## Integració de la API
L'API de TransMed actua com a columna vertebral tecnològica del sistema, integrant diversos components clau per a la gestió eficient del transport de medicaments, operant dins un esquema combinat de **Cloud** i **Fog Computing**:

- **Enllaç amb MongoDB**: L'API utilitza MongoDB per emmagatzemar i gestionar dades de manera eficient, incloent detalls de les comandes, informació d'usuari i registres de transaccions, tot gestionat des del **Cloud** per a una escalabilitat i accessibilitat màxima.
- **Interacció amb la Interfície Web**: Proporciona els endpoints necessaris per que la web interactue amb les dades de l'API, permetent funcions com la gestió de comandes i el seguiment en temps real.
- **Connexió amb l'Aplicació Android**: Permet a l'aplicació mòbil accedir i manipular les dades necessàries per a l'operativitat en dispositius mòbils, incloent la validació de medicaments per part dels metges.
- **Control de Vehicles Autònoms i Drons**: L'API envia comandes als vehicles autònoms i coordina una flota de drons per l'última milla de l'entrega, implementant una combinació de processament **Cloud** per a tasques generals i **Fog Computing** a nivell local per a operacions ràpides i amb baixa latència en el repartiment.

### Seguretat Transversal
A més, tota la infraestructura API està protegida amb capes de seguretat transversals que cobreixen tant la comunicació de dades com la confidencialitat de la informació, implementades tant en l'entorn de **Cloud** com en el de **Fog** per assegurar una protecció completa en tots els nivells de l'arquitectura.

### Implementació Tècnica
Per interactuar amb l'API, els desenvolupadors poden referir-se a la documentació específica que detalla els endpoints disponibles, els mètodes de petició i les expectatives de resposta. Això permet una integració fàcil i robusta per part de tots els components del sistema TransMed.

Aquesta API no només facilita la interoperabilitat entre diferents plataformes i dispositius sinó que també optimitza la gestió logística del transport de medicaments, convertint TransMed en una solució de transport de medicaments àgil i adaptable, ideal per a escenaris d'ús que requereixen altes demandes de dades i temps de resposta ràpid.

## Començar
Segueix aquests passos per executar l'interfície web en el teu entorn local per a desenvolupament i proves:
1. Clona el repositori a la teva màquina local.
2. Navega fins al directori del projecte.
3. Instal·la les dependències requerides.
4. Inicia el servidor de desenvolupament.

## Contribució i Desenvolupament
En la creació del projecte s'ha seguit una **metodologia àgil SCRUM**,s'ha desenvolupat amb iteracions que han permés la col·laboració i la ràpida adaptació als canvis dels clients i noves tecnologies. 

## Agraïments
- Gràcies al personal del curs PTIN per la seva orientació.
- Agraïments especials a tots els membres del grup A3 pel seu esforç col·laboratiu.

**Nota**: Aquest repositori és un fork de la part de l'API original de TransMed, on he col·laborat activament, especialment en el desenvolupament i refinament dels serveis de l'API.
