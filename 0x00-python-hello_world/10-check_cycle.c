#include "lists.h"

/**
 * check_cyle - checks for a cyle within a linked list
 * @list: list to be checked
 * Return: 1(has cyle) or 0(Does not)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;

	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
