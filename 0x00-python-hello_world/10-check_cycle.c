#include "lists.h"

/**
  *check_cycle - detects loop in a linked list
  *@list: pointer to first node
  *)
  *Return: 1 if loop, else 0
  */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	long int pt;

	while (current)
	{
		pt = current - current->next;
		if (pt > 0)
			current = current->next;
		else
			return (1);
	}
	return (0);
}
