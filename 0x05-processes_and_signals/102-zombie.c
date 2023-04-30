#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
  int i;
  pid_t pid;

  for (i = 0; i < 5; i++) {
    pid = fork();
    if (pid == 0) {
      exit(0);
    }
    else if (pid > 0) {
      printf("Zombie process created, PID: %d\n", pid);
    }
    else {
      fprintf(stderr, "Fork failed!\n");
      return 1;
    }
  }

  sleep(10);

  return 0;
}
