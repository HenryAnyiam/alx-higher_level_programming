#include "lists.h"

/**
  *insert_node - inserts node into a sorted list
  *@head: pointer to pointer to first node
  *@number: new number
  *)
  *Return: new node or NULL
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *former = NULL;
	listint_t *new_head;

	new_head = malloc(sizeof(listint_t));
	if (new_head == NULL)
		return (NULL);
	new_head->n = number;
	while (current->next != NULL)
	{
		if (current->n > number)
		{
			new_head->next = current;
			if (former != NULL)
				former->next = new_head;
			return (new_head);
		}
		former = current;
		current = current->next;
	}
	current->next = new_head;
	return (new_head);
}
