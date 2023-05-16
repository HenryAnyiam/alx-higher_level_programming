#include "lists.h"

/**
 * addnode - add new node to beginning of a linked list
 * @head: start of linked list
 * @n: integer
 * )
 * Return: Null or Head to modified node
 */
listint_t *addnode(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (*head);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to first node
 * )
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *count = *head;
	listint_t *check = *head;
	listint_t *comp = NULL;
	listint_t *comp_head;

	if (*head == NULL)
		return (1);
	while (count)
	{
		comp = addnode(&comp, count->n);
		count = count->next;
	}
	comp_head = comp;
	while (check)
	{
		if (comp->n != check->n)
		{
			free(comp_head);
			return (0);
		}
		comp = comp->next;
		check = check->next;
	}
	free(comp_head);
	return (1);
}
