#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *list;
    listint_t *tmp;

    if (!head || !*head)
        return (NULL);
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    list = *head;
    new->n = number;
    new->next = NULL;
    while (list && list->next)
    {
        if (number < list->next->n)
        {
            tmp = list->next;
            list->next = new;
            new->next = tmp;
            break;
        }
        list = list->next;
    }
    return (new);
}
