0x02-shell_redirections: Project on I/O redirections, chaining commands, sorting and finding.

0-hello_world - prints “Hello, World”, followed by a new line to the standard output. Utilizes the redirect symbol: >.

1-confused_smiley - write a script that displays a confused smiley "(Ôo)' Utilizes the escape character () or single quotes (') EX1: '"(Ôo)'\' EX2: \"(Ôo)\'.

2-hellofile - display the content of the /etc/passwd file.

3-twofiles - display the content of /etc/passwd and /etc/hosts Specify both folders after the command, separated by a space with no other flags.

4-lastlines - display the last 10 lines of /etc/passwd.

5-firstlines - display the first 10 lines of /etc/passwd.

6-third_line - write a script that displays the third line of the file iacta. The file iacta will be in the working directory. You're not allowed to use sed.

7-file - write a shell script that creates a file named exactly *\'"Holberton School"\'\$\?\****:) containing the text Holberton School ending by a new line. Uses the redirect -truncate symbol (>).

9-duplicate_last_line - write a script that duplicates the last line of the file iacta. Utilizes the pipe symbol (|) and the redirect -append symbol (>>).

10-no_more_js - write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders. 

11-directories - write a script that counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted. The command uses the pipe symbol (|) and counts the line numbers with another command.

12-newest_files - create a script that displays the 10 newest files in the current directory. List everything in the present working directory, organizing by time. Pipe the output through another command that lists only the top 10 lines then display to the standard output.

13-unique - create a scripts that takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word. Words should be sorted. From whatever is in the standard input, sort the list and pipe the sorted list into a command that displays only the unique lines, and not the duplicate lines, to the standard output.

14-findthatword - display lines containing the pattern "root" from the file /etc/passwd. The command requires a pattern to match (in this case "root") and also requires a file to look through.

15-countthatword - display the number of lines that contain the pattern "bin" in the file /etc/passwd. The command needs to be told how to display the results. In this case, by counting, not displaying, the matching patterns. Then it needs a pattern to match, then a place to look.

16-whatsnext - display lines containing the pattern "root" and 3 lines after them in the file. The command needs to be told what to look for and how far to look past the result. Then the pattern to match, then a place to look.

17-hidethisword - display all the lines in the file /etc/passwd that do not contain the pattern "bin". The command needs to be told to invert the pattern to look for, and a place to look.

18-letteronly - display all lines of the file /etc/ssh/sshd_config starting with a letter, include capital letters as well The command needs to be told where to look in the line for the targeted type of character. Syntax matters. 'firstCharacterSelector[:AlphabeticalSelection:]'

19-AZ - replace all characters A and c from input to Z and e respectively. Requires a specific syntax. tr zX fD fileName

20-hiago - create a script that removes all letters c and C from input. tr has a delete flag.

21-reverse - write a script that reverse its input. Very simple.

22-users_and_homes - write a script that displays all users and their home directories, sorted by users. cut has a delimiter flag. You need to specify the field that you want.

100-empty_casks - write a command that finds all empty files and directores in the current directory and all sub-directories. Only the names of the files and directoires should be displayed (not the entire path.) Hidden files should be listed, one file name per line. The listing should end with a new line character. You are not allowed to use basename, grep, egrep, fgrep, or rgrep.
Uses the printf and empty flags.

101-gifs - write a script that lists all the files with a .gif extension in the current directory and all its sub-directories. Hidden files should be listed. Only regular files, not directories should be listed. The names of the files should be displayed without their extensions. Not allowed to use basename, grep, egrep, fgrep or rgrep.

102-acrostic - create a script that decodes acrostics that use the first letter of each line. The decoded message has to end with a new line. You are not allowed to use grep, egrep, fgrep or rgrep.

103-tsv - write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. Order by numbers of requests, most active host or IP at the top. Not allowed to use grep, egrep, fgrep, or rgrep. .