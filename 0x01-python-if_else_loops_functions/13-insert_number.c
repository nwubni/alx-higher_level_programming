#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
* insert_node - Inserts a node in a sorted list
* @head: Head of linked list
* @number: Value to insert
* Return: Pointer
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *curr, *prev = NULL;

	node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (!(*head))
	{
		*head = node;
		return (node);
	}
	curr = *head;
	while (curr)
	{
		if (curr->n >= node->n)
		{
			if (!prev)
			{
				node->next = curr;
				*head = node;
			}
			else
			{
				node->next = curr;
				prev->next = node;
			}
			return (node);
		}

		prev = curr;
		curr = curr->next;
	}
	prev->next = node;
	return (node);
}
