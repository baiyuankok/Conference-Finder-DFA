# Conference-Finder-DFA

## Table of Contents

- [Intro](#intro)
- [Install](#install)
- [Output](#output)

## Intro

This project is a localhost web application that implements a Deterministic Finite Automata (DFA) recognizer as a conference/workshop finder to find patterns from the user input

Features:
* Visualisation using boldface of the pattern in the text
* Display of the position and occurrences of the pattern(s) found.

The DFA recognises the following 19 patterns (which was retrieved from [International Conferences in Malaysia 2022 & 2023](https://www.allconferencealert.com/malaysia.html?srh=1&searchtopic=&searchcountry=&searchmonth=&searchcity=Kuala%20Lumpur&searchdate=&page=2)):<br>
ICMBS, ICITS, ICIRPEBS, ICBAES, ICBMSS, ICEABT, ICEFR, ICCSNS, ICCSPEE, ICCSIEE, ICCBEE, ICAASS, ICAPM, ICAIMLBDE, ICAIRME, EUICNB, EUIC3BCB, EUIWNMC, EUCELS

## Install

Download the whole project to use

Python 3 and Django should be installed


## Output

Examples  | Result
------------- | -------------
Accepted  | ![image](https://user-images.githubusercontent.com/72374023/170331716-7b7d3c66-e098-42eb-abc0-df75f692ded8.png)
Rejected  | ![image](https://user-images.githubusercontent.com/72374023/170331796-d7256e07-333a-4757-b2ef-5e00f3727a37.png)
