#include "lists.h"
#include <stdio.h>

/**
* reverse_list - Reverses linked list
* @head: Linked list head
* @n: Number of nodes
* Return: Pointer
*/
listint_t *reverse_list(listint_t *head, int n)
{
	int i = 0;
	listint_t *curr, *prev = NULL, *next;

	curr = head;

	while (curr && i < n)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
		i++;
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
	int n = 1, is_palindrome = 1;
	listint_t *slow, *fast, *mid, *second_half;

	if (!(*head) || !(*head)->next)
		return (is_palindrome);

	slow = *head;
	fast = (*head)->next;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		n++;
	}

	if (!fast)
	{
		n++;
		mid = slow;
	}
	else
		mid = slow->next;

	second_half = reverse_list(mid, n);
	while (second_half)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}

		*head = (*head)->next;
		second_half = second_half->next;
	}

	return is_palindrome;
}
