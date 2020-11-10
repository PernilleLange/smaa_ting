def sum_timestamps(times):
    second_sum = 0
    for time in times:
        time_list = [int(comp) for comp in time.split(':')]
        if len(time_list) == 3:
            hours, minutes, seconds = time_list
            second_sum += hours * 3600 + minutes * 60 + seconds
        else:
            minutes, seconds = time_list
            second_sum += minutes * 60 + seconds
    if second_sum < 3600:
        minute_total, second_total = (str(num) for num in divmod(second_sum, 60))
        return f'{minute_total.zfill(1)}:{second_total.zfill(2)}'
    else:
        remainder = second_sum % 3600
        hour_total = int((second_sum - (remainder)) / 3600)
        minute_total, second_total = (str(num) for num in divmod(remainder, 60))
        return f'{hour_total}:{minute_total.zfill(2)}:{second_total.zfill(2)}'


