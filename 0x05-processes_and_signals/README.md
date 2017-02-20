0x05. Processes and signals
The purpose of this project is to understand Linux PID, process, signal, traps etc.

## Description of Files:

0-what-is-my-pid - Bash script that displays its PID.

1-list_your_processes - Bash script that displays a list of currently running processes.

2-show_your_bash_pid - Bash script that displays line containing the bash
		     word, this allowing you to easily get the PID of your Bash process.

3-show_your_bash_pid_made_easy - Bash script that displays the PID, along
			       with the process name, of processes which name contains
			       the word bash, without using ps.

4-to_infinity_and_beyond - Bash script that displays To infinity and beyond indefinitely.

5-kill_me_now - Bash script that kills 4-to_infinity_and_beyond process.

6-kill_me_now_made_easy - Bash script that kills 4-to_infinity_and_beyond process,
			without using kill or killall.

7-highlander - Bash script that displays string literal indefinitely and when receiving a signal.

67-kill_me_now_made_easy - kills the 7-highlander process.

8-beheaded_process - kills the process 7-highlander.

9-process_and_pid_file - Bash script that creates a file, deletes it, display
		       different string literals on different signals.

manage_my_process - Bash script that writes a string literal to /tmp/my_process.

10-manage_my_process - Bash (init) script that manages manage_my_process.

11-zombie.c - a C program that creates 5 zombie processes.
