1. Normal mode (Esc) <---> (i) Insert mode
                ...  <---> (R) Replace mode
                ...  <---> (v) Visual mode:
                ...  <------> (V) Visual line
                ...  <------> (Ctrl+v) Visual block
                ...  <---> (:) Command-line mode

2. Normal: for moving around a file and making edits
3. Insert: for inserting text
4. Replace: for replacing text
5. Visual (plain, line, or block): for selecting blocks of text
6. Command-line: for running a command
7. :quit of :q - command to quit vim
8. :w - wirte any changes to in file
9. :help [any command, for example :w] - show an information about command
10. :sp - add a new split to the window
11. :qa - quit all the windows
12. Normal mode keys:
    h - move left
    j - move down
    k - move up
    l - move right
    w - move one word forward
    b - move backword by one word
    e - move to the end of the word
    0 - move to the begining of the line
    ^ - move to first non-empty character in a line
    o - it opens a new line below and changes the mode to INSERT
    O - it opens a new line above and changes the mode to INSERT
    D - it delete all the characters in string right
    dd - it delete the whole string
    dw - it delete the whole word
    de - it delete all content from cursor to end of word
    ce - it delete all content from cursor to end of word and open the INSERT mode
    x - delete characters to the right
    u - undone all the changes
    y - copy the line
    yw - copy the word
    p - paste copied line 
    Ctrl+r - redo all the changes
    Ctrl+u - move up
    Ctrl+d - scrolle down
    G - move all the way down
    gg - move all the way up
    L - move to lowest line on the screen
    M - move to middle line on the screen
    H - move to highest line on the screen
    fo - find the first o in a line
    Fo - find the backword o in a line
    di( - delete inside the parentheses
    ci[ - change inside brackets