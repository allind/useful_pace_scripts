#! /bin/bash

touch $1
echo "#! /usr/bin/env python" >> $1
echo "import sys" >> $1
echo "def main(argv):" >> $1
echo 'if __name__ == "__main__":' >> $1
echo "  main(sys.argv)" >> $1
chmod 755 $1
