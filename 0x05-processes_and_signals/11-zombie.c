#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
* infite_while - function that runs an infinite loop with a gap of 1 sec.
* Return: 0
**/
int infite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - creates 5 zombie processes and prints their PID.
* Return: 0
**/
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", pid);
		sleep(1);
	}
	infite_while();
	return (0);
}
