1. ls: -la, -lh, -lt, --color
2. In marco.sh script.
3. In debug.sh script.
4. a) Create tmp directory and some files:
    - mkdir tmp && cd tmp && mkdir tmp2 && touch {1..5}.html pict{1..5}.jpg tmp2/{a..e}.html
   b) Ziping all HTML flies:
    - find . -name "*.html" | xargs -d "\n" tar czf htmls.tar.gz
5. find . -type f -printf "%T@ %P\n" | sort -n | tail -1 | cut -d ' ' -f2