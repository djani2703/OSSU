1. echo $SHELL
2. mkdir /tmp/missing
3. man touch 
4. touch /tmp/missing/semester && cd /tmp/missing 
5. echo '!#/bin/sh' > semester && echo 'curl --head --silent https://missing.csail.mit.edu' >> semester
6. ./semester
7. sh semester
8. man chmod
9. chmod 764 semester
10. ls -l semester | cut -c33-38 > ~/last-modified.txt
11. cat /sys/class/power_supply/BAT0/capacity