#!/bin/bash

echo Processing PFDtrans
echo duplicating...
cp -p pfd/PFDtrans.txt pfd/PFDtrans_test2.txt
echo replacing...
sed -i s/\|\,\,\|/\|\,\|\|\,\|/g pfd/PFDtrans_test2.txt  # replacing |,,| with |,||,| 
sed -i s/\|\,\|/\\t/g pfd/PFDtrans_test2.txt             # replacing |,| with tab
sed -i s/\|\,/\\t/g pfd/PFDtrans_test2.txt               # replacing |, with tab
sed -i s/\,\|/\\t/g pfd/PFDtrans_test2.txt               # replacing ,| with tab
sed -i s/\|//g pfd/PFDtrans_test2.txt	                 # removing | at the beginning and at the end
echo done.

echo Processing PFDasset
echo duplicating...
cp -p pfd/PFDasset.txt pfd/PFDasset_test2.txt
echo replacing...
sed -i s/\|\,\,\|/\|\,\|\|\,\|/g pfd/PFDasset_test2.txt  # replacing |,,| with |,||,| 
sed -i s/\|\,\|/\\t/g pfd/PFDasset_test2.txt             # replacing |,| with tab
sed -i s/\|\,/\\t/g pfd/PFDasset_test2.txt               # replacing |, with tab
sed -i s/\,\|/\\t/g pfd/PFDasset_test2.txt               # replacing ,| with tab
sed -i s/\|//g pfd/PFDasset_test2.txt	                 # removing | at the beginning and at the end
echo done.

echo finished. 
