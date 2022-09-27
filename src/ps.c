/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps.c                                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amaria-d <amaria-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/27 10:05:38 by amaria-d          #+#    #+#             */
/*   Updated: 2022/09/27 10:18:15 by amaria-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

int main(int argc, char **argv)
{
    t_list  *args, *b;
    int     i, count;

    args = ft_lstnew(ft_atoi(argv[0]));
    i = 1;
    while (argv[i])
    {
        ft_lstadd_back(&args, ft_lstnew(ft_atoi(argv[i])));
        i++;
    }
    b = NULL;
    count = bgearSort(&args, &b);

    ft_printf("Number of moves: %d", count);
    
    return (0);
}