inactivity_threshold = 7200


def customer_opted_in(customer):
    return customer['opt_in']


def customer_is_active(customer):
    if customer['inactivity_timer'] > inactivity_threshold:
        return False
    return True


def customer_is_adsmart(customer):
    if customer['customer_id'] % 7 == 0:
        return False
    return True


def system_is_not_offline(customer):
    if customer['inactivity_timer'] % 9 == 0:
        return False
    return True


ad_substitution_checks = [customer_opted_in, customer_is_active, customer_is_adsmart, system_is_not_offline]