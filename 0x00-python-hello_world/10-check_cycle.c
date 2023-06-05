#include "lists.h"

/**
* check_cycle - Checks for cycle in linked list
* @list: Head of linked list
* Return: Integer
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
