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
	listint_t *hare = list;
	listint_t *tort = list;

	if (!list)
		return (0);

	while (tort && hare && hare->next)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (list == hare)
			return (1);
	}
	return (0);
}
