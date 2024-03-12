#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a list is cycle
 * @list: the list
 * Return: 0 / 1
 */

int check_cycle(listint_t *list)
{
	listint_t *hare;

	if (!list)
		return (0);
	hare = list->next->next;
	if (!list->next || !hare)
		return (0);
	while (list)
	{
		if (!hare)
			return (0);
		if (list == hare)
			return (1);
		list = list->next;
		hare = hare->next->next;
	}
	return (0);
}
