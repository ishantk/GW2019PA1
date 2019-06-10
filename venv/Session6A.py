def applyPromoCode(promoCode, amount):
    if promoCode == "FLAT50":
        return amount * 50//100
    elif promoCode == "FLAT30":
        return amount * 30//100
    else:
        return amount * 10//100

total = 1000
# discount = applyPromoCode("FLAT30", total)
# print("Please pay: \u20b9",total-discount)

print("Please pay: \u20b9",total-applyPromoCode("FLAT30", total))

print("applyPromoCode is:",applyPromoCode)

# Reference Copy !!
fun = applyPromoCode

print("fun is:",fun)

print("Please pay: \u20b9",total-fun("FLAT50", total))

# del applyPromoCode
# print("Please pay: \u20b9",total-applyPromoCode("FLAT30", total))

# Create a Function which applies promo code on the basis of these conditions:
# 1. Flat50 Promo Code can work only if user has total amount > 1000
# 2. Flat30 Promo Code can work only if user has total amount > 500 and < 1000
# 3. We can propose use to apply a promo code which is more beneficial foo him/her
# 4 Make user of various test cases