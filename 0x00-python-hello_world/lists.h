#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>
/**
 * struct linked_lists - singly linked lists.
 * @p: integers
 * @next: points to the next node
 *
 * Descriptions: singly linked lists node structures
 * for Alx project
 */
typedef struct linked_lists
{
	int p;
	struct linked_lists *next;
} linked_list_t;
size_t print_listint(const linked_list_t *h);
linked_list_t *add_nodeint(linked_list_t **head, const int p);
void free_listint(linked_list_t *head);
int check_cycle(linked_list_t *list);
#endif

