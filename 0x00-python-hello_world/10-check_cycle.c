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

	if (!list || !list->next)
		return (0);
	hare = list;
	while (list && hare && hare->next)
	{
		list = list->next;
		hare = hare->next->next;
		if (list == hare)
			return (1);
	}
	return (0);
}
