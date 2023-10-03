#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the linked list.
 * @number: the value of the newly created node.
 *
 * Return: the address of the new node, or NULL if it faile.
 **/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL, *tmp;

	/* initialize the new node */
	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	/* if the linked list is empty */
	if (!head || *head == NULL)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	/* loop through the linked list and the node before the node with n>number*/
	tmp = *head;
	while (tmp)
	{
		if (tmp->n > number)	/* handle the newnode at the beginning */
		{
			newnode->next = tmp;
			*head = newnode;
			break;
		}
		else if (tmp->next == NULL) /* handle the new node at the end */
		{
			tmp->next = newnode;
			newnode->next = NULL;
			break;
		}
		else if ((tmp->next)->n > number)
		{
			newnode->next = tmp->next;
			tmp->next = newnode;
			break;
		}
		tmp = tmp->next;
	}
	return (newnode);
}
