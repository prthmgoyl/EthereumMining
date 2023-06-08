# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V5dZCWEFOgdgEdxCig8XF6mWXcFMej6R
"""

!nvidia-smi

!sudo add-apt-repository ppa:ethereum/ethereum

!sudo cat /etc/apt/sources.list

!sudo apt update

!sudo apt install ethereum

!wget https://github.com/ethereum-mining/ethminer/releases/download/v0.18.0/ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz

# Commented out IPython magic to ensure Python compatibility.
# %ls
!tar -zxvf ethminer-0.18.0-cuda-9-linux-x86_64.tar.gz
# %cd bin/

!./ethminer -G -P stratum1+tcp:// XXXXXXX-xXXXXXXX-xXXXXXXX @eth-asia1.nanopool.org:9999