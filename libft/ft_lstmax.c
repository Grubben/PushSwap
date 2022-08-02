#include "libft.h"

/*
Presumes t_list:content is originally int type
*/
int		ft_lstmax(t_list *lst)
{
	int	max;

	if (!lst)
	{
		ft_printf("ERROR");
		*(void *)NULL = 0;
	}
	max = lst->content;
	while (lst->next != NULL)
	{
		lst = lst -> next;
		if (lst -> content > max)
			max = lst -> content;
	}
	if (lst -> content > max)
		max = lst -> content;
	return (max);
}