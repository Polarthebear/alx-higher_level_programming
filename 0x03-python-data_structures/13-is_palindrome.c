#include "lists.h"

/**
 * rev_listint - main entry point
 * Description: reverses a linked list
 * @head: pointer to first node
 * Return: pointer to first node in new list
 */
void rev_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

}

/**
 * is_palindrome - main entry point
 * Description: Checks if a list is a palindrome
 * @head: **linked list
 * Return: 1 (Success) 0 (Fail)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw = *head, *fst = *head, *tmp = *head, *dupli = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fst = fst->next->next;
		if (!fst)
		{
			dupli = slw->next;
			break;
		}
		if (!fst->next)
		{
			dupli = slw->next->next;
			break;
		}
		slw = slw->next;
	}

	rev_listint(&dupli);

	while (dupli && tmp)
	{
		if (tmp->n == dupli->n)
		{
			dupli = dupli->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dupli)
		return (1);

	return (0);
}
