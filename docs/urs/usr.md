### User Requirements Specification Document
##### ITS ICT

**VERSION : 0.8**

**Authors**  
Lorenzo Motto

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| 0.78 | 22/09/2022 | Lorenzo | Bug Fixes |


# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction

<a name="sp1.1"></a>

### 1.1 Document Scope

Il documento va a mostrare le funzionalità dell'app. 

<a name="sp1.2"></a>

### 1.2 Definitios and Acronym


| Acronym				| Definition | 
| ------------------------------------- | ----------- | 
| E.C.                               | Estratto conto |

<a name="sp1.3"></a>

### 1.3 References 

<a name="p2"></a>

## 2. System Description
<a name="sp2.15"></a>

### 2.1 Context and Motivation

Applicazione sviluppata sotto richiesta dell'azienda "ePortafoglio"

<a name="sp2.2"></a>

### 2.2 Project Obectives 

L'utente dell'app potrà, attraverso l'accesso tramite credenziali segrete, oltre che a visualizzare il proprio E.C. potrà anche inviare e ricevere denaro all'interno e all'esterno del circuito "ePortafoglio", in modo semplice e veloce tramite un codice univoco associato ad ogni singolo E.C.

<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders

#### Utenti
| Gruppo | Ruoli | Obiettivo |
| ----------- | ----------- | ----------- |
|Funzionario "ePortafoglio" | Dipendenti adebiti alla gestione dell'app | Gestire organizzazione di iscrizioni, bloccare conti, assistenza clienti |
|Cliente | Utilizzatore dell'app | Utilizzatore finale dell'app | Iscriversi, aprire conti, chiudere conti, trasferire denaro |
 

#### Regolatori
| Gruppo | Ruoli |
| ----------- | ----------- | 
| Prof  | STakeholder universale | 



<a name="sp3.2"></a>
### 3.2 Functional Requirements 

#### 3.2.0 Requisiti Generali
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 0.1.0 | Per poter creare un conto è necessario un deposito minimo |M|


#### 3.2.0 Requisiti Funzionali Applicazione

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.1.0 |  L'app crea i conti su richiesta |M| 
| 1.1.1 |  L'app assegna i codici univoci ai conti |M|
| 1.1.2 |  L'app si occupa di comunicare al di fuori del proprio circuito per i trasferimenti di denaro [M]

#### 3.2.2 Requisiti Funzionali Cliente

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 2.1.0 |  Il Cliente può accedere all'app e visualizzare il proprio E.C. [M]
| 2.2.0 |  Il Cliente può inviare e ricevere denaro tramite il codice. [M]
| 2.3.0 |  Il Cliente può decidere se aprire uno o più conti. [M]
| 2.3.1 |  Il Cliente può decidere se chiudere uno o più conti. [M]


#### 3.2.3 Requisiti Funzionali Funzionari

| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 3.1.0 |  Il Funzionario può bloccare il conto se necessario |M|
| 3.1.1 |  Il Funzionario si occupa dell'assistenza clienti |M|
| 3.2.0 |  Il Funzionario verifica la buona riuscita delle transazioni e risolve eventuali problemi |M|


<a name="sp3.3"></a>
### 3.3 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| R1 | Il software deve essere compatibile con Windows, MACOS, e Linux |M|
| R2 | Il software deve essere accessibile tramite tutti i browser |M|
| R3 | Il software deve essere accessibile tramite app dedicata (Android e IoS) |D|
| R4 | Il software deve appoggiarsi su un database dedicato |M|
| R5 | Il software deve essere disponibile anche in Inglese |M|