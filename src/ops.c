#include "../header/push_swap.h"

//Swap the first 2 elements at the top of stack
int s(t_list **stack)
{

	t_list	*oldFirst;
	t_list	*newFirst;

	if (stack && ft_lstsize(*stack) > 1)
	{
		oldFirst = *stack;
		newFirst = (*stack) -> next;
		oldFirst -> next = newFirst -> next;
		newFirst -> next = oldFirst;
		*stack = newFirst;
		return (1);
	}
	return (0);

}

int	p(t_list **stack1, t_list **stack2)
//TODO: TBC and verified
{
	t_list	*newHeadS1;
		
	if (stack2)
	{
		newHeadS1 = *stack2;
		(*stack2) = (*stack2) -> next;
		ft_lstadd_front(stack1, newHeadS1);
		return (1);
	}
	return (0);
}

int	r(t_list **stack)
//TODO: TBC and verified
{
	t_list *newTail;
	t_list	*newHead;

	if (stack)
	{
		newTail = *stack;
		newHead = (*stack) -> next;
		newTail -> next = NULL;
		ft_lstadd_back(&newHead, newTail);
		return (1);
	}
	return (0);
}

int	rr(t_list **stack)
//TODO: TBC and verified
{
	t_list	*newHead;
	t_list	*newTail;

	if (stack)
	{
		newHead = ft_lstlast(*stack);
		newTail = ft_lstindex(*stack, -2);
		newTail -> next = NULL;
		newHead -> next = *stack;
		*stack = newHead;
		return (1);
	}
	return (0);
}

int	main(void)
{
	t_list	*head;
	t_list	el;

	head = NULL;

	el.content = (void *)"good";
	el.next = NULL;

	printf("%d\n", ft_lstsize(head)); // == 0

	head = ft_lstnew((void *)"hello");
	printf("%d\n", ft_lstsize(head)); // == 1

	ft_lstadd_front(&head, &el);
	printf("%d\n", ft_lstsize(head)); // == 2

	ft_lstadd_back(&head, ft_lstnew((void *)"bye"));
	printf("%d\n", ft_lstsize(head)); // == 2

	ft_lstprint(head);

	// Check if s func works
	printf("%d\n", s(&head));
	ft_lstprint(head);
}