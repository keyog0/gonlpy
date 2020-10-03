# GoNLpy
This repository include  Morpheme analyzer for gopizza

# Install KoNLPy
version == 0.4.3
include == KoNLpy, Mecab

# Why use Mecab
Loading time: Class loading time, including dictionary loads.    
Execution time: Time for executing the pos method for each class, with 100K characters.    
|Name | Loding time|Excution time|
|:---|---:|:---:|
|Kkma| 5.6988 secs|35.7163 secs|
|Komoran| 5.4866 secs|25.6008 secs|
|Hannanum| 0.6591 secs|8.8251 secs|
|Okt (previous Twitter)| 1.4870 secs|2.4714 secs|
|Mecab| **0.0007 secs**|**0.2838 secs**|

![Alt text](readme/time.png)


## MAC OS
1. install KoNLpy
```
pip install konlpy     # Python 2.x
pip3 install konlpy    # Python 3.x
```
2. install MeCab
```
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

## Ubuntu
1. install KoNLpy
```
sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
sudo apt-get install python-dev; pip install konlpy     # Python 2.x
sudo apt-get install python3-dev; pip3 install konlpy   # Python 3.x
```
2. install MeCab
```
sudo apt-get install curl
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```
