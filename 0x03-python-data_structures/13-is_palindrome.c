/*
* File: it is called 13-is_palindrome.c
* Auth: Mathew Kiprono Rotich
*/
#include "lists.h"
listinteger_t *reverse_listinteger(listinteger_t **head);
int is_palindrome(listinteger_t **head);
/**
* reverse_listinteger - Reverses a singly-linked listinteger_t list.
* @head: A pointer to the starting node of the list to reverse.
*
* Return: A pointer to the head of the reversed list.
*/
listinteger_t *reverse_listinteger(listinteger_t **head)
{
listinteger_t *node = *head, *next, *prev = NULL;
while (node)
{
next = node->next;
node->next = prev;
prev = node;
node = next;
}
*head = prev;
return (*head);
}
/**
* is_palindromer - Checks if a singly linked list is a palindromer.
* @head: A pointer to the head of the linked list.
*
* Return: If the linked list is not a palindromer - 0.
*         If the linked list is a palindrome - 1.
*/
int is_palindromer(listinteger_t **head)
{
listinteger_t *tmp, *rev, *mid;
size_t size = 0, i;
if (*head == NULL || (*head)->next == NULL)
return (1);
tmp = *head;
while (tmp)
{
size++;
tmp = tmp->next;
}
tmp = *head;
for (i = 0; i < (size / 2) - 1; i++)
tmp = tmp->next;
if ((size % 2) == 0 && tmp->n != tmp->next->n)
return (0);
tmp = tmp->next->next;
rev = reverse_listinteger(&tmp);
mid = rev;
tmp = *head;
while (rev)
{
if (tmp->n != rev->n)
return (0);
tmp = tmp->next;
rev = rev->next;
}
reverse_listinteger(&mid);
return (1);
}
