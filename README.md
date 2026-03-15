# Multilevel Network Intrusion Detection System

This project builds a **two-stage network intrusion detection system** using the **UNSW-NB15** dataset.

## Project Goal
The system works in two stages:
1. classify whether network traffic is **normal or an attack**
2. if it is an attack, classify the **type of attack**

## Dataset
This project uses the **UNSW-NB15** dataset for network intrusion detection. Dataset source details and file information are provided in `data/README.md`.

## Preprocessing Overview
The dataset was prepared for a two-stage intrusion detection pipeline. The main preprocessing steps included:
- standardizing column names
- checking missing values and duplicate rows
- identifying categorical and numeric features
- one-hot encoding categorical columns (`proto`, `service`, `state`)
- scaling numeric features using `StandardScaler`
- preparing the binary target (`label`) for attack detection
- preparing the multi-class target (`attack_cat`) for attack type classification
- encoding attack-type labels for the second-stage model

## Folder Structure
- `docs/` — proposal and deliverables
- `notebooks/` — Jupyter notebooks
- `data/` — dataset notes and source information

## Note
The raw dataset files are **not uploaded to this GitHub repository** because they are large. Only project code, notebooks, and documentation are included here.