from conditions import ad_substitution_checks


def substitute_ad(customer_id, opt_in, inactivity_timer):
    customer = {'customer_id': customer_id, 'opt_in': opt_in, 'inactivity_timer': inactivity_timer}
    check_results = []
    for ad_substitution_check in ad_substitution_checks:
        check_results.append(ad_substitution_check(customer))
    print(check_results)
    if False in check_results:
        return False
    return True


print(substitute_ad(700000000001, True, 19))