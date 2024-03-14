#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *list;
    listint_t *tmp;

    if (!head)
        return (NULL);
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    list = *head;
    new->n = number;
    new->next = NULL;
    if (*head)
    {
        while (list && list->next)
        {
            if (number < list->next->n || number < (*head)->n)
            {
                if (number < (*head)->n)
                {
                    new->next = (*head);
                    *head = new;
                    break;
                }
                else
                {
                    tmp = list->next;
                    list->next = new;
                    new->next = tmp;
                }
                break;
            }
            list = list->next;
        }
        if (!list->next)
            list->next = new;
    }
    else
        *head = new;
    return (new);
}
