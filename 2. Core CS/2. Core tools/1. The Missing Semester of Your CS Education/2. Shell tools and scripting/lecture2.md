1. foo=bar - Create variable foo with value bar
2. echo $foo - Print the value of foo
3. 'some text' or "some text" - Two ways to create a string in bash
4. echo "hello $foo" - Approach to printing a variable on a string
5. $1..$n - Get 1..n argument in a bash script
6. $? - Get an error code of the previous command in a bash
7. $_ - Get the last argument of the previous command in bash
8. $# - Get count of arguments
9. $@ - Get all arguments (from 1 to n)
10. $$ - Get pid of current process
11. !! - Substitute the previous command. For example: sudo !!
12. false && print "some text" - Won't print anything
13. false || print "some text" - It'll print "some text"
14. true && print "some text" - It'll print "some text"
15. true || print "some text" - Won't print anything
16. true ; echo "some text" - concatinate commands and always print "some text"
17. foo=$(date) - Substitute data from function
18. cat <(ls) <(ls ..) - Getting concationation of both file
19. touch proj{1,2}/src/test/foo{,1,2,3} - Create files foo, foo1, foo2..
20. touch {foo, bar}/{a..j} - Create a series of files for foo and bar directories
21. find . -name src -type d - Search directories named src in a project
22. find . -path '**/test/*.py' -type f - Search for files in the project
23. grep foobar -R - Recursively search for files with foobar content inside
24. rg "import" -t py ~/Projects/Study/Python- Find all py files containing the word import inside
25. history | grep rg - Search for bash history containing rg
26. ls -R - List the contents of all directories
27. nnn - Start file manager in bash