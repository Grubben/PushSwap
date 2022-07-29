/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstindex.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amc <amc@student.42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/29 15:56:37 by amc               #+#    #+#             */
/*   Updated: 2022/07/29 15:56:47 by amc              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstindex(t_list *lst, ssize_t index)
{
	int		size;
	int		i;

	if (index == 0)
		return (lst);
	if (index > 0)
	{
		while (index > 0)
		{
			lst = lst -> next;
			// I dont check if it's ever NULL
			index--;
		}
		return (lst);
	}
	if (index == -1)
		return ft_lstlast(lst);
	// if (index < 0)
	size = ft_lstsize(lst);
	if (-index > size)
		return (NULL);
	i = 0;
	while (i < size + index)
	{
		lst = lst -> next;
		i++;
	}
	return (lst);
}