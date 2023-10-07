#include "lists.h"
int is_palindrome(listint_t **head)
{
	int len, half, sum1, sum2, i;
	listint_t *tmp = *head;

	len = linked_length(*head);
	half = len / 2;
	sum1 = sum2 = i = 0;

	if (len == 0)
		return (1);
	else if (len % 2 != 0)
		return (-1);

	while (tmp)
	{
		i++;
		if (i <= half)
			sum1 += tmp->n;
		else if (i > half)
			sum2 += tmp->n;
		tmp = tmp->next;
	}
	if (sum1 == sum2)
		return (1);
	else
		return (-1);
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
