#include "lists.h"
int is_palindrome(listint_t **head)
{
	int arr[5000], len, i;
	listint_t *tmp = *head;

	if (!*head)
		return (1);
	for (len = 0; tmp; len++)
	{
		arr[len] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0, tmp = *head, len--; tmp; tmp = tmp->next, i++, len--)
		if (tmp->n != arr[len])
			return (-1);

	return (1);
}
