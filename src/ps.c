/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps.c                                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amaria-d <amaria-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/27 10:05:38 by amaria-d          #+#    #+#             */
/*   Updated: 2022/09/27 10:54:46 by amaria-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include "../header/push_swap.h"

int main(int argc, char **argv)
{
    t_list  *args, *b;
    int     i, count;
    int     *tmp;

    if (argc < 2)
        return (0);
    tmp = ft_calloc(1, sizeof(int));
    *tmp = ft_atoi(argv[1]);
    args = ft_lstnew(tmp);
    i = 2;
    while (argv[i])
    {
        tmp = ft_calloc(1, sizeof(int));
        *tmp = ft_atoi(argv[i]);
        ft_lstadd_back(&args, ft_lstnew(tmp));
        i++;
    }
    b = NULL;
    // ft_lstprint(args);
    // ft_lstprint(b);
    // ft_printf("\n");

    count = bgearSort(&args, &b);
    // count = 0;

    ft_lstclear(&args, free);
    ft_lstclear(&b, free);

    ft_printf("Number of moves: %d", count);
    
    return (0);
}