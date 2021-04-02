Simple operations:
1. date - Tue 23 Mar 2021 01:05:28 PM EET
2. echo hello echo - hello echo
3. echo $PATH - /home/prog/.local/bin:/home/prog/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
4. which echo - /usr/bin/echo
5. pwd - /home/prog/Projects/OSSU/
6. cd /home - /home
7. cd .. - /
8. cd ./home -/home
9. cd ~ - /home/prog
10. ls - lost+found prog
11. ls .. - bin Desktop home lib64 ..
12. ls -l - -rw-rw-r-- 1 prog prog 444 Mar 23 14:19 lecture1.txt
12. mv n.txt new.txt - rw-rw-r-- 1 prog prog 0 Mar 24 13:40 new.file
13. cp new.txt copy_new.txt - rw-rw-r-- 1 prog prog 0 Mar 24 13:48 copy_new.txt
14. rm copy_new.txt && ls -l - ls: cannot access 'copy_new.txt': No such file or directory
15. mkdir My\ Photos - drwxrwxr-x 2 prog prog 4096 Mar 24 13:54 'My Photos'
16. man ls - NAME: ls - list directory contents

Pipes and redirections:
17. echo hello > new.txt - Receive the string hello in the file new.txt
18. cat < new.txt - hello
19. cat < new.txt > cp_new.txt - hello in cp_new.txt
20. cat < new.txt >> cp_new.txt - hellohello in cp_new.txt
21. ls -l | tail -n1 - rw-rw-r-- 1 prog prog  441 Mar 24 14:01 new.txt
22. curl --head google.com | grep Content-Length - 219
23. sudo echo 10000 > /sys/devices/../brightness
24. echo 20000 | sudo tee brightness - 20000
25. xdg-open new.txt - open a file