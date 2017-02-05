0x01-shell_permissions: Project on changing permissions, groups and owners for files.

0-iam_betty - changes user ID to "betty". Uses only 8 characters.

1-who_am_i - prints current user ID.

2-groups - prints all the groups the current user is part of.

3-new_owner - changes owner of file "hello" to user "betty"

4-empty - creates an empty file called "hello"

5-execute - adds execute permission for the file "hello"

6-multiple_permissions - on the file "hello", adds execute permissions to owner and group owner, and adds read permission to other users.

7-everybody - on the file "hello", adds execute permissions to the owner, group owner and the other users.

8-james_bond - on the file "hello", adds permissions as follows: no permission at all for owners, and group owners. All permissions for all other users.

9-john_doe - on the file "hello", set mode of the file to this: -rwxr-x-wx

10-mirror_permissions - set the mode of file "hello" the same as file "olleh". (They are both in the same working directory)

11-directory_permissions - adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed

12-directory_permissions - create a script that creates a directory called dir_holberton with permissions 751 in the working directory.

13-change_group - write a script that changes the group owner to holberton for the file "hello" (File "hello" will be in the current working directory)


14-change_owner_and_group - write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

15-symbolic_link_permissions - write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.

16-if_only - write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. (file "hello" is in the current working directory)

100-Star_Wars - write a script to play starwars in the terminal.

101-man_holberton - create a man page that looks like the one on the intranet.