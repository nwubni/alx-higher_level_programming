#include "lists.h"

/**
* reverse_list - Reverses linked list
* @head: Linked list head
* @n: Number of nodes
* Return: Pointer
*/
listint_t *reverse_list(listint_t *head, int n)
{
	listint_t *curr, *prev = NULL, *next;

	curr = head;

	while (curr && n >= 0)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
		n--;
	}

	return (prev);
}

/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: Linked list head
* Return: Integer
*/

int is_palindrome(listint_t **head)
{
	int n = 0, is_palindrome = 1;
	listint_t *slow, *fast;

	if (!(*head) || !(*head)->next)
		return (is_palindrome);

	slow = *head;
	fast = (*head)->next->next;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		n++;
	}

	if (fast)
		n++;

	fast = slow->next;
	slow = reverse_list(*head, n);

	while (slow && fast)
	{
		if (slow->n != fast->n)
		{
			is_palindrome = 0;
			break;
		}

		slow = slow->next;
		fast = fast->next;
	}

	return (is_palindrome);
}
