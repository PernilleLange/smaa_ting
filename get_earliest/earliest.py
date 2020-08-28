def get_earliest(*date_tuple):
    earliest_year = date_tuple[0][-4:]
    earliest_month = date_tuple[0][0:2]
    earliest_day = date_tuple[0][3:5]
    for date in date_tuple:
        year = date[-4:]
        month = date[0:2]
        day = date[3:5]
        if year < earliest_year:
            earliest_year = year
            earliest_month = month
            earliest_day = day
        elif year == earliest_year:
            if month < earliest_month:
                earliest_month = month
                earliest_day = day
            elif month == earliest_month:
                if day < earliest_day:
                    earliest_day = day
    earliest_date = earliest_month + '/' + earliest_day + '/' + earliest_year

    return (earliest_date)
