#!/bin/bash

echo duplicating...
cp -p PFDtrans.txt PFDtrans_test.txt
echo replacing...
sed -i s/\,\,/\,\|\|\,/g PFDtrans_test.txt
sed -i s/\|\,\|/\\t/g PFDtrans_test.txt
sed -i s/\|//g PFDtrans_test.txt
echo done.

