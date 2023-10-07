#include "lists.h"
int is_palindrome(listint_t **head)
{
	int len, half, i;
	listint_t *sechalf = *head;
	int *firsthalf;

	len = linked_length(*head);
	half = len / 2;

	if (len == 0)
		return (1);

	firsthalf = malloc(sizeof(int) * half);
	for (i = 0; i < half; i++)
	{
		firsthalf[i] = sechalf->n;
		sechalf = sechalf->next;
	}
	for (i = half - 1; i > 0; i--)
	{
		if (firsthalf[i] != sechalf->n)
		{
			free(firsthalf);
			return (-1);
		}
		sechalf = sechalf->next;
	}
	free(firsthalf);
	return (1);
}


int linked_length(listint_t *head)
{
	listint_t *tmp = head;
	int count = 0;

	if (!head)
		return (0);
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}
