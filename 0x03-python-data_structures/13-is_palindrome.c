#include "lists.h"

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
	int i, j, k = 0, len = 0;
	long int total_1 = 0, total_2 = 0, first, last;

	if (*head == NULL)
		return (1);
	first = count->n;
	while (count)
	{
		count = count->next;
		len++;
	}
	i = len / 2;
	j = len - i;
	while (check)
	{
		last = check->n;
		if (k < i)
			total_1 += check->n;
		if (k >= j)
			total_2 += check->n;
		check = check->next;
		k++;
	}
	if ((total_1 == total_2) && (first == last))
		return (1);
	return (0);
}
