/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bgearSort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amaria-d <amaria-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/27 09:08:33 by amaria-d          #+#    #+#             */
/*   Updated: 2022/09/27 10:33:11 by amaria-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../header/push_swap.h"

size_t  bgearSort(t_list **a, t_list **b)
{
    size_t  moves, chunks;

    moves = 0;

    if (is_ascendingP(*a))
        return (0);
    
    if (turnedP(*a))
    {
        while (turnedP(*a))
        {
            r_p(a, 'a');
            moves++;
        }
        return (moves);
    }
    
    if (switchedP(*a, is_ascendingP) > (-1))
        return (swap_at(*a, switchedP(*a, is_ascendingP)));

    if (ft_lstlen(*a) < 50)
        chunks = 3;
    else if (ft_lstlen(*a) <= 100)
        chunks = 7;
    else
        chunks = 10;

    moves = moves + prepTop(a, chunks);
    p_p(b, a, 'b');
    moves++;

    while (*a)
    {
        if (turnedP(*a))
        {
            ft_printf("Turned__");
            moves = moves + set_ascending(a);
            ft_printf("Unturned a");
        }

        if (switchedP(*a, is_ascendingP) > (-1))
            swap_at(*a, switchedP(*a, is_ascendingP));
        
        if (is_ascendingP(*a) && (ft_lstmin(*a) > ft_lstmax(*b)))
        {
            moves = moves + drain(b, a);
            ft_lstprint(*a);
            break;
        }

        moves = moves + prepTop(a, chunks);

        // ft_lstprint(*a);
        // ft_lstprint(*b);

        if (ft_pslstget_it(*a, 0) < ft_lstmin(*b))
        {
            moves = moves + set_descending(b);
            p_p(b, a, 'a');
            r_p(b, 'b');
            moves = moves + 2;
        }

        else if (ft_pslstget_it(*a, 0) > ft_lstmax(*b))
        {
            moves = moves + set_descending(b);
            p_p(b, a, 'b');
            moves++;
        }
        else
        {
            moves = moves + set_descending(b);
            while (ft_pslstget_it(*a, 0) < ft_pslstget_it(*b, 0))
            {
                r_p(b, 'b');
                moves++;
            }
            p_p(b, a, 'b');
            moves++;
        }
    }

    while ((is_ascendingP(*a) && *b) && (ft_pslstget_it(*b, 0) != ft_lstmax(*b)))
    {
        r_p(b, 'b');
        moves++;
    }
    // ft_lstprint(*a);
    // ft_lstprint(*b);

    while (*b)
    {
        p_p(a, b, 'a');
        moves++;
    }
    
    // ft_printf("\n");
    // ft_lstprint(*a);

    return (moves);
}