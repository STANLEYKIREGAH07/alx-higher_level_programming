#include "lists.h"

/**
 * insert_node - Inserts  number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the neww node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *neww;

	neww = malloc(sizeof(listint_t));
	if (neww == NULL)
		return (NULL);
	neww->n = number;

	if (node == NULL || node->n >= number)
	{
		neww->next = node;
		*head = neww;
		return (neww);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	neww->next = node->next;
	node->next = neww;

	return (neww);
}
