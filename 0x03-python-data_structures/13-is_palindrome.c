#include "lists.h"

/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: Linked list head
* Return: Integer
*/

int is_palindrome(listint_t **head)
{
	int *tmp = NULL, i = 0, j = 0, is_palindrome = 1;
	listint_t *curr = NULL;

	curr = *head;

	while (curr)
	{
		tmp = realloc(tmp, sizeof(int) * (i + 1));
		tmp[i] = curr->n;
		i++;
		curr = curr->next;
	}

	j = i - 1;
	i = 0;

	while (i < j)
	{
		if (tmp[i] != tmp[j - i])
		{
			is_palindrome = 0;
			break;
		}

		i++;
	}

	free(tmp);
	return (is_palindrome);
}
