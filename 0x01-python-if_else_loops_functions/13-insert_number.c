#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into sorted linked list
 * @head: pointer to head of list
 * @number: number to be inserted into new node
 * Return: pointer to new node or 0 Upon Error
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *tmp = NULL;
listint_t *new = NULL;
if (head == NULL)
return (NULL);
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
new->next = NULL;
/*if there is no node insert as new node */
if (*head == NULL)
{
*head = new;
(*head)->next = NULL;
return (new);
}
/* if there is only one node compare and insert */
if ((*head)->next == NULL)
{
if ((*head)->n < new->n)
(*head)->next = new;
else
{
new->next = *head;
*head = new;
}
return (new);
}
/* if many nodes do comparison and insert */
tmp = *head;
while (tmp->next != NULL)
{
if (new->n < tmp->n)
{
new->next = tmp;
*head = new;
return (new);
}
if (((new->n > tmp->n) && (new->n < (tmp->next)->n)) || (new->n == tmp->n))
{
new->next = tmp->next;
tmp->next = new;
return (new);
}
tmp = tmp->next;
}
tmp->next = new;
return (new);
}
